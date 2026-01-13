import unittest
from src.helpers.text_to_textnodes import text_to_textnodes
from src.text_node import TextNode, TextType

class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_textnodes_full(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 10)
        self.assertEqual(nodes[1].text, "text")
        self.assertEqual(nodes[1].text_type, TextType.BOLD)
        self.assertEqual(nodes[3].text_type, TextType.ITALIC)
        self.assertEqual(nodes[5].text_type, TextType.CODE)
        self.assertEqual(nodes[7].text_type, TextType.IMAGE)
        self.assertEqual(nodes[9].text_type, TextType.LINK)

    def test_text_to_textnodes_simple(self):
        text = "Just some **bold** text"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text, "Just some ")
        self.assertEqual(nodes[1].text, "bold")

    def test_text_to_textnodes_no_formatting(self):
        text = "Plain text with nothing"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].text, "Plain text with nothing")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)

if __name__ == "__main__":
    unittest.main()