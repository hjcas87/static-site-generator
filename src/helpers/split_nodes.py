from src.helpers.extract_markdown import extract_markdown_images, extract_markdown_links
from src.text_node import TextNode, TextType


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter, text_type: TextType):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        new_node = node.text.split(delimiter)
        if len(new_node) % 2 == 0:
            raise Exception(f"Invalid Markdown: missing closing delimiter {delimiter}")
        for i in range(len(new_node)):
            if new_node[i] == "":
                continue
            if i == 0 or i % 2 == 0:
                new_nodes.append(TextNode(new_node[i], TextType.TEXT))
            else:
                new_nodes.append(TextNode(new_node[i], text_type))
    return new_nodes


def split_nodes_image(old_nodes: list[TextNode]):
    new_nodes = []
    for n in old_nodes:
        if n.text_type != TextType.TEXT:
            new_nodes.append(n)
            continue
        parts = extract_markdown_images(n.text)
        if not parts:
            new_nodes.append(n)
            continue
        actual_text = n.text
        for i in range(len(parts)):
            section = actual_text.split(f"![{parts[i][0]}]({parts[i][1]})", 1)
            if len(section) != 2:
                raise Exception(f"Invalid Markdown")
            if section[0]:
                new_nodes.append(TextNode(section[0], TextType.TEXT))
            new_nodes.append(TextNode(parts[i][0], TextType.IMAGE, parts[i][1]))
            actual_text = section[1]
        if actual_text:
            new_nodes.append(TextNode(actual_text, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes: list[TextNode]):
    new_nodes = []
    for n in old_nodes:
        if n.text_type != TextType.TEXT:
            new_nodes.append(n)
            continue
        parts = extract_markdown_links(n.text)
        if not parts:
            new_nodes.append(n)
            continue
        actual_text = n.text
        for i in range(len(parts)):
            section = actual_text.split(f"[{parts[i][0]}]({parts[i][1]})", 1)
            if len(section) != 2:
                raise Exception(f"Invalid Markdown")
            if section[0]:
                new_nodes.append(TextNode(section[0], TextType.TEXT))
            new_nodes.append(TextNode(parts[i][0], TextType.LINK, parts[i][1]))
            actual_text = section[1]
        if actual_text:
            new_nodes.append(TextNode(actual_text, TextType.TEXT))
    return new_nodes
