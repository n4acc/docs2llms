# docs2llms

> A tool to convert documentation websites into LLM-friendly formats. It generates both an llms.txt file (following the llms.txt specification) and markdown files for each documentation page.

⚠️ Warning: This is version 0.1 and is quite buggy. Use at your own risk.

This tool is designed to help:

- Create standardized llms.txt files from documentation websites
- Generate clean markdown versions of documentation for LLM context 
- Make documentation more accessible to AI assistants
- Support the llms.txt standard for better AI-documentation interaction

## Installation

```bash
pip install docs2llms
```

## Usage

Basic usage:

```bash
# Generate both llms.txt and markdown files
docs2llms https://docs.example.com/ -o llms.txt -m docs/

# Only generate llms.txt
docs2llms https://docs.example.com/ -o llms.txt

# Enable verbose logging
docs2llms https://docs.example.com/ -v

# Enable debug logging
docs2llms https://docs.example.com/ -d
```

### Options

- `-o, --output`: Output file path for llms.txt (default: llms.txt)
- `-m, --markdown-dir`: Directory to save markdown files 
- `-v, --verbose`: Enable verbose output
- `-d, --debug`: Enable debug output

### Current Limitations

- May miss some documentation pages due to JavaScript rendering
- Link extraction can be unreliable
- Memory usage may be high for large documentation sites
- Limited handling of complex navigation structures
- Some markdown formatting may be lost in conversion

### Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### License

MIT License

### Acknowledgments

This project is inspired by the llms.txt specification by Jeremy Howard.
