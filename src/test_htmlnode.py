import unittest

from htmlnode import HtmlNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = HtmlNode("p", "This is some text for a paragraph",
                        props={"href": "https://www.google.com", "target": "_blank"})
        node2 = HtmlNode("p", "This is some text for a paragraph",
                        props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node, node2)
        node3 = HtmlNode("a", "This is some text for a link")
        node4 = HtmlNode("a", "This is some text for a link")
        self.assertEqual(node3, node4)
        node5 = HtmlNode("h1", "This is some text for a heading (h1)",
                         [node, node2, node3, node4],
                         {"href": "https://www.google.com", "target": "_blank"})
        node6 = HtmlNode("h1", "This is some text for a heading (h1)",
                         [node, node2, node3, node4],
                         {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node5, node6)
        node7 = HtmlNode(tag= "This is some text for a image")
        node8 = HtmlNode(tag= "This is some text for a image")
        self.assertEqual(node7, node8)

    def test_not_eq(self):
        node = HtmlNode("h1", "This is some text for a heading (h1)",
                         [],
                         {"href": "https://www.google.com", "target": "_blank"})
        node2 = HtmlNode("This is a text node", "This is some text for a image")
        self.assertIsNot(node, node2)


    def test_is_same(self):
        node = HtmlNode("This is a sparse HTML node")
        node2 = node
        self.assertIs(node, node2)
        node3 = HtmlNode("This is a sparse HTML node", "a")
        node4 = node3
        self.assertIs(node3, node4)

    def test_no_props(self):
        # Test case where props is not provided.
        node = HtmlNode(tag="p", value="This is a paragraph.")
        self.assertEqual(node.props_to_html(), "")  # No attributes should be present.

    def test_with_props(self):
        # Test case where props is provided.
        node = HtmlNode(tag="a", value="Click Here", props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), 'href="https://www.google.com" target="_blank"')

    def test_children(self):
        # Test case where the node has children
        child_node = HtmlNode(tag="span", value="This is a span.")
        parent_node = HtmlNode(tag="div", children=[child_node], props={"class": "container"})
        self.assertEqual(len(parent_node.children), 1)  # The parent node has one child.
        self.assertEqual(parent_node.props_to_html(), 'class="container"')


if __name__ == "__main__":
    unittest.main()