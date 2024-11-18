# docs2llms

A Python tool to convert website documentation into LLM-friendly formats, following the llms.txt specification.

## Installation

Clone the repository and install locally:

```
# Clone the repository
git clone https://github.com/n4acc/docs2llms.git
cd docs2llms

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install the package
pip install -e .
```

## Usage

Basic usage:

```
docs2llms https://docs.example.com -o llms.txt
```

Save markdown files:

```
docs2llms https://docs.example.com -m docs/
```

Create a single markdown file with all documentation:

```
docs2llms https://docs.example.com --megadump complete_docs.md
```

### CLI Options

- `url`: The URL of the documentation to convert
- `-o, --output`: Output file path (default: llms.txt)
- `-m, --markdown-dir`: Directory to save individual markdown files
- `-md, --megadump`: Save all documentation to a single markdown file
- `-c, --config`: Path to config file
- `-v, --verbose`: Enable verbose output
- `-d, --debug`: Enable debug output
- `--include-related`: Include related pages section in markdown files (disabled by default)

### Examples

Convert documentation and save individual markdown files:

```
docs2llms https://docs.example.com -m docs/
```

Create a complete documentation file:

```
docs2llms https://docs.example.com --megadump complete_docs.md
```

Save both individual files and complete documentation:

```
docs2llms https://docs.example.com -m docs/ --megadump complete_docs.md
```

Include related pages in markdown files:

```
docs2llms https://docs.example.com -m docs/ --include-related
```

Enable verbose logging:

```
docs2llms https://docs.example.com -v
```

## Features

- Converts documentation to llms.txt format
- Optionally saves clean markdown versions of pages
- Creates a single markdown file with all documentation
- Configurable crawling depth and limits
- Support for JavaScript-rendered content
- Clean output without navigation elements and unwanted content

## Development

To set up for development:

```
# Clone the repository
git clone https://github.com/n4acc/docs2llms.git
cd docs2llms

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install in editable mode with development dependencies
pip install -e ".[dev]"
```