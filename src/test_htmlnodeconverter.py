import unittest
from src.textnode import TextNode, TextType
from src.htmlnode import LeafNode
from src.htmlnodeconverter import text_node_to_html_node


class TestHTMLNodeConverter(unittest.TestCase):
    def test_node_eq(self):
        text_node = TextNode("Bold text", TextType.BOLD)
        expected_node = LeafNode(tag="b", value="Bold text")
        converted_node = text_node_to_html_node(text_node)
        self.assertEqual(converted_node, expected_node)

    def test_node_not_eq(self):
        text_node = TextNode("Italic text", TextType.ITALIC)
        expected_node = LeafNode(tag="b", value="Bold text")  # Intentionally wrong
        converted_node = text_node_to_html_node(text_node)
        self.assertNotEqual(converted_node, expected_node)

    def test_link_node(self):
        text_node = TextNode("Google", TextType.LINK, props={"href": "https://www.google.com"})
        expected_node = LeafNode(tag="a", value="Google", props={"href": "https://www.google.com"})
        converted_node = text_node_to_html_node(text_node)
        self.assertEqual(converted_node, expected_node)

    def test_image_node(self):
        text_node = TextNode("", TextType.IMAGE, props={"src": "image.png", "alt": "An image"})
        expected_node = LeafNode(tag="img", value="", props={"src": "image.png", "alt": "An image"})
        converted_node = text_node_to_html_node(text_node)
        self.assertEqual(converted_node, expected_node)


if __name__ == "__main__":
    unittest.main()
