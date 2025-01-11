from src.extract_markdownimage import extract_markdown_images
from src.textnode import TextNode, TextType
import re


def split_nodes_link(old_nodes):
    """
    Splits text nodes in old_nodes into separate nodes based on markdown links and images.

    :param old_nodes: List of TextNode objects to be processed.
    :return: New list of TextNode objects with links processed.
    """
    pattern = re.compile(r'(!?\[.*?]\(.*?\))')  # Matches both images and links.
    return __split_nodes(old_nodes, pattern)



def __split_nodes(old_nodes, regex_pattern):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            text = node.text
            last_index = 0
            for match in regex_pattern.finditer(text):
                # Add text before the match
                if match.start() > last_index:
                    new_nodes.append(TextNode(text[last_index:match.start()], TextType.TEXT))

                # Extract the matched markdown
                matched_text = match.group(0)
                if matched_text.startswith("!["):  # Handle image markdown
                    alt, url = re.match(r'!\[(.*?)\]\((.*?)\)', matched_text).groups()
                    new_nodes.append(TextNode(alt, TextType.IMAGE, url))
                elif matched_text.startswith("["):  # Handle link markdown
                    link_text, url = re.match(r'\[(.*?)\]\((.*?)\)', matched_text).groups()
                    new_nodes.append(TextNode(link_text, TextType.LINK, url))

                last_index = match.end()

            # Add remaining text after the last match
            if last_index < len(text):
                new_nodes.append(TextNode(text[last_index:], TextType.TEXT))
        else:
            new_nodes.append(node)
    return new_nodes
