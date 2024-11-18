from dataclasses import dataclass
from typing import List, Dict, Optional
import logging
from tqdm import tqdm
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright
import os
import re
from pathlib import Path
import asyncio
from collections import deque

@dataclass
class CrawlConfig:
    max_pages: int = 100
    max_depth: int = 3
    pages_per_minute: int = 10
    wait_time: int = 30
    retry_attempts: int = 3
    exclude_patterns: List[str] = None
    include_patterns: List[str] = None
    debug: bool = False

class Docs2LLMs:
    def __init__(self, config: Optional[CrawlConfig] = None):
        self.config = config or CrawlConfig()
        self.logger = logging.getLogger(__name__)
        self.visited_urls = set()
        self.failed_urls = set()
        self.progress = tqdm(total=100, desc="Converting docs")

    async def convert(self, url: str) -> str:
        """Convert documentation to llms.txt format"""
        try:
            self.logger.debug("Starting conversion")
            async with async_playwright() as p:
                browser = await p.chromium.launch()
                context = await browser.new_context()
                
                try:
                    pages = await self._crawl_pages(context, url)
                    self.logger.debug(f"Crawled {len(pages)} pages successfully")
                    
                    if not pages:
                        self.logger.warning("No pages were crawled successfully")
                        return "# No content found\n\n> No documentation content could be extracted."
                    
                    return self._generate_llms_txt(pages)
                    
                finally:
                    await context.close()
                    await browser.close()
                    
        except Exception as e:
            self.logger.error(f"Conversion failed: {str(e)}", exc_info=True)
            raise

    def _extract_title(self, soup: BeautifulSoup) -> str:
        """Extract page title"""
        title = soup.find('title')
        if title:
            return title.get_text(strip=True)
        h1 = soup.find('h1')
        if h1:
            return h1.get_text(strip=True)
        return "Documentation"

    def _extract_description(self, soup: BeautifulSoup) -> Optional[str]:
        """Extract page description"""
        meta_desc = soup.find('meta', {'name': 'description'})
        if meta_desc and meta_desc.get('content'):
            return meta_desc['content']
        
        first_p = soup.find('p')
        if first_p:
            text = first_p.get_text(strip=True)
            if text and len(text) > 20:
                return text
        return None

    def _extract_main_content(self, soup: BeautifulSoup) -> str:
        """Extract main content from page"""
        self.logger.debug("Trying content selectors")
        
        # Try different content selectors
        for selector in ['main', 'article', '.content', '#content', '.documentation', '#__next']:
            self.logger.debug(f"Trying selector: {selector}")
            content = soup.select_one(selector)
            if content:
                self.logger.debug(f"Found content with selector: {selector}")
                
                # Remove unwanted elements
                for element in content.select('nav, header, footer, .navigation, .sidebar'):
                    element.decompose()
                
                return content.get_text(strip=True)
        
        # Fallback to body if no content found
        return soup.body.get_text(strip=True) if soup.body else ""

    def _generate_llms_txt(self, pages: List[Dict]) -> str:
        """Generate llms.txt format from processed pages"""
        if not pages:
            return "# No content found\n\n> No documentation content could be extracted."
        
        output = []
        
        # Add title and description from first page
        title = pages[0].get('title', 'Documentation')
        output.append(f"# {title}\n")
        
        description = pages[0].get('description', 'Documentation and reference materials.')
        output.append(f"> {description}\n")
        
        # Add main sections
        sections = self._organize_sections(pages)
        
        for section_name, section_links in sections.items():
            if section_links:  # Only add sections that have content
                output.append(f"\n## {section_name}\n")
                
                for link in section_links:
                    # Add the link with its title
                    output.append(f"\n- [{link['text']}]({link['url']})")
                    
                    # Add description if available and meaningful
                    if link.get('description') and len(link['description']) > 20:
                        output.append(f"  {link['description']}")
        
        return "\n".join(output)

    async def _crawl_pages(self, context, start_url: str, *, save_markdown: bool = False, 
                          markdown_dir: str = None, include_related: bool = False) -> List[Dict]:
        """Crawl documentation pages using a queue-based approach"""
        pages = []
        self.visited_urls: Set[str] = set()
        self.failed_urls: Set[str] = set()
        url_queue: Deque[tuple[str, int]] = deque([(start_url, 0)])  # (url, depth)
        
        # Extract base domain and path
        base_path = '/'.join(start_url.split('/')[:-1])   # Gets path without filename
        self.logger.debug(f"Base path: {base_path}")
        
        # Setup markdown directory if needed
        output_path = None
        if save_markdown and markdown_dir:
            output_path = Path(markdown_dir)  # Use the provided directory name
            output_path.mkdir(parents=True, exist_ok=True)
        
        async def process_page(url: str, depth: int) -> List[str]:
            """Process a single page and return valid links"""
            if depth >= self.config.max_depth or len(pages) >= self.config.max_pages:
                self.logger.debug(f"Skipping {url}: depth={depth}, pages={len(pages)}")
                return []
            
            page = await context.new_page()
            try:
                await page.set_viewport_size({"width": 1280, "height": 800})
                
                # Try loading the page
                try:
                    response = await page.goto(url, wait_until='domcontentloaded', timeout=15000)
                    if not response or response.status >= 400:
                        self.failed_urls.add(url)
                        self.logger.warning(f"Failed to load {url} (status: {response.status if response else 'None'})")
                        return []
                except Exception as e:
                    self.failed_urls.add(url)
                    self.logger.error(f"Error loading {url}: {str(e)}")
                    return []

                # Get page content
                html_content = await page.content()
                self.logger.debug(f"Got HTML content for {url} ({len(html_content)} bytes)")
                
                soup = BeautifulSoup(html_content, 'html.parser')
                
                # Extract content based on mode
                if save_markdown:
                    main_content = self._extract_markdown_content(soup)
                    self.logger.debug(f"Extracted markdown content: {len(main_content)} chars")
                else:
                    main_content = self._extract_main_content(soup)
                    self.logger.debug(f"Extracted main content: {len(main_content)} chars")
                
                if not main_content:
                    return []

                # Get all links
                all_links = await page.evaluate('''
                    () => Array.from(document.querySelectorAll('a[href]')).map(a => {
                        try {
                            return {
                                href: new URL(a.href, window.location.href).href,
                                text: a.textContent.trim()
                            }
                        } catch {
                            return null;
                        }
                    }).filter(link => link !== null)
                ''')
                
                # Create page data
                page_data = {
                    'url': url,
                    'title': self._extract_title(soup),
                    'content': main_content,
                    'description': self._extract_description(soup),
                    'links': all_links
                }
                
                # Save markdown file immediately if requested
                if save_markdown and output_path:
                    try:
                        relative_url = self._get_relative_path(url)
                        file_path = output_path / f"{relative_url}.md"
                        file_path.parent.mkdir(parents=True, exist_ok=True)
                        
                        markdown_content = self._generate_page_markdown(page_data, include_related)
                        
                        self.logger.debug(f"Saving markdown to: {file_path}")
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(markdown_content)
                    except Exception as e:
                        self.logger.error(f"Error saving markdown for {url}: {str(e)}")
                
                pages.append(page_data)
                
                # Process valid links
                valid_links = []
                for link in all_links:
                    href = link['href'].split('#')[0].rstrip('/')
                    
                    # Skip if already processed or queued
                    if href in self.visited_urls or href in self.failed_urls:
                        continue
                        
                    # Only process links from same path
                    if not href.startswith(base_path):
                        continue
                        
                    # Skip asset and API paths
                    if any(p in href.lower() for p in ['/static/', '/assets/', '/cdn-cgi/', '.css', '.js', '/search']):
                        continue
                        
                    # Skip non-documentation files
                    if href.endswith(('.png', '.jpg', '.gif', '.ico', '.woff', '.ttf')):
                        continue
                        
                    valid_links.append(href)
                
                unique_links = list(set(valid_links))
                self.logger.debug(f"Found {len(unique_links)} valid links to process")
                
                return unique_links
                
            finally:
                await page.close()

        try:
            self.progress = tqdm(total=self.config.max_pages, desc="Converting docs")
            
            # Process pages in parallel batches
            while url_queue and len(pages) < self.config.max_pages:
                # Get batch of URLs to process
                batch_size = min(5, len(url_queue))
                batch = []
                
                for _ in range(batch_size):
                    if not url_queue:
                        break
                    url, depth = url_queue.popleft()
                    if url not in self.visited_urls and url not in self.failed_urls:
                        batch.append((url, depth))
                        self.visited_urls.add(url)
                
                if not batch:
                    continue
                
                # Process batch concurrently
                tasks = [process_page(url, depth) for url, depth in batch]
                results = await asyncio.gather(*tasks, return_exceptions=True)
                
                # Add new URLs to queue
                for result in results:
                    if isinstance(result, list):  # Skip exceptions
                        for new_url in result:
                            if new_url not in self.visited_urls and new_url not in self.failed_urls:
                                url_queue.append((new_url, depth + 1))
                
                self.progress.update(len(batch))
                
            return pages
            
        finally:
            self.progress.close()

    def _get_valid_links(self, links: List[Dict], base_url: str) -> List[str]:
        """Filter and return valid documentation links"""
        valid_links = []
        base_url = base_url.rstrip('/')
        
        for link in links:
            href = link['href'].split('#')[0].rstrip('/')
            
            # Skip if not an internal doc link
            if not href.startswith(base_url):
                continue
            
            # Skip asset and API paths
            if any(p in href.lower() for p in ['/static/', '/assets/', '/api/', '/cdn-cgi/']):
                continue
            
            # Skip non-documentation files
            if href.endswith(('.js', '.css', '.png', '.jpg', '.gif', '.ico')):
                continue
            
            # Skip navigation links
            if link['text'].lower() in ['previous', 'next', 'skip to content']:
                continue
            
            valid_links.append(href)
        
        return list(set(valid_links))  # Remove duplicates

    def _extract_markdown_content(self, soup: BeautifulSoup) -> str:
        """Extract content preserving more structure for markdown output"""
        # Try different content selectors
        selectors = [
            'main',
            'article',
            '.content', 
            '#content',
            '.documentation',
            '#__next',
            '.markdown-body',
            '[role="main"]'
        ]
        
        main_content = None
        for selector in selectors:
            self.logger.debug(f"Trying markdown selector: {selector}")
            main_content = soup.select_one(selector)
            if main_content:
                self.logger.debug(f"Found content with selector: {selector}")
                break
        
        if not main_content:
            self.logger.warning("No main content container found")
            return ""
        
        # Remove navigation and unwanted elements
        for selector in ['nav', 'header', 'footer', '.navigation', '.sidebar', 
                        '.table-of-contents', '.edit-page', '.page-nav']:
            for element in main_content.select(selector):
                element.decompose()
        
        # Convert to markdown while preserving structure
        content = []
        
        for element in main_content.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 
                                            'ul', 'ol', 'pre', 'blockquote', 'div']):
            if element.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                text = element.get_text(strip=True)
                if text:  # Only add non-empty headers
                    content.append(f"\n{'#' * int(element.name[1])} {text}\n")
            
            elif element.name == 'p':
                text = element.get_text(strip=True)
                if text:  # Only add non-empty paragraphs
                    content.append(text)
            
            elif element.name in ['ul', 'ol']:
                for li in element.find_all('li', recursive=False):
                    text = li.get_text(strip=True)
                    if text:  # Only add non-empty list items
                        content.append(f"- {text}")
            
            elif element.name == 'pre':
                code = element.get_text(strip=True)
                if code:  # Only add non-empty code blocks
                    # Try to detect language from class
                    classes = element.get('class', [])
                    lang = next((c for c in classes if c.startswith('language-')), '')
                    lang = lang.replace('language-', '') if lang else ''
                    content.append(f"```{lang}\n{code}\n```")
            
            elif element.name == 'blockquote':
                text = element.get_text(strip=True)
                if text:  # Only add non-empty blockquotes
                    content.append(f"> {text}")
            
            elif element.name == 'div' and element.get('class'):
                # Handle special div containers (like code examples)
                classes = element.get('class')
                if any('code' in c.lower() for c in classes):
                    code = element.get_text(strip=True)
                    if code:
                        content.append(f"```\n{code}\n```")
        
        markdown = "\n\n".join(content)
        
        # Clean up extra whitespace while preserving structure
        markdown = re.sub(r'\n{3,}', '\n\n', markdown)
        markdown = markdown.strip()
        
        return markdown

    def _organize_sections(self, pages: List[Dict]) -> Dict[str, List[Dict]]:
        """Organize documentation links into logical sections"""
        self.logger.debug("Starting section organization")
        
        sections = {
            'Getting Started': [],
            'Model Endpoints': [],
            'Client SDKs': [],
            'Authentication': [],
            'Integrations': [],
            'Private Serverless': [],
            'Guides': [],
            'Reference': []
        }
        
        # Keep track of processed URLs and titles to avoid duplicates
        processed_urls = set()
        processed_titles = set()
        
        def add_to_section(section: str, link: Dict) -> bool:
            """Add link to section if not already processed"""
            url_without_fragment = link['url'].split('#')[0]
            title = link['text'].strip()
            
            # Skip navigation links and duplicates
            if (any(x in title.lower() for x in ['previous', 'next', 'skip to content', 'overview']) or
                url_without_fragment in processed_urls or
                title in processed_titles):
                return False
            
            processed_urls.add(url_without_fragment)
            processed_titles.add(title)
            sections[section].append(link)
            self.logger.debug(f"Added to {section}: {title} ({url_without_fragment})")
            return True

        # Process each page
        for page in pages:
            url = page['url'].lower()
            
            # Create link entry with description
            page_link = {
                'url': page['url'],
                'text': page['title'],
                'description': page.get('description', '')
            }
            
            # Determine section based on URL path components
            if any(x in url for x in ['introduction', 'quick-start', 'quickstart']):
                add_to_section('Getting Started', page_link)
            elif 'model-endpoints' in url:
                add_to_section('Model Endpoints', page_link)
            elif 'clients' in url:
                add_to_section('Client SDKs', page_link)
            elif 'authentication' in url or 'secrets' in url:
                add_to_section('Authentication', page_link)
            elif 'integrations' in url:
                add_to_section('Integrations', page_link)
            elif 'private-serverless' in url:
                add_to_section('Private Serverless', page_link)
            elif any(x in url for x in ['guide', 'guidelines', 'tutorial', 'how-to']):
                add_to_section('Guides', page_link)
            else:
                add_to_section('Reference', page_link)
        
        # Remove empty sections and sort links
        organized = {}
        for section_name, links in sections.items():
            if links:
                # Sort links by title
                sorted_links = sorted(links, key=lambda x: x['text'].lower())
                # Move introduction/overview to top if present
                sorted_links = sorted(sorted_links, 
                                    key=lambda x: 0 if 'introduction' in x['text'].lower() else 1)
                organized[section_name] = sorted_links
                
        self.logger.debug(f"Organized into {len(organized)} sections")
        return organized

    def __del__(self):
        """Ensure progress bar is closed on object destruction"""
        if hasattr(self, 'progress'):
            self.progress.close()

    def save_markdown_files(self, pages: List[Dict], output_dir: str, include_related: bool = False):
        """Save markdown files from crawled pages"""
        self.logger.info(f"Saving markdown docs to: {output_dir}")
        
        # Create output directory
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        for page in pages:
            if not page.get('content'):
                continue
                
            # Create filename from URL
            relative_url = self._get_relative_path(page['url'])
            file_path = output_path / f"{relative_url}.md"
            
            # Create subdirectories if needed
            file_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Generate markdown content
            markdown_content = self._generate_page_markdown(page, include_related)
            
            # Save to file
            self.logger.debug(f"Saving markdown to: {file_path}")
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
                
        self.logger.info(f"Saved {len(pages)} markdown files to {output_dir}")

    def _get_relative_path(self, base_url: str) -> str:
        """Convert URL to relative file path"""
        # Remove protocol and domain
        base = re.sub(r'https?://[^/]+/', '', base_url)
        
        # Remove trailing slashes and .html
        base = re.sub(r'(index)?(\.html?|\.mdx?)?/?$', '', base)
        
        # Convert to safe filename
        safe_path = re.sub(r'[^\w/\-.]', '_', base)
        
        # Use index for root
        if not safe_path:
            return 'index'
            
        return safe_path

    def _generate_page_markdown(self, page: Dict, include_related: bool = True) -> str:
        """Generate markdown content for a page"""
        output = []
        
        # Add title
        if page.get('title'):
            output.append(f"# {page['title']}\n")
        
        # Add description if available
        if page.get('description'):
            output.append(f"> {page['description']}\n")
        
        # Add main content
        if page.get('content'):
            output.append(page['content'])
        
        # Add link section if there are internal links and it's not disabled
        if include_related:
            internal_links = [link for link in page.get('links', []) 
                            if link['href'].startswith(page['url'].split('/')[0])]
            if internal_links:
                output.append("\n## Related Pages\n")
                for link in internal_links:
                    output.append(f"- [{link['text']}]({link['href']})")
        
        return "\n\n".join(output)

    def create_megadump(self, pages: List[Dict], output_file: str):
        """Combine all documentation into a single markdown file"""
        self.logger.info(f"Creating megadump file: {output_file}")
        
        output = []
        
        # Add title and description from first page
        if pages:
            title = pages[0].get('title', 'Documentation')
            output.append(f"# {title} - Complete Documentation\n")
            
            description = pages[0].get('description', 'Complete documentation dump.')
            output.append(f"> {description}\n")
        
        # Add table of contents
        output.append("\n## Table of Contents\n")
        for i, page in enumerate(pages, 1):
            title = page.get('title', f'Page {i}')
            output.append(f"{i}. [{title}](#{self._make_anchor(title)})")
        
        # Add content from each page
        for i, page in enumerate(pages, 1):
            output.append(f"\n\n{'#' * 2} {page.get('title', f'Page {i}')}\n")
            
            if page.get('description'):
                output.append(f"> {page.get('description')}\n")
                
            if page.get('content'):
                output.append(page['content'])
                
            # Add source URL
            output.append(f"\n*Source: [{page['url']}]({page['url']})*")
            
            # Add separator between pages
            if i < len(pages):
                output.append("\n---\n")
        
        # Write to file
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(output))
        
        self.logger.info(f"Megadump created with {len(pages)} pages")

    def _make_anchor(self, text: str) -> str:
        """Convert text to GitHub-style anchor"""
        # Convert to lowercase and replace spaces with hyphens
        anchor = text.lower().replace(' ', '-')
        # Remove any character that isn't alphanumeric or hyphen
        anchor = re.sub(r'[^\w\-]', '', anchor)
        return anchor