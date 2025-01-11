import unittest
from src.blocktoblock import block_to_block_type

class TestBlockToBlockType(unittest.TestCase):
    def test_heading(self):
        self.assertEqual(block_to_block_type("# Heading"), "heading")
        self.assertEqual(block_to_block_type("###### Small Heading"), "heading")

    def test_code_block(self):
        self.assertEqual(block_to_block_type("```\nCode block content\n```"), "code")
        self.assertEqual(block_to_block_type("```\nAnother code block\n```"), "code")

    def test_quote_block(self):
        self.assertEqual(block_to_block_type("> Quote line 1\n> Quote line 2"), "quote")
        self.assertEqual(block_to_block_type("> Single quote line"), "quote")

    def test_unordered_list_block(self):
        self.assertEqual(block_to_block_type("* Item 1\n* Item 2"), "unordered_list")
        self.assertEqual(block_to_block_type("- Item 1\n- Item 2"), "unordered_list")

    def test_ordered_list_block(self):
        self.assertEqual(block_to_block_type("1. First item\n2. Second item\n3. Third item"), "ordered_list")
        self.assertEqual(block_to_block_type("1. Item\n2. Another item"), "ordered_list")

    def test_ordered_list_incorrect_numbers(self):
        self.assertEqual(block_to_block_type("1. Item\n3. Another item"), "paragraph")  # Invalid ordered list

    def test_paragraph(self):
        self.assertEqual(block_to_block_type("This is just a normal paragraph."), "paragraph")
        self.assertEqual(block_to_block_type("Another line of text."), "paragraph")

    def test_mixed_block(self):
        self.assertEqual(block_to_block_type("> Quote\nNormal text"), "paragraph")  # Mixed content

    def test_empty_block(self):
        self.assertEqual(block_to_block_type(""), "paragraph")  # Treat empty as a paragraph

