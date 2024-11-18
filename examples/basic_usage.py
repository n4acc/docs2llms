from docs2llms.converter import Docs2LLMs
from docs2llms.config import CrawlConfig
import asyncio

async def main():
    # Initialize converter with custom config
    config = CrawlConfig(
        max_pages=50,
        max_depth=2,
        pages_per_minute=10
    )
    
    converter = Docs2LLMs(config=config)
    
    # Convert documentation
    result = await converter.convert("https://docs.example.com")
    
    # Save output
    with open("output.txt", "w") as f:
        f.write(result)

if __name__ == "__main__":
    asyncio.run(main()) 