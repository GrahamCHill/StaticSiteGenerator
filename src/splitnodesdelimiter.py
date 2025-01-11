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
                # Handle empty parts between delimiters
                if i % 2 == 1:  # Delimited part
                    new_nodes.append(TextNode(part, text_type))
                elif part:  # Non-empty text outside delimiters
                    new_nodes.append(TextNode(part, TextType.TEXT))
        else:
            # Non-text nodes are directly appended
            new_nodes.append(node)

    return new_nodes


