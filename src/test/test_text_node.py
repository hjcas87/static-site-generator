import unittest

from src.helpers.text_node_to_html_node import text_node_to_html_node
from src.text_node import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self): 
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.IMAGE)
        self.assertNotEqual(node, node2)

    def test_eq_with_url(self):
        node = TextNode("A", TextType.BOLD, "https://boot.dev")
        node2 = TextNode("A", TextType.BOLD, "https://boot.dev")
        self.assertEqual(node, node2)

    def test_url_none(self):
        node = TextNode("Este es un nodo", TextType.TEXT, None)
        node2 = TextNode("Este es un nodo", TextType.TEXT, "https://url.com")
        self.assertNotEqual(node, node2)

    def test_different_text_type(self):
        node = TextNode("Mismo texto", TextType.BOLD, None)
        node2 = TextNode("Mismo texto", TextType.ITALIC, None)
        self.assertNotEqual(node, node2)

    def test_text_different(self):
        node = TextNode("Texto A", TextType.CODE, None)
        node2 = TextNode("Texto B", TextType.CODE, None)
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_img(self):
        node = TextNode("Alt text", TextType.IMAGE, "https://best-free-travel-images-image-2.jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props["alt"], "Alt text")
        self.assertEqual(html_node.props["src"], "https://best-free-travel-images-image-2.jpg")


if __name__ == "__main__":
    unittest.main()