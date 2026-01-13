from src.helpers.text_node_to_html_node import text_node_to_html_node
from src.helpers.text_to_textnodes import text_to_textnodes
from src.helpers.block_to_block_type import BlockType, block_to_block_type
from src.helpers.markdown_to_blocks import markdown_to_blocks
from src.html_node import HTMLNode
from src.parent_node import ParentNode
from src.text_node import TextNode, TextType


def markdown_to_html_node(markdown: str):
    parent = ParentNode("div", [])

    blocks = markdown_to_blocks(markdown)
    new_nodes = []

    for block in blocks:
        block_type = block_to_block_type(block)
        children = []
        if block_type == BlockType.PARAGRAPH:
            clean_block = " ".join(block.splitlines())
            text_nodes = text_to_textnodes(clean_block)
            children = []
            for node in text_nodes:
                children.append(text_node_to_html_node(node))
            p = ParentNode("p", children)
            new_nodes.append(p)
        elif block_type == BlockType.HEADING:
            heading = block.split(" ", 1)
            head = heading_choice(heading[0])
            text_nodes = text_to_textnodes(heading[1])
            for node in text_nodes:
                children.append(text_node_to_html_node(node))
            h = ParentNode(head, children)
            new_nodes.append(h)
        elif block_type == BlockType.CODE:
            text = block.split("```")
            code_text = text[1].lstrip("\n")
            tn = TextNode(code_text, TextType.TEXT)
            child = text_node_to_html_node(tn)
            code_node = ParentNode("code", [child])
            pre_node = ParentNode("pre", [code_node])
            new_nodes.append(pre_node)
        elif block_type == BlockType.QUOTE:
            lines = block.split("\n")
            clean_lines = []
            for line in lines:
                if line.strip() == "":
                    continue
                stripped = line.lstrip()
                if stripped.startswith(">"):
                    stripped = stripped[1:]
                    if stripped.startswith(" "):
                        stripped = stripped[1:]
                clean_lines.append(stripped)

            text_clean = " ".join(clean_lines)
            text_nodes = text_to_textnodes(text_clean)
            children = []
            for node in text_nodes:
                children.append(text_node_to_html_node(node))

            b = ParentNode("blockquote", children)
            new_nodes.append(b)
        elif block_type == BlockType.UNORDERED_LIST:
            lines = block.split("\n")
            li_nodes = []

            for line in lines:
                if line.strip() == "":
                    continue
                if line.startswith("- "):
                    item_text = line[2:]
                else:
                    item_text = line

                text_nodes = text_to_textnodes(item_text)

                li_children = []
                for node in text_nodes:
                    li_children.append(text_node_to_html_node(node))

                li_node = ParentNode("li", li_children)
                li_nodes.append(li_node)

            ul = ParentNode("ul", li_nodes)
            new_nodes.append(ul)
        elif block_type == BlockType.ORDERED_LIST:
            lines = block.split("\n")
            li_nodes = []

            for line in lines:
                if line.strip() == "":
                    continue

                if ". " in line:
                    _, item_text = line.split(". ", 1)
                else:
                    item_text = line

                text_nodes = text_to_textnodes(item_text)
                li_children = []
                for node in text_nodes:
                    li_children.append(text_node_to_html_node(node))

                li_node = ParentNode("li", li_children)
                li_nodes.append(li_node)

            ol = ParentNode("ol", li_nodes)
            new_nodes.append(ol)
    parent.children = new_nodes
    return parent


def heading_choice(text: str):

    headings = {
        "#": "h1",
        "##": "h2",
        "###": "h3",
        "####": "h4",
        "#####": "h5",
        "######": "h6",
    }

    return headings[text]
