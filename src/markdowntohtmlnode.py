from src.blocktoblock import block_to_block_type
from src.htmlnode import HtmlNode
from src.markdowntoblocks import markdown_to_blocks
from src.textnode import TextType
from src.texttotextnode import text_to_textnodes


def markdown_to_html_node(markdown):
    """
    Converts a Markdown document into a single parent HTMLNode with nested children.

    :param markdown: Full markdown document as a string.
    :return: A single parent HTMLNode containing nested children representing the document.
    """
    # Split markdown into blocks
    blocks = markdown_to_blocks(markdown)

    # Create a parent HTMLNode
    parent_node = HtmlNode("div", {})

    # Process each block
    for block in blocks:
        block_type = block_to_block_type(block)
        children = text_to_children(block)  # Shared helper for inline markdown parsing

        if block_type == "heading":
            level = block.count("#")
            content = block.lstrip("# ").strip()
            heading_node = HtmlNode(f"h{level}", {}, text_to_children(content))
            parent_node.children.append(heading_node)
        elif block_type == "code":
            code_content = block.strip("`").strip()
            code_node = HtmlNode("pre", {},
                                 [HtmlNode("code", {},
                                           [HtmlNode("text", {"text": code_content})])])
            parent_node.children.append(code_node)
        elif block_type == "quote":
            quote_node = HtmlNode("blockquote", {}, children)
            parent_node.children.append(quote_node)
        elif block_type == "unordered_list":
            ul_node = HtmlNode("ul", {})
            for line in block.splitlines():
                item_text = line.lstrip("-* ").strip()
                li_node = HtmlNode("li", {}, text_to_children(item_text))
                ul_node.children.append(li_node)
            parent_node.children.append(ul_node)
        elif block_type == "ordered_list":
            ol_node = HtmlNode("ol", {})
            for line in block.splitlines():
                item_text = line.split(". ", 1)[-1].strip()
                li_node = HtmlNode("li", {}, text_to_children(item_text))
                ol_node.children.append(li_node)
            parent_node.children.append(ol_node)
        else:  # Paragraph
            paragraph_node = HtmlNode("p", {}, children)
            parent_node.children.append(paragraph_node)

    return parent_node


def text_to_children(text):
    """
    Converts inline Markdown text to HTMLNode children.

    :param text: Inline markdown text as a string.
    :return: List of HTMLNode objects representing the parsed inline content.
    """
    text_nodes = text_to_textnodes(text)
    html_nodes = []

    for node in text_nodes:
        print(f"Processing node: text={node.text}, type={node.text_type}, props={node.props}")

        if node.text_type is TextType.BOLD:
            # Create a <strong> node for bold text
            html_nodes.append(HtmlNode("strong", {}, [HtmlNode("text", {"text": node.text})]))
        elif node.text_type is TextType.ITALIC:
            # Create an <em> node for italic text
            html_nodes.append(HtmlNode("em", {}, [HtmlNode("text", {"text": node.text})]))
        elif node.text_type is TextType.CODE:
            # Create a <code> node for inline code
            html_nodes.append(HtmlNode("code", {}, [HtmlNode("text", {"text": node.text})]))
        elif node.text_type is TextType.LINK:
            # Create an <a> node for links
            html_nodes.append(HtmlNode("a", {"href": node.props}, [HtmlNode("text", {"text": node.text})]))
        elif node.text_type is TextType.IMAGE:
            # Create an <img> node for images
            html_nodes.append(HtmlNode("img", {"src": node.props, "alt": node.text}))
        else:  # Default to plain text
            html_nodes.append(HtmlNode("text", {"text": node.text}))

    print("\nFinal HTML nodes:")
    for node in html_nodes:
        print(f"tag: {node.tag}, value: {node.value}, children: {node.children}")
    return html_nodes
