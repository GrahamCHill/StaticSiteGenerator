import re


def markdown_to_blocks(markdown):
    """
    Splits a raw Markdown string into blocks of content.

    :param markdown: Raw Markdown string representing a document.
    :return: List of block strings.
    """
    # Split the Markdown content into blocks based on empty lines.
    raw_blocks = re.split(r'\n\s*\n', markdown)

    # Clean up each block by stripping leading/trailing whitespace.
    cleaned_blocks = [block.strip() for block in raw_blocks]

    # Filter out any empty blocks.
    non_empty_blocks = [block for block in cleaned_blocks if block]

    return non_empty_blocks
