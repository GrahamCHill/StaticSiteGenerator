import unittest
from src.markdowntohtmlnode import markdown_to_html_node
from src.htmlnode import HtmlNode

class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_simple_paragraph(self):
        markdown = "This is a simple paragraph."
        result = markdown_to_html_node(markdown)
        expected = HtmlNode("div", {}, [
            HtmlNode("p", {}, [HtmlNode("text", {"text": "This is a simple paragraph."})])
        ])
        self.assertEqual(result, expected)

    def test_heading(self):
        markdown = "# Heading 1"
        result = markdown_to_html_node(markdown)
        expected = HtmlNode("div", {}, [
            HtmlNode("h1", {}, [HtmlNode("text", {"text": "Heading 1"})])
        ])
        self.assertEqual(result, expected)

    def test_code_block(self):
        markdown = "```\nCode block\n```"
        result = markdown_to_html_node(markdown)
        expected = HtmlNode("div", {}, [
            HtmlNode("pre", {}, [
                HtmlNode("code", {}, [HtmlNode("text", {"text": "Code block"})])
            ])
        ])
        self.assertEqual(result, expected)

    def test_unordered_list(self):
        markdown = "* Item 1\n* Item 2\n* Item 3"
        result = markdown_to_html_node(markdown)
        expected = HtmlNode("div", {}, [
            HtmlNode("ul", {}, [
                HtmlNode("li", {}, [HtmlNode("text", {"text": "Item 1"})]),
                HtmlNode("li", {}, [HtmlNode("text", {"text": "Item 2"})]),
                HtmlNode("li", {}, [HtmlNode("text", {"text": "Item 3"})])
            ])
        ])
        self.assertEqual(result, expected)

    def test_combined_markdown(self):
        markdown = "# Heading\n\nThis is a **bold** paragraph."
        result = markdown_to_html_node(markdown)
        expected = HtmlNode("div", {}, [
            HtmlNode("h1", {}, [HtmlNode("text", {"text": "Heading"})]),
            HtmlNode("p", {}, [
                HtmlNode("text", {"text": "This is a "}),
                HtmlNode("strong", {}, [HtmlNode("text", {"text": "bold"})]),
                HtmlNode("text", {"text": " paragraph."})
            ])
        ])
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
