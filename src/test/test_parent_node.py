import unittest
from src.parent_node import ParentNode
from src.leaf_node import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("b", "Bold text")
        node = ParentNode("p", [child_node, LeafNode(None, "Normal text")])
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text</p>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        expected = "<div><span><b>grandchild</b></span></div>"
        self.assertEqual(parent_node.to_html(), expected)

    def test_to_html_with_props(self):
        node = ParentNode(
            "div", 
            [LeafNode("b", "Bold")], 
            {"class": "container", "id": "main"}
        )
        self.assertEqual(
            node.to_html(), 
            '<div class="container" id="main"><b>Bold</b></div>'
        )

if __name__ == "__main__":
    unittest.main()