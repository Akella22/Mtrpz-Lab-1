import unittest
from unittest.mock import patch, mock_open, MagicMock
import argparse
import sys

from md_to_html import md_to_html, md_to_ansi, main

class TestMarkdownConversion(unittest.TestCase):

    def test_md_to_html(self):
        markdown = "# Title\n## Subtitle\n### Subsubtitle\n- item1\n- item2\nPlain text"
        expected_html = (
            "<h1>Title</h1>\n"
            "<h2>Subtitle</h2>\n"
            "<h3>Subsubtitle</h3>\n"
            "<li>item1</li>\n"
            "<li>item2</li>\n"
            "<p>Plain text</p>"
        )
        self.assertEqual(md_to_html(markdown), expected_html)

    def test_md_to_ansi(self):
        markdown = "# Title\n## Subtitle\n### Subsubtitle\n- item1\n- item2\nPlain text"
        expected_ansi = (
            "\033[1mTitle\033[0m\n"
            "\033[1mSubtitle\033[0m\n"
            "\033[1mSubsubtitle\033[0m\n"
            "\033[7mitem1\033[0m\n"
            "\033[7mitem2\033[0m\n"
            "\033[7mPlain text\033[0m"
        )
        self.assertEqual(md_to_ansi(markdown), expected_ansi)

    @patch('builtins.open', new_callable=mock_open, read_data="# Title")
    @patch('sys.stdout', new_callable=MagicMock)
    def test_main_no_output_file_ansi(self, mock_stdout, mock_open_file):
        test_args = ['script.py', 'input.md', '--format', 'ansi']
        with patch.object(sys, 'argv', test_args):
            main()
        mock_open_file.assert_called_once_with('input.md', 'r', encoding='utf-8')
        mock_stdout.getvalue = MagicMock(return_value='\033[1mTitle\033[0m\n')
        self.assertIn('\033[1mTitle\033[0m\n', mock_stdout.getvalue())

    @patch('builtins.open', new_callable=mock_open, read_data="# Title")
    @patch('builtins.open', new_callable=mock_open)
    def test_main_output_file_html(self, mock_open_file_read, mock_open_file_write):
        test_args = ['script.py', 'input.md', '--out', 'output.html', '--format', 'html']
        with patch.object(sys, 'argv', test_args):
            main()
        mock_open_file_read.assert_any_call('input.md', 'r', encoding='utf-8')
        mock_open_file_write.assert_any_call('output.html', 'w', encoding='utf-8')
        mock_open_file_write().write.assert_called_once_with('<h1>Title</h1>\n')

    @patch('builtins.open', new_callable=mock_open, read_data="# Title")
    @patch('sys.stderr', new_callable=MagicMock)
    def test_main_file_not_found(self, mock_stderr, mock_open_file):
        mock_open_file.side_effect = FileNotFoundError
        test_args = ['script.py', 'non_existent_file.md']
        with patch.object(sys, 'argv', test_args):
            with self.assertRaises(SystemExit):
                main()
        mock_stderr.write.assert_called_with('Error: The file non_existent_file.md does not exist.\n')

    @patch('builtins.open', new_callable=mock_open, read_data="# Title")
    @patch('sys.stderr', new_callable=MagicMock)
    def test_main_general_exception(self, mock_stderr, mock_open_file):
        mock_open_file.side_effect = Exception("General Error")
        test_args = ['script.py', 'input.md']
        with patch.object(sys, 'argv', test_args):
            with self.assertRaises(SystemExit):
                main()
        mock_stderr.write.assert_called_with('Error: General Error\n')

if __name__ == '__main__':
    unittest.main()
