from dataclasses import dataclass
from typing import List, Optional
import re

@dataclass
class Section:
    title: str
    content: str
    subsections: List['Section']
    level: int

class SectionExtractor:
    def __init__(self):
        self.header_pattern = re.compile(r'^(#{1,6})\s+(.+)$', re.MULTILINE)
    
    def extract_sections(self, content: str) -> List[Section]:
        """Extract hierarchical sections from markdown content"""
        lines = content.split('\n')
        root_sections = []
        current_sections = {0: root_sections}
        current_content = []
        current_level = 0
        
        for line in lines:
            header_match = self.header_pattern.match(line)
            if header_match:
                # Save current content if any
                if current_content and current_level in current_sections:
                    self._add_content_to_section(
                        current_sections[current_level],
                        '\n'.join(current_content)
                    )
                
                level = len(header_match.group(1))
                title = header_match.group(2)
                
                section = Section(title=title, content='', subsections=[], level=level)
                
                if level > current_level:
                    parent_sections = current_sections[current_level]
                    if parent_sections:
                        parent_sections[-1].subsections.append(section)
                    current_sections[level] = [section]
                else:
                    current_sections[level] = [section]
                    if level in current_sections:
                        current_sections[level].append(section)
                
                current_level = level
                current_content = []
            else:
                current_content.append(line)
        
        return root_sections
    
    def _add_content_to_section(self, sections: List[Section], content: str):
        if sections:
            sections[-1].content += content 