

from html_node import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Tag is not optional, you must pass a tag argument.")
        if not self.children:
            raise ValueError("Children argument is not optional, you must pass a children argument.")
        children_html = ""
        for node in self.children:
            children_html += node.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
                
               
        