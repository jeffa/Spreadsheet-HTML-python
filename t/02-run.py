import unittest
from Spreadsheet.HTML import Table

class TestTable(unittest.TestCase):

    def test_args_via_method(self):
        data = [[1,'a'], [2,'b']]
        html = '<table><tr><th>1</th><th>a</th></tr><tr><td>2</td><td>b</td></tr></table>'

        gen  = Table()

        self.assertEqual(
            html,
            gen.generate( [1,'a'], [2,'b'] ),
            "two array refs"
        )

        self.assertEqual(
            html,
            gen.generate( data ),
            "one array ref"
        )

        self.assertEqual(
            html,
            gen.generate({ 'data': data }),
            "one named arg"
        )

        self.assertEqual(
            html,
            gen.generate( 'data', data ),
            "multiple arg"
        )

    def test_args_via_constructor(self):
        data = [[1,'a'], [2,'b']]
        html = '<table><tr><th>1</th><th>a</th></tr><tr><td>2</td><td>b</td></tr></table>'

        self.assertEqual(
            html,
            Table( [1,'a'], [2,'b'] ).generate(),
            "two array refs"
        )

        self.assertEqual(
            html,
            Table( data ).generate(),
            "one array ref"
        )

        self.assertEqual(
            html,
            Table({ 'data': data }).generate(),
            "one named arg"
        )

        self.assertEqual(
            html,
            Table( 'data', data ).generate(),
            "multiple arg"
        )

    def test_args_via_reused_constructor(self):
        data = [[1,'a'], [2,'b']]
        html = '<table><tr><th>1</th><th>a</th></tr><tr><td>2</td><td>b</td></tr></table>'

        gen  = Table( data )

        self.assertEqual(
            html,
            gen.generate(),
            "1st call to method using one arg"
        )

        self.assertEqual(
            html,
            gen.generate(),
            "2nd call to method using one arg"
        )

        gen  = Table( 'data', data )

        self.assertEqual(
            html,
            gen.generate(),
            "1st call to method using two args"
        )

        self.assertEqual(
            html,
            gen.generate(),
            "2nd call to method using two args"
        )

        gen  = Table( { 'data': data } )

        self.assertEqual(
            html,
            gen.generate(),
            "1st call to method using dict"
        )

        self.assertEqual(
            html,
            gen.generate(),
            "2nd call to method using dict"
        )


if __name__ == '__main__':
    unittest.main()
