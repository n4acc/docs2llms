from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from .spider import DocsSpider
import tempfile
import json
from pathlib import Path
import time

class DocFetcher:
    def __init__(self, base_url: str, doc_type: str = 'auto', max_depth: int = 3):
        self.base_url = base_url
        self.doc_type = doc_type
        self.max_depth = max_depth
        
    def fetch(self) -> dict:
        """
        Fetch and parse documentation structure using Scrapy
        """
        # Create temporary file for storing results
        with tempfile.NamedTemporaryFile(mode='w+', delete=False) as f:
            temp_path = f.name
        
        # Configure Scrapy settings
        settings = get_project_settings()
        settings.update({
            'USER_AGENT': 'docs2llms (+https://github.com/yourusername/docs2llms)',
            'ROBOTSTXT_OBEY': True,
            'CONCURRENT_REQUESTS': 16,
            'DOWNLOAD_DELAY': 1,
            'COOKIES_ENABLED': False,
            'FEED_FORMAT': 'jsonlines',
            'FEED_URI': f'file://{temp_path}',
            'LOG_LEVEL': 'ERROR'
        })
        
        # Run the spider
        process = CrawlerProcess(settings)
        process.crawl(
            DocsSpider,
            url=self.base_url,
            doc_type=self.doc_type,
            max_depth=self.max_depth
        )
        process.start()
        
        # Read results
        structure = None
        try:
            with open(temp_path) as f:
                for line in f:
                    data = json.loads(line)
                    if data['url'] == self.base_url:
                        structure = data
                        break
        finally:
            Path(temp_path).unlink()
        
        return structure

class RetryHandler:
    def __init__(self, max_retries: int = 3, retry_delay: int = 5):
        self.max_retries = max_retries
        self.retry_delay = retry_delay
        self.failed_urls = []
    
    async def with_retry(self, func, *args, **kwargs):
        """Execute function with retry logic"""
        for attempt in range(self.max_retries):
            try:
                return await func(*args, **kwargs)
            except Exception as e:
                if attempt == self.max_retries - 1:
                    self.failed_urls.append(kwargs.get('url', 'unknown'))
                    raise
                time.sleep(self.retry_delay)