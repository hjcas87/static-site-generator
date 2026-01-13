import unittest
from src.helpers.split_nodes import split_nodes_delimiter
from src.text_node import TextNode, TextType

class TestSplitNodes(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, "This is text with a ")
        self.assertEqual(new_nodes[1].text, "code block")
        self.assertEqual(new_nodes[1].text_type, TextType.CODE)
        self.assertEqual(new_nodes[2].text, " word")

    def test_split_double_delimiters(self):
        node = TextNode("Text with **bold** and `code` inline", TextType.TEXT)
        bold_split = split_nodes_delimiter([node], "**", TextType.BOLD)
        final_split = split_nodes_delimiter(bold_split, "`", TextType.CODE)
        self.assertEqual(len(final_split), 5)
        self.assertEqual(final_split[1].text_type, TextType.BOLD)
        self.assertEqual(final_split[3].text_type, TextType.CODE)
        self.assertEqual(final_split[0].text, "Text with ")
        self.assertEqual(final_split[2].text, " and ")

    def test_exception_unclosed(self):
        node = TextNode("This is **invalid bold", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "**", TextType.BOLD)

    def test_multiple_of_same_type(self):
        node = TextNode("One `code` and another `block`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(new_nodes), 4)

    def test_split_start_end(self):
        node = TextNode("`code` at start and end `code`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, "code")
        self.assertEqual(new_nodes[0].text_type, TextType.CODE)
        self.assertEqual(new_nodes[2].text, "code")
        self.assertEqual(new_nodes[2].text_type, TextType.CODE)

    def test_split_italic(self):
        node = TextNode("This is _italic_ text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[1].text, "italic")
        self.assertEqual(new_nodes[1].text_type, TextType.ITALIC)

if __name__ == "__main__":
    unittest.main()