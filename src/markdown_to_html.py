from block_markdown import markdown_to_blocks, block_to_block, BlockType
from inline_markdown import text_to_textnodes
from htmlnode import ParentNode, LeafNode
from textnode import text_node_to_html_node


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = []

    for block in blocks:
        block_type = block_to_block(block)
        block_node = block_to_html_node(block_type, block)
        nodes.append(block_node)

    parent = ParentNode("div", children=nodes)

    return parent


def block_to_html_node(block_type, block=None):
    match block_type:
        case BlockType.HEADING:
            return heading_to_html(block)

        case BlockType.CODE:
            return code_to_html(block)

        case BlockType.QUOTE:
            return quote_to_html(block)

        case BlockType.UNORDERED_LIST:
            return unordered_list_to_html(block)

        case BlockType.ORDERED_LIST:
            return ordered_list_to_html(block)

        case BlockType.PARAGRAPH:
            return paragraph_to_html(block)

        case _:
            raise ValueError(f"{block_type} is not a valid BlockType.")


def text_to_children(text):
    if not text:
        return
    html_nodes = []
    text_nodes = text_to_textnodes(text)
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        html_nodes.append(html_node)
    return html_nodes


def heading_to_html(block):
    i = 0
    while block[i] == "#":
        i += 1
    children_text = block[i:].strip()
    children_nodes = text_to_children(children_text)

    parent = ParentNode(f"h{i}", children=children_nodes)

    return parent


def code_to_html(block):
    code_text = block.replace("`", "").strip() + "\n"
    code_node = LeafNode("code", code_text)

    parent = ParentNode("pre", children=[code_node])

    return parent


def quote_to_html(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    parent = ParentNode("blockquote", children)
    return parent


def unordered_list_to_html(block):
    list_items_nodes = []
    list_items = block.split("\n")
    for list_item in list_items:
        if not list_item:
            continue
        list_item_text = list_item[2:]
        list_item_children = text_to_children(list_item_text)
        list_item_node = ParentNode("li", children=list_item_children)
        list_items_nodes.append(list_item_node)

    parent = ParentNode("ul", children=list_items_nodes)

    return parent


def ordered_list_to_html(block):
    list_items_nodes = []
    list_items = block.split("\n")
    for list_item in list_items:
        if not list_item:
            continue
        list_item_text = list_item.split(maxsplit=1)[1]
        list_item_children = text_to_children(list_item_text)
        list_item_node = ParentNode("li", children=list_item_children)
        list_items_nodes.append(list_item_node)

    parent = ParentNode("ol", children=list_items_nodes)

    return parent


def paragraph_to_html(block):
    children_text = block.replace("\n", " ").strip()
    children_nodes = text_to_children(children_text)

    parent = ParentNode("p", children=children_nodes)

    return parent
