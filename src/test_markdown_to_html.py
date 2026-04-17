import unittest

from block_markdown import BlockType
from markdown_to_html import (
    block_to_html_node,
    heading_to_html,
    code_to_html,
    quote_to_html,
    unordered_list_to_html,
    ordered_list_to_html,
    paragraph_to_html,
    markdown_to_html_node,
)


class TestMarkdownToHtml(unittest.TestCase):
    def test_block_to_html_node_p(self):
        block_type = BlockType.PARAGRAPH
        block = """
This is **bolded** paragraph
text in a p
tag here
"""
        result = block_to_html_node(block_type, block).to_html()
        expected = "<p>This is <b>bolded</b> paragraph text in a p tag here</p>"
        self.assertEqual(result, expected)

    def test_block_to_html_node_code(self):
        block_type = BlockType.CODE
        block = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
        result = block_to_html_node(block_type, block).to_html()
        expected = "<pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre>"
        self.assertEqual(result, expected)

    def test_block_to_html_node_h1(self):
        block_type = BlockType.HEADING
        block = "## A **bolded** title"
        result = block_to_html_node(block_type, block).to_html()
        expected = "<h2>A <b>bolded</b> title</h2>"
        self.assertEqual(result, expected)

    def test_block_to_html_node_ol(self):
        block_type = BlockType.ORDERED_LIST
        block = """
1. First item
2. Second item
3. Third item
4. Fourth item 
"""
        result = block_to_html_node(block_type, block).to_html()
        expected = "<ol><li>First item</li><li>Second item</li><li>Third item</li><li>Fourth item </li></ol>"
        self.assertEqual(result, expected)

    def test_block_to_html_node_ul(self):
        block_type = BlockType.UNORDERED_LIST
        block = """
- Item 1
- Item 2
- Item 3
"""
        result = block_to_html_node(block_type, block).to_html()
        expected = "<ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul>"
        self.assertEqual(result, expected)

    def test_block_to_html_node_quote(self):
        block_type = BlockType.QUOTE
        block = """> Dorothy followed her through many of the beautiful rooms in her castle.
> The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with wood."""
        result = block_to_html_node(block_type, block).to_html()
        expected = "<blockquote>Dorothy followed her through many of the beautiful rooms in her castle. The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with wood.</blockquote>"
        self.assertEqual(result, expected)

    ###### Tests fonctions utlititaires

    ############ Headings

    def test_heading_to_html_h1(self):
        block = "# A title"
        result = heading_to_html(block).to_html()
        expected = "<h1>A title</h1>"
        self.assertEqual(result, expected)

    def test_heading_to_htm_h2_bold(self):
        block = "## A **bolded** title"
        result = heading_to_html(block).to_html()
        expected = "<h2>A <b>bolded</b> title</h2>"
        self.assertEqual(result, expected)

    def test_heading_to_htm_h3_bold_italic(self):
        block = "### A **bolded** _italic_ title"
        result = heading_to_html(block).to_html()
        expected = "<h3>A <b>bolded</b> <i>italic</i> title</h3>"
        self.assertEqual(result, expected)

    def test_heading_to_htm_h3_italic_bold(self):
        block = "### A _italic_ **bolded** title"
        result = heading_to_html(block).to_html()
        expected = "<h3>A <i>italic</i> <b>bolded</b> title</h3>"
        self.assertEqual(result, expected)

    ############ Code

    def test_code_to_html(self):
        block = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
        result = code_to_html(block).to_html()
        expected = "<pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre>"
        self.assertEqual(result, expected)

    ############ Quote

    def test_quote_to_html(self):
        block = """> Dorothy followed her through many of the beautiful rooms in her castle.
> The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with wood."""
        result = quote_to_html(block).to_html()
        expected = "<blockquote>Dorothy followed her through many of the beautiful rooms in her castle. The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with wood.</blockquote>"
        self.assertEqual(result, expected)

    ############ Unordered list

    def test_unordered_list_to_html(self):
        block = """
- Item 1
- Item 2
- Item 3
"""
        result = unordered_list_to_html(block).to_html()
        expected = "<ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul>"
        self.assertEqual(result, expected)

    ############ Ordered list

    def test_ordered_list_to_html(self):
        block = """
1. First item
2. Second item
3. Third item
4. Fourth item 
"""
        result = ordered_list_to_html(block).to_html()
        expected = "<ol><li>First item</li><li>Second item</li><li>Third item</li><li>Fourth item </li></ol>"
        self.assertEqual(result, expected)

    ############ Paragraph

    def test_paragraph_to_html(self):
        block = """
This is **bolded** paragraph
text in a p
tag here
"""
        result = paragraph_to_html(block).to_html()
        expected = "<p>This is <b>bolded</b> paragraph text in a p tag here</p>"
        self.assertEqual(result, expected)

    ###### Tests markdown_to_html_node

    def test_markdown_to_html_node_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        result = markdown_to_html_node(md).to_html()
        expected = "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>"
        self.assertEqual(result, expected)

    def test_markdown_to_html_node_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
        result = markdown_to_html_node(md).to_html()
        expected = "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>"
        self.assertEqual(result, expected)

    def test_markdown_to_html_node_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""
        result = markdown_to_html_node(md).to_html()
        expected = "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>"
        self.assertEqual(result, expected)

    def test_markdown_to_html_node_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""
        result = markdown_to_html_node(md).to_html()
        expected = "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>"
        self.assertEqual(result, expected)

    def test_markdown_to_html_node_lists(self):
        md = """
- This is a list
- with items
- and _more_ items

1. This is an `ordered` list
2. with items
3. and more items

"""
        result = markdown_to_html_node(md).to_html()
        expected = "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>"
        self.assertEqual(result, expected)
