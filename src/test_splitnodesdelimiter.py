import unittest
from src.textnode import TextNode, TextType
from splitnodesdelimiter import *


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_single_delimiter(self):
        node = TextNode("This is `code` text", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" text", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_multiple_delimiters(self):
        node = TextNode("Text with `code` and more `code` blocks", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("Text with ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" and more ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" blocks", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_no_delimiters(self):
        node = TextNode("No special formatting here", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [node]  # No change
        self.assertEqual(result, expected)

    def test_adjacent_delimiters(self):
        node = TextNode("`code1``code2`", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("", TextType.TEXT),  # Leading empty text
            TextNode("code1", TextType.CODE),
            TextNode("", TextType.TEXT),  # Empty between adjacent delimiters
            TextNode("code2", TextType.CODE),
            TextNode("", TextType.TEXT),  # Trailing empty text
        ]
        self.assertEqual(result, expected)

    def test_other_text_types_untouched(self):
        node = TextNode("Bold text", TextType.BOLD)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [node]  # Non-text nodes are unchanged
        self.assertEqual(result, expected)

    def test_combination_of_types(self):
        nodes = [
            TextNode("This is `code`", TextType.TEXT),
            TextNode(" and ", TextType.BOLD),
            TextNode("*italic* text", TextType.TEXT),
        ]
        result = split_nodes_delimiter(nodes, "`", TextType.CODE)
        result = split_nodes_delimiter(result, "*", TextType.ITALIC)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode("", TextType.TEXT),  # Trailing empty text after code delimiter
            TextNode(" and ", TextType.BOLD),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_italic_delimiter(self):
        node = TextNode("Text with *italic* style", TextType.TEXT)
        result = split_nodes_delimiter([node], "*", TextType.ITALIC)
        expected = [
            TextNode("Text with ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" style", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_mixed_delimiters(self):
        nodes = [
            TextNode("Text with *italic* and `code` blocks", TextType.TEXT)
        ]
        result = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
        result = split_nodes_delimiter(result, "`", TextType.CODE)
        expected = [
            TextNode("Text with ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" and ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" blocks", TextType.TEXT),
        ]
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
