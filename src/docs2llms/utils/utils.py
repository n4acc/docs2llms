import time
from typing import Optional
from tqdm import tqdm
import logging

class RateLimiter:
    def __init__(self, pages_per_minute: int = 10, wait_time_between_chunks: int = 30):
        self.pages_per_minute = pages_per_minute
        self.wait_time_between_chunks = wait_time_between_chunks
        self.chunk_size = pages_per_minute
        
    def wait_if_needed(self, processed_count: int):
        """Wait between chunks to respect rate limits"""
        if processed_count % self.chunk_size == 0:
            time.sleep(self.wait_time_between_chunks) 

class ProgressTracker:
    def __init__(self, total: int, desc: str = "Processing"):
        self.total = total
        self.desc = desc
        self.progress_bar = tqdm(total=total, desc=desc)
        self.failed = []
        self.successful = []
        
    def update(self, url: str, success: bool):
        """Update progress and track success/failure"""
        if success:
            self.successful.append(url)
        else:
            self.failed.append(url)
        self.progress_bar.update(1)
        
    def get_summary(self) -> dict:
        """Get summary of processing"""
        return {
            'total': self.total,
            'successful': len(self.successful),
            'failed': len(self.failed),
            'failed_urls': self.failed
        } 