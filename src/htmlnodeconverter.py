from src.htmlnode import LeafNode
from src.textnode import TextType, TextNode


def text_node_to_html_node(text_node):
    if not isinstance(text_node, TextNode):
        raise ValueError("text_node must be a TextNode")

    if text_node.text_type == TextType.TEXT:
        return LeafNode(tag=None, value=text_node.text)

    if text_node.text_type == TextType.BOLD:
        return LeafNode(tag="b", value=text_node.text)

    if text_node.text_type == TextType.ITALIC:
        return LeafNode(tag="i", value=text_node.text)

    if text_node.text_type == TextType.CODE:
        return LeafNode(tag="code", value=text_node.text)

    if text_node.text_type == TextType.LINK:
        return LeafNode(tag="a", value=text_node.text, props={"href": text_node.props.get("href", "")})

    if text_node.text_type == TextType.IMAGE:
        return LeafNode(
            tag="img",
            value="",
            props={"src": text_node.props.get("src", ""), "alt": text_node.props.get("alt", "")},
        )

    raise ValueError("Unsupported TextType")
