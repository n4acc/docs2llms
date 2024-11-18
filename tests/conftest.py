import pytest
from pathlib import Path
import yaml

@pytest.fixture
def test_config():
    config_path = Path(__file__).parent.parent / 'config' / 'default.yaml'
    with open(config_path) as f:
        return yaml.safe_load(f)

@pytest.fixture
def sample_html():
    return """
    <html>
        <head><title>Test Doc</title></head>
        <body>
            <h1>Documentation</h1>
            <p>This is a test documentation page.</p>
            <h2>Section 1</h2>
            <p>Section 1 content</p>
            <code>print("Hello World")</code>
        </body>
    </html>
    """ 