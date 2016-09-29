import unittest
from Spreadsheet.HTML import Table

class TestIndent(unittest.TestCase):

    def test_indent(self):

        data = [
            [ 'header1', 'header2', 'header3' ],
            [ 'foo1', 'bar1', 'baz1' ],
            [ 'foo2', 'bar2', 'baz2' ],
        ]

        gen = Table( { 'data': data, 'indent': '  ' } )

        self.assertEqual(
            "<table>\n  <tr>\n    <th>header1</th>\n    <th>header2</th>\n    <th>header3</th>\n  </tr>\n  <tr>\n    <td>foo1</td>\n    <td>bar1</td>\n    <td>baz1</td>\n  </tr>\n  <tr>\n    <td>foo2</td>\n    <td>bar2</td>\n    <td>baz2</td>\n  </tr>\n</table>\n",
            gen.generate(),
            "results have proper indentation"
        )


if __name__ == '__main__':
    unittest.main()
