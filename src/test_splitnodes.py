import unittest

from src.splitnodes import split_nodes_link
from src.textnode import TextNode, TextType


class TestSplitNodes(unittest.TestCase):
    def test_split_nodes_link(self):
        node = TextNode(
            "Here is [a link](https://example.com) and [another](https://example.org)",
            TextType.TEXT,
        )
        expected = [
            TextNode("Here is ", TextType.TEXT),
            TextNode("a link", TextType.LINK, "https://example.com"),
            TextNode(" and ", TextType.TEXT),
            TextNode("another", TextType.LINK, "https://example.org"),
        ]
        self.assertEqual(split_nodes_link([node]), expected)

    def test_split_nodes_image(self):
        node = TextNode(
            "Here is ![alt](https://example.com/img.png) and ![another](https://example.org/img2.png)",
            TextType.TEXT,
        )
        expected = [
            TextNode("Here is ", TextType.TEXT),
            TextNode("alt", TextType.IMAGE, "https://example.com/img.png"),
            TextNode(" and ", TextType.TEXT),
            TextNode("another", TextType.IMAGE, "https://example.org/img2.png"),
        ]
        self.assertEqual(split_nodes_link([node]), expected)

    def test_split_nodes_mixed(self):
        node = TextNode(
            "Here is ![alt](https://example.com/img.png) and [a link](https://example.com)",
            TextType.TEXT,
        )
        expected_link = [
            TextNode("Here is ", TextType.TEXT),
            TextNode("alt", TextType.IMAGE, "https://example.com/img.png"),
            TextNode(" and ", TextType.TEXT),
            TextNode("a link", TextType.LINK, "https://example.com"),
        ]
        self.assertEqual(split_nodes_link([node]), expected_link)


if __name__ == "__main__":
    unittest.main()
