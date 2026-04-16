from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block(block):
    pattern = r"^\#{1,6} .+"
    if re.match(pattern, block):
        return BlockType.HEADING

    pattern = r"^\`{3}\n[\s\S]*\`{3}$"
    if re.match(pattern, block):
        return BlockType.CODE

    if block[0] == ">":
        block_lines = block.split("\n")
        type_quote = True
        for line in block_lines:
            if not (line == "" or line[0] == ">"):
                type_quote = False
                break
        if type_quote:
            return BlockType.QUOTE

    if block[0] == "-":
        block_lines = block.split("\n")
        type_ul = True
        for line in block_lines:
            if not (line == "" or line[0] == "-"):
                type_ul = False
                break
        if type_ul:
            return BlockType.UNORDERED_LIST

    if block[0:2] == "1.":
        block_lines = block.split("\n")
        index = 1
        type_ol = True
        for line in block_lines:
            if line[0:2] == f"{index}.":
                index += 1
            elif line != "":
                type_ol = False
                break
        if type_ol:
            return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    cleaned_blocks = []
    for block in blocks:
        cleaned_block = block.strip()
        if cleaned_block:
            cleaned_blocks.append(cleaned_block)

    return cleaned_blocks
