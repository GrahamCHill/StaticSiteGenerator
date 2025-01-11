import unittest

from src.extract_markdownimage import extract_markdown_images, extract_markdown_links


class TestMarkdownExtractors(unittest.TestCase):

    def test_extract_markdown_images(self):
        text = (
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) "
            "and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        )
        expected = [
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
        ]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_markdown_images_no_images(self):
        text = "This is text with no images!"
        expected = []
        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_markdown_images_edge_cases(self):
        text = (
            "![alt](https://example.com/image.png) "
            "![empty]() ![multiple spaces](https://example.com)"
        )
        expected = [
            ("alt", "https://example.com/image.png"),
            ("empty", ""),
            ("multiple spaces", "https://example.com"),
        ]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_markdown_links(self):
        text = (
            "This is text with a link [to boot dev](https://www.boot.dev) "
            "and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        expected = [
            ("to boot dev", "https://www.boot.dev"),
            ("to youtube", "https://www.youtube.com/@bootdotdev"),
        ]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_extract_markdown_links_no_links(self):
        text = "This is text with no links!"
        expected = []
        self.assertEqual(extract_markdown_links(text), expected)

    def test_extract_markdown_links_edge_cases(self):
        text = (
            "[anchor](https://example.com) "
            "[empty]() [multiple spaces](https://example.com)"
        )
        expected = [
            ("anchor", "https://example.com"),
            ("empty", ""),
            ("multiple spaces", "https://example.com"),
        ]
        self.assertEqual(extract_markdown_links(text), expected)

if __name__ == "__main__":
    unittest.main()
