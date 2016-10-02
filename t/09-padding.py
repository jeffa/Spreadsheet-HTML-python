import unittest
from Spreadsheet.HTML import Table

class TestPadding(unittest.TestCase):

    def test_padding(self):

        data = [
            [ 'header1', 'header2', 'header3' ],
            [ 'foo1', 'bar1' ],
            [ 'foo2' ],
        ]

        gen = Table()

        self.assertEqual(
            '<table><tr><th>header1</th><th>header2</th><th>header3</th></tr><tr><td>foo1</td><td>bar1</td><td>&nbsp;</td></tr><tr><td>foo2</td><td>&nbsp;</td><td>&nbsp;</td></tr></table>',
            gen.generate( {'data': data } ),
            "empty values are padded with default"
        )

        data = [
            [ 'header1', 'header2' ],
            [ 'foo1', 'bar1', 'baz1' ],
            [ 'foo2', 'bar2', 'baz2', 'qux2' ],
        ]

        self.assertEqual(
            '<table><tr><th>header1</th><th>header2</th></tr><tr><td>foo1</td><td>bar1</td></tr><tr><td>foo2</td><td>bar2</td></tr></table>',
            gen.generate( {'data': data } ),
            "extra values are truncated"
        )

    def test_fill(self):
        return

        data = [
            [ 'header1', 'header2' ],
            [ 'foo1', 'bar1' ],
            [ 'foo2', 'bar2' ],
        ]

        gen = Table()

        self.assertEqual(
            '<table><tr><th>&nbsp;</th><th>&nbsp;</th><th>&nbsp;</th><th>&nbsp;</th><th>&nbsp;</th></tr><tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr></table>',
            gen.generate( {'fill': '3x5' } ),
            "fill works with no data"
        )

        self.assertEqual(
            '<table><tr><th>header1</th><th>header2</th></tr><tr><td>foo1</td><td>bar1</td></tr><tr><td>foo2</td><td>bar2</td></tr></table>',
            gen.generate( {'fill': '1x2', 'data': data } ),
            "fill does not truncate larger data"
        )

        self.assertEqual(
            '<table><tr><th>&nbsp;</th></tr></table>',
            gen.generate( {'fill': nil } ),
            "fill defaults to 1x1 with with invalid data (nil)"
        )

        self.assertEqual(
            '<table><tr><th>&nbsp;</th></tr></table>',
            gen.generate( {'fill': '' } ),
            "fill defaults to 1x1 with with invalid data (empty)"
        )

        self.assertEqual(
            '<table><tr><th>&nbsp;</th></tr></table>',
            gen.generate( {'fill': '0x0' } ),
            "fill defaults to 1x1 with with invalid data (zero)"
        )

        self.assertEqual(
            '<table><tr><th>&nbsp;</th></tr></table>',
            gen.generate( {'fill': '-2x4' } ),
            "fill defaults to 1x1 with with invalid data (first negative)"
        )

        self.assertEqual(
            '<table><tr><th>&nbsp;</th></tr></table>',
            gen.generate( {'fill': '1x-3' } ),
            "fill defaults to 1x1 with with invalid data (second negative)"
        )

        self.assertEqual(
            '<table><tr><th>&nbsp;</th></tr></table>',
            gen.generate( {'fill': 'axb' } ),
            "fill defaults to 1x1 with with invalid data (letters)"
        )

        self.assertEqual(
            '<table><tr><th>header1</th><th>header2</th><th>&nbsp;</th><th>&nbsp;</th><th>&nbsp;</th></tr><tr><td>foo1</td><td>bar1</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td>foo2</td><td>bar2</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr></table>',
            gen.generate( {'fill': '3x5', 'data': data } ),
            "fill works with valid data"
        )


if __name__ == '__main__':
    unittest.main()
