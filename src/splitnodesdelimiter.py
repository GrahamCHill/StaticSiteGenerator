from src.textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    """
    Splits text nodes in old_nodes based on the given delimiter and assigns the specified text_type
    to the delimited segments.

    :param old_nodes: List of TextNode objects to be processed.
    :param delimiter: String used as the delimiter for splitting.
    :param text_type: TextType for delimited segments.
    :return: New list of TextNode objects with delimited segments processed.
    """
    new_nodes = []

    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            parts = node.text.split(delimiter)
            for i, part in enumerate(parts):
                # Only add non-empty text or delimited parts
                if part:
                    current_type = text_type if i % 2 == 1 else TextType.TEXT
                    new_nodes.append(TextNode(part, current_type))
        else:
            new_nodes.append(node)

    return new_nodes

