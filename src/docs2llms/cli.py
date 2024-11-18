import click
from .core.converter import Docs2LLMs
from .utils.config import CrawlConfig
import yaml
import asyncio
import logging
from playwright.async_api import async_playwright

@click.command()
@click.argument('url')
@click.option('--output', '-o', default='llms.txt', help='Output file path')
@click.option('--markdown-dir', '-m', help='Directory to save markdown files')
@click.option('--config', '-c', help='Path to config file')
@click.option('--verbose', '-v', is_flag=True, help='Enable verbose output')
@click.option('--debug', '-d', is_flag=True, help='Enable debug output')
@click.option('--include-related', is_flag=True, help='Include related pages section in markdown files')
def main(url: str, output: str, markdown_dir: str, config: str, verbose: bool, debug: bool, include_related: bool):
    """Main CLI entry point"""
    # Setup logging
    log_level = logging.DEBUG if debug else (logging.INFO if verbose else logging.WARNING)
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    
    logger = logging.getLogger(__name__)
    logger.info(f"Starting conversion of {url}")
    
    # Create config
    crawler_config = CrawlConfig(
        max_pages=100,
        max_depth=3,
        debug=debug
    )
    
    # Create converter and run
    converter = Docs2LLMs(config=crawler_config)
    
    async def run_crawler():
        async with async_playwright() as p:
            browser = await p.chromium.launch()
            context = await browser.new_context()
            try:
                return await converter._crawl_pages(context, url, 
                                                 save_markdown=bool(markdown_dir),
                                                 markdown_dir=markdown_dir,
                                                 include_related=include_related)
            finally:
                await context.close()
                await browser.close()
    
    # Run conversion - only crawl once and use results for both outputs
    pages = asyncio.run(run_crawler())
    
    # Generate markdown files if requested
    if markdown_dir:
        converter.save_markdown_files(pages, markdown_dir, include_related)
    
    # Generate llms.txt
    result = converter._generate_llms_txt(pages)
    with open(output, 'w') as f:
        f.write(result)
    
    logger.info(f"Generated {output}")

if __name__ == '__main__':
    main() 