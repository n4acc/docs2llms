from dataclasses import dataclass
from typing import List, Optional
from bs4 import BeautifulSoup
import re

@dataclass
class DocStructure:
    title: Optional[str] = None
    description: Optional[str] = None
    sections: dict[str, List[tuple[str, str, str]]] = None  # section_name: [(title, url, description)]
    
    def __post_init__(self):
        if self.sections is None:
            self.sections = {}

class DocParser:
    def __init__(self, doc_type: str = "auto"):
        """
        Initialize parser with doc_type: 'sphinx', 'mkdocs', 'docusaurus', or 'auto'
        """
        self.doc_type = doc_type
        self.patterns = {
            'sphinx': {
                'nav': '.sphinxsidebar',
                'content': '.body',
                'title': '.document h1',
                'description': '.document .topic-title + p'
            },
            'mkdocs': {
                'nav': '.md-nav',
                'content': '.md-content',
                'title': 'h1',
                'description': '.md-content > p:first-of-type'
            },
            'docusaurus': {
                'nav': '.menu',
                'content': 'article',
                'title': 'h1',
                'description': 'article > p:first-of-type'
            }
        }
    
    def detect_doc_type(self, soup: BeautifulSoup) -> str:
        """Detect documentation system type from page structure"""
        if soup.select('.sphinxsidebar'):
            return 'sphinx'
        elif soup.select('.md-nav'):
            return 'mkdocs'
        elif soup.select('.menu') and soup.select('[class*="docusaurus"]'):
            return 'docusaurus'
        return 'generic'
    
    def extract_structure(self, soup: BeautifulSoup) -> DocStructure:
        if self.doc_type == 'auto':
            self.doc_type = self.detect_doc_type(soup)
            
        patterns = self.patterns.get(self.doc_type, {
            'nav': 'nav',
            'content': 'main',
            'title': 'h1',
            'description': 'main > p:first-of-type'
        })
        
        structure = DocStructure()
        
        # Extract title
        title_elem = soup.select_one(patterns['title'])
        if title_elem:
            structure.title = title_elem.get_text(strip=True)
        
        # Extract description
        desc_elem = soup.select_one(patterns['description'])
        if desc_elem:
            structure.description = desc_elem.get_text(strip=True)
        
        # Extract navigation structure
        nav = soup.select_one(patterns['nav'])
        if nav:
            self._parse_navigation(nav, structure)
            
        return structure
    
    def _parse_navigation(self, nav: BeautifulSoup, structure: DocStructure):
        """Parse navigation structure based on doc type"""
        current_section = "Documentation"
        
        for elem in nav.find_all(['a', 'h2', 'h3']):
            if elem.name in ['h2', 'h3']:
                current_section = elem.get_text(strip=True)
                if current_section not in structure.sections:
                    structure.sections[current_section] = []
            elif elem.name == 'a':
                href = elem.get('href', '')
                if href and not href.startswith(('#', 'javascript:')):
                    title = elem.get_text(strip=True)
                    description = self._extract_link_description(elem)
                    structure.sections[current_section].append((title, href, description))
    
    def _extract_link_description(self, link_elem: BeautifulSoup) -> str:
        """Extract description from link context"""
        next_elem = link_elem.find_next_sibling()
        if next_elem and next_elem.name == 'p':
            return next_elem.get_text(strip=True)
        return "" 