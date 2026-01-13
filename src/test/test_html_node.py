import unittest

from src.html_node import HTMLNode
from src.leaf_node import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_basic(self):
        node = HTMLNode(props={"href": "https://www.google.com"})
        expected = ' href="https://www.google.com"'
        self.assertEqual(node.props_to_html(), expected)

    def test_props_to_html_multiple(self):
        node = HTMLNode(props={
            "href": "https://www.google.com", 
            "target": "_blank",
        })
        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)

    def test_props_to_html_none(self):
        node = HTMLNode(props=None)
        self.assertEqual(node.props_to_html(), "")
        
        node2 = HTMLNode(props={})
        self.assertEqual(node2.props_to_html(), "")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

if __name__ == "__main__":
    unittest.main()