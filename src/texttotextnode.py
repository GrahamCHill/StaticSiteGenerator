from src.splitnodes import split_nodes_link, __split_nodes
from src.textnode import TextNode, TextType
import re


def text_to_textnodes(text):
    """
    Converts a text string into a list of TextNode objects based on markdown parsing.

    :param text: Input text string containing markdown for links, images, etc.
    :return: List of TextNode objects with appropriate types and content.
    """

    # Helper function for splitting text into nodes based on regex and TextType
    def process_nodes(nodes_input, pattern, text_type, strip_chars=0):
        new_nodes = []
        for node in nodes_input:
            if node.text_type == TextType.TEXT:
                text_input = node.text
                last_index = 0
                for match in pattern.finditer(text_input):
                    # Add preceding text as a text node
                    if match.start() > last_index:
                        new_nodes.append(TextNode(text_input[last_index:match.start()], TextType.TEXT))

                    # Create a new node based on the match
                    matched_text = match.group(0)
                    new_text = matched_text[strip_chars:-strip_chars] if strip_chars else matched_text
                    new_nodes.append(TextNode(new_text, text_type))

                    last_index = match.end()

                # Add remaining text as a text node
                if last_index < len(text_input):
                    new_nodes.append(TextNode(text_input[last_index:], TextType.TEXT))
            else:
                new_nodes.append(node)
        return new_nodes

    # Initial node containing the full text
    nodes = [TextNode(text, TextType.TEXT)]

    # Process for links and images (already handled by split_nodes_link)
    nodes = split_nodes_link(nodes)

    # Process for bold (**text**)
    bold_pattern = re.compile(r"\*\*(.*?)\*\*")
    nodes = process_nodes(nodes, bold_pattern, TextType.BOLD, strip_chars=2)

    # Process for italic (*text*)
    italic_pattern = re.compile(r"\*(.*?)\*")
    nodes = process_nodes(nodes, italic_pattern, TextType.ITALIC, strip_chars=1)

    # Process for inline code (`text`)
    code_pattern = re.compile(r"`(.*?)`")
    nodes = process_nodes(nodes, code_pattern, TextType.CODE, strip_chars=1)

    return nodes
