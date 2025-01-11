import re

def extract_markdown_images(text):
    """
    Extracts markdown image alt text and URLs from the input text.

    :param text: String containing markdown text.
    :return: List of tuples containing alt text and image URLs.
    """
    pattern = r"!\[(.*?)\]\((.*?)\)"
    return re.findall(pattern, text)

def extract_markdown_links(text):
    """
    Extracts markdown link anchor text and URLs from the input text.

    :param text: String containing markdown text.
    :return: List of tuples containing anchor text and link URLs.
    """
    pattern = r"\[(.*?)\]\((.*?)\)"
    return re.findall(pattern, text)
