import unittest

from generate_content_html import extract_title


class TestGenerateContentHTML(unittest.TestCase):
    def test_extract_title_oneline(self):
        md = "# Hello"
        result = extract_title(md)
        expected = "Hello"
        self.assertEqual(result, expected)

    def test_extract_title_multilines(self):
        md = """
This is not the first line
# Hello
This is not the last line
"""
        result = extract_title(md)
        expected = "Hello"
        self.assertEqual(result, expected)

    def test_extract_title_exception_multiple(self):
        md = """
This is not the first line
# Hello
This is not the last line
# Hello
"""
        with self.assertRaises(Exception) as ctx:
            extract_title(md)
        self.assertEqual("Error: mutliple titles.", str(ctx.exception))

    def test_extract_title_exception_none(self):
        md = """
This is not the first line
## Hello
This is not the last line
### Hello
"""
        with self.assertRaises(Exception) as ctx:
            extract_title(md)
        self.assertEqual("There is no Title", str(ctx.exception))
