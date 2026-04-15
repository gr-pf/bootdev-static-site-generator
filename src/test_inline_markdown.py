import unittest

from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
)
from textnode import TextType, TextNode


class TestSplitNode(unittest.TestCase):
    def test_split_nodes_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_italic(self):
        node = TextNode("This is text with a _italic_ word", TextType.TEXT)
        result = split_nodes_delimiter([node], "_", TextType.ITALIC)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_bold(self):
        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_bold_italic(self):
        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        node2 = TextNode("This is text with a _italic_ word", TextType.TEXT)
        result = split_nodes_delimiter([node, node2], "**", TextType.BOLD)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
            node2,
        ]
        self.assertEqual(result, expected)

    def test_extract_markdown_images(self):
        result = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        expected = [("image", "https://i.imgur.com/zjjcJKZ.png")]
        self.assertListEqual(result, expected)

    def test_extract_markdown_images_multiples(self):
        result = extract_markdown_images(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        )
        expected = [
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
        ]
        self.assertListEqual(result, expected)

    def test_extract_markdown_links(self):
        result = extract_markdown_links(
            "This is text with an [link](https://www.dummy.com)"
        )
        expected = [("link", "https://www.dummy.com")]
        self.assertListEqual(result, expected)

    def test_extract_markdown_links_multiples(self):
        result = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        expected = [
            ("to boot dev", "https://www.boot.dev"),
            ("to youtube", "https://www.youtube.com/@bootdotdev"),
        ]
        self.assertListEqual(result, expected)
