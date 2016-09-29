import unittest
from Spreadsheet.HTML import Table

class TestHeadless(unittest.TestCase):

    def test_headless(self):

        data = [[1,'a'], [2,'b'], [3,'c']]
        html = '<table><tr><td>2</td><td>b</td></tr><tr><td>3</td><td>c</td></tr></table>'

        self.assertEqual(
            html,
            Table( { 'data': data, 'headless': 1 } ).generate(),
            "dict via constructor only"
        )

        self.assertEqual(
            html,
            Table( 'data', data, 'headless', 1 ).generate(),
            "list via constructor only"
        )

        self.assertEqual(
            html,
            Table( { 'data': data } ).generate( { 'headless': 1 } ),
            "dicts via constructor and method"
        )

        self.assertEqual(
            html,
            Table( 'data', data ).generate( 'headless', 1 ),
            "lists via constructor and method"
        )


if __name__ == '__main__':
    unittest.main()
