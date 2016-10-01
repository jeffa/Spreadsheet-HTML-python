import unittest
from Spreadsheet.HTML import Table

class TestEmpty(unittest.TestCase):

    def test_empty(self):

        data = [
            [ 'header1', 'header2', 'header3' ],
            [ 'foo1', '', 'baz1' ],
            [ '', 'bar2', '' ],
        ]

        self.assertEqual(
            '<table><tr><th>header1</th><th>header2</th><th>header3</th></tr><tr><td>foo1</td><td>&nbsp;</td><td>baz1</td></tr><tr><td>&nbsp;</td><td>bar2</td><td>&nbsp;</td></tr></table>',
            Table( { 'data': data } ).generate(),
            "empty values are defaulted to &nbsp;"
        )

        self.assertEqual(
            '<table><tr><th>header1</th><th>header2</th><th>header3</th></tr><tr><td>foo1</td><td> </td><td>baz1</td></tr><tr><td> </td><td>bar2</td><td> </td></tr></table>',
            Table( { 'data': data } ).generate( { 'empty': ' ' } ),
            "empty values can be overriden (space)"
        )

        self.assertEqual(
            '<table><tr><th>header1</th><th>header2</th><th>header3</th></tr><tr><td>foo1</td><td>0</td><td>baz1</td></tr><tr><td>0</td><td>bar2</td><td>0</td></tr></table>',
            Table( { 'data': data } ).generate( { 'empty': 0 } ),
            "empty values can be overriden (zero)"
        )


if __name__ == '__main__':
    unittest.main()
