import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from typing import Optional
from pathlib import Path
from .parser import DocParser
from urllib.parse import urlparse

class DocsSpider(CrawlSpider):
    name = 'docs_spider'
    
    def __init__(self, url: str, doc_type: str = 'auto', 
                 max_depth: int = 3, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set start URL and allowed domains
        self.start_urls = [url]
        parsed_url = urlparse(url)
        self.allowed_domains = [parsed_url.netloc]
        
        # Initialize parser and storage
        self.doc_parser = DocParser(doc_type)
        self.structure = {
            'title': None,
            'description': None,
            'sections': {}
        }
        
        # Define crawling rules
        self.rules = (
            Rule(
                LinkExtractor(
                    allow=r'.*',
                    deny=[
                        r'.*(\.pdf|\.zip|\.js|\.css|\.png|\.jpg|\.jpeg|\.gif)$',
                        r'.*/static/.*',
                        r'.*/assets/.*',
                        r'.*/blog/.*',
                        r'.*/changelog/.*',
                    ],
                    deny_domains=['github.com', 'twitter.com', 'linkedin.com'],
                ),
                callback='parse_page',
                follow=True,
                cb_kwargs={'depth': 0}
            ),
        )
        
        self.max_depth = max_depth
        
    def parse_page(self, response, depth: int):
        if depth > self.max_depth:
            return
            
        # Parse the page using BeautifulSoup through our DocParser
        soup = BeautifulSoup(response.text, 'html.parser')
        page_structure = self.doc_parser.extract_structure(soup)
        
        # Store the main page info (title/description) only from the root page
        if response.url in self.start_urls:
            self.structure['title'] = page_structure.title
            self.structure['description'] = page_structure.description
        
        # Store section information
        for section_name, links in page_structure.sections.items():
            if section_name not in self.structure['sections']:
                self.structure['sections'][section_name] = []
            self.structure['sections'][section_name].extend(links)
        
        yield {
            'url': response.url,
            'title': page_structure.title,
            'sections': page_structure.sections
        }