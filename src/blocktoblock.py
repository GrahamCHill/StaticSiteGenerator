import re

def block_to_block_type(block):
    """
    Identifies the type of a Markdown block.

    :param block: A single block of Markdown text (stripped of leading/trailing whitespace).
    :return: A string representing the type of the block ('heading', 'code', 'quote',
             'unordered_list', 'ordered_list', or 'paragraph').
    """
    # Handle empty block
    if not block.strip():
        return "paragraph"

    # Check for Heading
    if re.match(r'^#{1,6} ', block):
        return "heading"

    # Check for Code Block
    if block.startswith("```") and block.endswith("```"):
        return "code"

    # Check for Quote Block
    if all(line.startswith(">") for line in block.splitlines()):
        return "quote"

    # Check for Unordered List Block
    if all(re.match(r'^[-*] ', line) for line in block.splitlines()):
        return "unordered_list"

    # Check for Ordered List Block
    ordered_list_pattern = r'^(\d+)\. '
    lines = block.splitlines()
    if all(re.match(ordered_list_pattern, line) for line in lines):
        # Verify ordered numbering starts at 1 and increments correctly
        numbers = [int(re.match(ordered_list_pattern, line).group(1)) for line in lines]
        if numbers == list(range(1, len(numbers) + 1)):
            return "ordered_list"

    # Default to Paragraph
    return "paragraph"
