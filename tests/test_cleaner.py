import pytest
from docs2llms.cleaner import ContentCleaner

def test_content_cleaner():
    cleaner = ContentCleaner()
    html_content = """
    <div>
        <h1>Test</h1>
        <p>Some text</p>
        <pre><code>print("test")</code></pre>
    </div>
    """
    cleaned = cleaner.clean(html_content)
    assert "Test" in cleaned
    assert "```python" in cleaned
    assert "print(" in cleaned 