import unittest
from Spreadsheet.HTML import Table

class TestMatrix(unittest.TestCase):

    def test_matrix_with_instance(self):
        data = [[1,'a'], [2,'b']]
        html = '<table><tr><td>1</td><td>a</td></tr><tr><td>2</td><td>b</td></tr></table>'

        self.assertEqual(
            html,
            Table( { 'data': data, 'matrix': 1 } ).generate(),
            "one dict via constructor only"
        )

        self.assertEqual(
            html,
            Table( 'data', data, 'matrix', 1 ).generate(),
            "list via constructor only"
        )

        self.assertEqual(
            html,
            Table().generate( { 'data': data, 'matrix': 1 } ),
            "one dict via constructor only"
        )

        self.assertEqual(
            html,
            Table().generate( 'data', data, 'matrix', 1 ),
            "list via constructor only"
        )

        self.assertEqual(
            html,
            Table( { 'data': data } ).generate( { 'matrix': 1 } ),
            "via constructor and method"
        )

        self.assertEqual(
            html,
            Table( { 'matrix': 1 } ).generate( { 'data': data } ),
            "via constructor and method"
        )

        html = '<table><tr><th>1</th><th>a</th></tr><tr><td>2</td><td>b</td></tr></table>'

        self.assertEqual(
            html,
            Table( { 'matrix': 1 } ).generate( { 'data': data, 'matrix': 0 } ),
            "override constructor arg in method"
        )


if __name__ == '__main__':
    unittest.main()
