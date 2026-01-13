from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"    


def block_to_block_type(block):
    lines = block.split("\n")
    if block.startswith("#"):
        count = 0
        for char in block:
            if char == "#":
                count += 1
            else:
                break
        if 1 <= count <= 6 and len(block) > count and block[count] == " ":
            return BlockType.HEADING

    if len(lines) > 1 and block.startswith("```") and block.endswith("```"):
        return BlockType.CODE

    if all(line.startswith("> ") for line in lines):
        return BlockType.QUOTE

    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    if block.startswith("1. "):
        is_ordered = True
        for i in range(len(lines)):
            if not lines[i].startswith(f"{i + 1}. "):
                is_ordered = False
                break
        if is_ordered:
            return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
