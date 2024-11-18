from dataclasses import dataclass
from typing import List, Optional
from pathlib import Path

@dataclass
class CrawlConfig:
    max_pages: int = 100
    max_depth: int = 3
    pages_per_minute: int = 10
    wait_time_between_chunks: int = 30
    retry_attempts: int = 3
    exclude_patterns: List[str] = None
    include_patterns: List[str] = None
    debug: bool = False
    
    def __post_init__(self):
        self.exclude_patterns = self.exclude_patterns or [
            r'.*(\.pdf|\.zip|\.js|\.css|\.png|\.jpg|\.jpeg|\.gif)$',
            r'.*/static/.*',
            r'.*/assets/.*',
            r'.*/blog/.*',
            r'.*/changelog/.*',
        ]
        self.include_patterns = self.include_patterns or [
            r'.*/docs/.*',
            r'.*/documentation/.*',
            r'.*/guide/.*',
            r'.*/tutorial/.*'
        ]