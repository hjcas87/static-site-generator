from src.helpers.split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link
from src.text_node import TextNode, TextType


def text_to_textnodes(text: str) -> list[TextNode]:
    nodes = [TextNode(text, TextType.TEXT)]
    
    converters = [
        (split_nodes_image, None, None),
        (split_nodes_link, None, None),
        (split_nodes_delimiter, "**", TextType.BOLD),
        (split_nodes_delimiter, "_", TextType.ITALIC),
        (split_nodes_delimiter, "`", TextType.CODE),
    ]

    for func, delim, t_type in converters:
        if delim:
            nodes = func(nodes, delim, t_type)
        else:
            nodes = func(nodes)
            
    return nodes
