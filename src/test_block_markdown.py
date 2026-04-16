import unittest

from block_markdown import markdown_to_blocks, block_to_block, BlockType


class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_h3(self):
        block = "### A Title"
        result = block_to_block(block)
        expected = BlockType.HEADING
        self.assertEqual(result, expected)

    def test_block_to_block_not_h2(self):
        block = "##A Title"
        result = block_to_block(block)
        expected = BlockType.HEADING
        self.assertNotEqual(result, expected)

    def test_block_to_block_not_h1(self):
        block = "# "
        result = block_to_block(block)
        expected = BlockType.HEADING
        self.assertNotEqual(result, expected)

    def test_block_to_block_code(self):
        block = """```
print('hello world')
```
"""
        result = block_to_block(block)
        expected = BlockType.CODE
        self.assertEqual(result, expected)

    def test_block_to_block_not_code(self):
        block = """``
print('hello world')
```
"""
        result = block_to_block(block)
        expected = BlockType.CODE
        self.assertNotEqual(result, expected)

    def test_block_to_block_quote(self):
        block = """>This is a quote
> On multilines
>end
"""
        result = block_to_block(block)
        expected = BlockType.QUOTE
        self.assertEqual(result, expected)

    def test_block_to_block_not_quote(self):
        block = """>This is a quote
> On multilines
end
"""
        result = block_to_block(block)
        expected = BlockType.QUOTE
        self.assertNotEqual(result, expected)

    def test_block_to_block_ul(self):
        block = """- This is a quote
- On multilines
- end
"""
        result = block_to_block(block)
        expected = BlockType.UNORDERED_LIST
        self.assertEqual(result, expected)

    def test_block_to_block_not_ul(self):
        block = """-This is a quote
- On multilines
end
"""
        result = block_to_block(block)
        expected = BlockType.UNORDERED_LIST
        self.assertNotEqual(result, expected)

    def test_block_to_block_ol(self):
        block = """1. This is a quote
2. On multilines
3. end
"""
        result = block_to_block(block)
        expected = BlockType.ORDERED_LIST
        self.assertEqual(result, expected)

    def test_block_to_block_not_ol(self):
        block = """1. This is a quote
2 On multilines
1. end
"""
        result = block_to_block(block)
        expected = BlockType.ORDERED_LIST
        self.assertNotEqual(result, expected)
