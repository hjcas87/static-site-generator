import unittest
from src.helpers.split_nodes import split_nodes_image, split_nodes_link
from src.text_node import TextNode, TextType

class TestSplitLinksAndImages(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertEqual(len(new_nodes), 4)
        self.assertEqual(new_nodes[0].text, "This is text with an ")
        self.assertEqual(new_nodes[1].text, "image")
        self.assertEqual(new_nodes[1].text_type, TextType.IMAGE)
        self.assertEqual(new_nodes[3].text_type, TextType.IMAGE)

    def test_split_links(self):
        node = TextNode(
            "Check [boot dev](https://www.boot.dev) now",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[1].text, "boot dev")
        self.assertEqual(new_nodes[1].url, "https://www.boot.dev")
        self.assertEqual(new_nodes[1].text_type, TextType.LINK)

    def test_split_mixed_media(self):
        node = TextNode(
            "Text with ![img](https://url.com/i.png) and a [link](https://url.com)",
            TextType.TEXT,
        )
        image_nodes = split_nodes_image([node])
        final_nodes = split_nodes_link(image_nodes)
        
        self.assertEqual(len(final_nodes), 4)
        self.assertEqual(final_nodes[1].text_type, TextType.IMAGE)
        self.assertEqual(final_nodes[3].text_type, TextType.LINK)
        self.assertEqual(final_nodes[0].text, "Text with ")
        self.assertEqual(final_nodes[2].text, " and a ")

if __name__ == "__main__":
    unittest.main()