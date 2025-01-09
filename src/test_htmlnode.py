import unittest

from htmlnode import HtmlNode, LeafNode, ParentNode


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

class TestLeafNode(unittest.TestCase):
    def test_leaf_node_raw_text(self):
        node = LeafNode(None, "Raw text")
        self.assertEqual(node.to_html(), "Raw text")

    def test_leaf_node_with_tag(self):
        node = LeafNode("p", "This is a paragraph.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph.</p>")

    def test_leaf_node_with_tag_and_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_node_missing_value(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None)

    def test_leaf_node_missing_tag_and_value(self):
        with self.assertRaises(ValueError):
            LeafNode(None, None)


class TestParentNode(unittest.TestCase):
    def test_parent_node_with_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_nested_parent_nodes(self):
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "p",
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                    ],
                ),
                ParentNode(
                    "p",
                    [
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text"),
                    ],
                ),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<div><p><b>Bold text</b>Normal text</p><p><i>italic text</i>Normal text</p></div>",
        )

    def test_parent_node_without_children(self):
        with self.assertRaises(ValueError):
            ParentNode("p", [])

    def test_parent_node_missing_tag(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("b", "Bold text")])

    def test_parent_node_with_props(self):
        node = ParentNode(
            "div",
            [LeafNode("span", "Hello, world!")],
            {"class": "container", "id": "main"},
        )
        self.assertEqual(
            node.to_html(),
            '<div class="container" id="main"><span>Hello, world!</span></div>',
        )

    def test_parent_node_with_empty_props(self):
        node = ParentNode(
            "ul",
            [
                LeafNode("li", "Item 1"),
                LeafNode("li", "Item 2"),
                LeafNode("li", "Item 3"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul>",
        )




if __name__ == "__main__":
    unittest.main()