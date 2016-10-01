import unittest
from Spreadsheet.HTML import Table

class TestCaption(unittest.TestCase):

    def test_caption(self):

        data = [
            [ 'a', 'b', 'c' ],
            [ '1', '2', '3' ],
            [ '4', '5', '6' ],
        ]

        gen = Table( { 'data': data, 'caption': "My Table" } )

        self.assertEqual(
            '<table><caption>My Table</caption><tr><th>a</th><th>b</th><th>c</th></tr><tr><td>1</td><td>2</td><td>3</td></tr><tr><td>4</td><td>5</td><td>6</td></tr></table>',
            gen.generate(),
            "caption present from generate()"
        )

        gen = Table( { 'data': data, 'caption': { "My Table": { 'key': 'value' } } } )

        self.assertEqual(
            '<table><caption key="value">My Table</caption><tr><th>a</th><th>b</th><th>c</th></tr><tr><td>1</td><td>2</td><td>3</td></tr><tr><td>4</td><td>5</td><td>6</td></tr></table>',
            gen.generate(),
            "caption present from generate()"
        )

        self.assertEqual(
            '<table><caption key="value">My Table</caption><thead><tr><th>a</th><th>b</th><th>c</th></tr></thead><tfoot><tr><td>4</td><td>5</td><td>6</td></tr></tfoot><tbody><tr><td>1</td><td>2</td><td>3</td></tr></tbody></table>',
            gen.generate( { 'tgroups': 2 } ),
            "caption present from generate() with tgroups"
        )

        self.assertEqual(
            '<table><caption>0</caption><tr><th>a</th><th>b</th><th>c</th></tr><tr><td>1</td><td>2</td><td>3</td></tr><tr><td>4</td><td>5</td><td>6</td></tr></table>',
            gen.generate( { 'caption': 0 } ),
            "caption can be overriden"
        )


if __name__ == '__main__':
    unittest.main()
