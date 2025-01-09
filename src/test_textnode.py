import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        node3 = TextNode("This is a text node", TextType.BOLD, "https://grahamhill.dev")
        node4 = TextNode("This is a text node", TextType.BOLD, "https://grahamhill.dev")
        self.assertEqual(node3, node4)
        node5 = TextNode("This is a text node", TextType.ITALIC, "https://grahamhill.dev")
        node6 = TextNode("This is a text node", TextType.ITALIC, "https://grahamhill.dev")
        self.assertEqual(node5, node6)
        node7 = TextNode("This is a text node", TextType.ITALIC, None)
        node8 = TextNode("This is a text node", TextType.ITALIC, None)
        self.assertEqual(node7, node8)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertIsNot(node, node2)
        node3 = TextNode("This is a text node", TextType.BOLD, None)
        node4 = TextNode("This is a text node", TextType.BOLD, "https://grahamhill.dev")
        self.assertIsNot(node3, node4)
        node5 = TextNode("This is a text node", TextType.ITALIC, "https://grahamhill.dev")
        node6 = TextNode("This is a text node", TextType.ITALIC, "https://boots.dev")
        self.assertIsNot(node5, node6)
        node7 = TextNode("This is a special text node", TextType.ITALIC, None)
        node8 = TextNode("This is a text node", TextType.ITALIC, None)
        self.assertIsNot(node7, node8)

    def test_is_same(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = node
        self.assertIs(node, node2)



if __name__ == "__main__":
    unittest.main()