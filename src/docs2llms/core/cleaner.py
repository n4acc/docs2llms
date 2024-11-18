import re
from bs4 import BeautifulSoup
from typing import List

class ContentCleaner:
    def __init__(self):
        self.replacements = [
            (r'\n{3,}', '\n\n'),  # Replace multiple newlines
            (r'\s+```', '\n```'),  # Fix code block formatting
            (r'```\s+', '```\n'),  # Fix code block formatting
        ]
    
    def clean(self, content: str) -> str:
        """Clean content for LLM consumption"""
        # Remove HTML if present
        if bool(BeautifulSoup(content, "html.parser").find()):
            content = self._clean_html(content)
            
        # Apply regex replacements
        for pattern, replacement in self.replacements:
            content = re.sub(pattern, replacement, content)
            
        # Ensure code blocks are properly formatted
        content = self._format_code_blocks(content)
        
        return content.strip()
    
    def _clean_html(self, content: str) -> str:
        soup = BeautifulSoup(content, 'html.parser')
        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.decompose()
        return soup.get_text()
    
    def _format_code_blocks(self, content: str) -> str:
        """Ensure code blocks are properly formatted"""
        lines = content.split('\n')
        in_code_block = False
        formatted_lines = []
        
        for line in lines:
            if line.strip().startswith('```'):
                in_code_block = not in_code_block
                if in_code_block and len(line.strip()) == 3:
                    # Add a default language identifier
                    line = '```python'
            formatted_lines.append(line)
            
        return '\n'.join(formatted_lines) 