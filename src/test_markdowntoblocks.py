import unittest
from src.markdowntoblocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_heading_and_paragraph(self):
        markdown = "# Heading\n\nThis is a paragraph."
        expected = [
            "# Heading",
            "This is a paragraph."
        ]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_paragraph_with_list(self):
        markdown = (
            "This is a paragraph.\n\n"
            "* List item 1\n* List item 2\n* List item 3"
        )
        expected = [
            "This is a paragraph.",
            "* List item 1\n* List item 2\n* List item 3"
        ]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_multiple_empty_lines(self):
        markdown = (
            "# Heading\n\n\n\n"
            "This is a paragraph.\n\n"
            "* List item"
        )
        expected = [
            "# Heading",
            "This is a paragraph.",
            "* List item"
        ]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_trailing_and_leading_whitespace(self):
        markdown = "  # Heading\n\n   Paragraph with spaces.  \n\n"
        expected = [
            "# Heading",
            "Paragraph with spaces."
        ]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_empty_markdown(self):
        markdown = ""
        expected = []
        self.assertEqual(markdown_to_blocks(markdown), expected)
