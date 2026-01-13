import unittest

from src.helpers.block_to_block_type import block_to_block_type, BlockType 

class TestBlockTypes(unittest.TestCase):
    def test_block_to_block_types(self):
        self.assertEqual(block_to_block_type("# heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("### heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("###### heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("####### invalid"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("#no_space"), BlockType.PARAGRAPH)
        
        code_block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(code_block), BlockType.CODE)
        
        quote_block = "> line 1\n> line 2\n> line 3"
        self.assertEqual(block_to_block_type(quote_block), BlockType.QUOTE)
        
        bad_quote = "> line 1\nline 2"
        self.assertEqual(block_to_block_type(bad_quote), BlockType.PARAGRAPH)
        
        ul_block = "- item 1\n- item 2"
        self.assertEqual(block_to_block_type(ul_block), BlockType.UNORDERED_LIST)
        
        bad_ul = "- item 1\n* item 2"
        self.assertEqual(block_to_block_type(bad_ul), BlockType.PARAGRAPH)
        
        ol_block = "1. first\n2. second\n3. third"
        self.assertEqual(block_to_block_type(ol_block), BlockType.ORDERED_LIST)
        
        bad_ol = "1. first\n3. third"
        self.assertEqual(block_to_block_type(bad_ol), BlockType.PARAGRAPH)
        
        bad_ol_start = "2. start\n3. next"
        self.assertEqual(block_to_block_type(bad_ol_start), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()