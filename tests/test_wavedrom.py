import unittest

from markdown import markdown

NO_MATCH_MARKDOWN = """
# Headline
"""

NO_MATCH_HTML = """
<h1>Headline</h1>
""".strip()

SIMPLE_DIAGRAM_MARKDOWN = """
# Headline

wavedrom (  
content
)
"""

SIMPLE_DIAGRAM_HTML = """
<h1>Headline</h1>
<script type="WaveDrom">content</script>
""".strip()

MULTI_DIAGRAM_MARKDOWN = """
# Headline 1

wavedrom (
content 1
)

## Headline 2

wavedrom (
    line 1
    line 2
)
"""

MULTI_DIAGRAM_HTML = """
<h1>Headline 1</h1>
<script type="WaveDrom">content 1</script>
<h2>Headline 2</h2>
<script type="WaveDrom">line 1
line 2</script>
""".strip()


INDENTED_DIAGRAM_MARKDOWN = """
# Headline
  - Bullet 1
  - Bullet 2

    wavedrom (
        content
    )

  - Bullet 3
"""

INDENTED_DIAGRAM_HTML = """
<h1>Headline</h1>
<ul>
<li>Bullet 1</li>
<li>
<p>Bullet 2</p>
<script type="WaveDrom">content</script>
</li>
<li>
<p>Bullet 3</p>
</li>
</ul>
""".strip()


class WavedromTest(unittest.TestCase):
    def test_empty_string(self):
        result = markdown("", extensions=["markdown_wavedrom"])
        self.assertEqual("", result)

    def test_no_match(self):
        result = markdown(NO_MATCH_MARKDOWN, extensions=["markdown_wavedrom"])
        self.assertEqual(NO_MATCH_HTML, result)

    def test_simple_diagram(self):
        result = markdown(SIMPLE_DIAGRAM_MARKDOWN, extensions=["markdown_wavedrom"])
        self.assertEqual(SIMPLE_DIAGRAM_HTML, result)

    def test_multi_diagram(self):
        result = markdown(MULTI_DIAGRAM_MARKDOWN, extensions=["markdown_wavedrom"])
        self.assertEqual(MULTI_DIAGRAM_HTML, result)

    def test_indented_diagram(self):
        result = markdown(INDENTED_DIAGRAM_MARKDOWN, extensions=["markdown_wavedrom"])
        self.assertEqual(INDENTED_DIAGRAM_HTML, result)
