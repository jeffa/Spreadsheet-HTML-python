import unittest
from Spreadsheet.HTML import Table

class TestColGroup(unittest.TestCase):

    def test_colgroup(self):
        return

        data = [
            ['a','b','c'],
            [1,2,3],
            [4,5,6],
        ]

        gen = Table( { 'data': data, 'colgroup': { 'span': 3, 'width': 100 }, 'attr_sort': 1 } )

        self.assertEqual(
            '<table><colgroup span="3" width="100" /><tr><th>a</th><th>b</th><th>c</th></tr><tr><td>1</td><td>2</td><td>3</td></tr><tr><td>4</td><td>5</td><td>6</td></tr></table>',
            gen.generate(),
            "colgroup present from generate()"
        )

        self.assertEqual(
            '<table><colgroup span="3" width="100" /><thead><tr><th>a</th><th>b</th><th>c</th></tr></thead><tfoot><tr><td>4</td><td>5</td><td>6</td></tr></tfoot><tbody><tr><td>1</td><td>2</td><td>3</td></tr></tbody></table>',
            gen.generate( { 'tgroups': 2 } ),
            "colgroup present from generate() with tgroups"
        )

        self.assertEqual(
            '<table><tr><th>a</th><th>b</th><th>c</th></tr><tr><td>1</td><td>2</td><td>3</td></tr><tr><td>4</td><td>5</td><td>6</td></tr></table>',
            gen.generate( { 'colgroup': None } ),
            "colgroup can be overriden"
        )

        self.assertEqual(
            '<table><tr><th>a</th><th>b</th><th>c</th></tr><tr><td>1</td><td>2</td><td>3</td></tr><tr><td>4</td><td>5</td><td>6</td></tr></table>',
            gen.generate( { 'colgroup': 1 } ),
            "colgroup yields no-op if scalar"
        )

        self.assertEqual(
            '<table><colgroup color="red" span="1" /><colgroup color="blue" span="2" /><tr><th>a</th><th>b</th><th>c</th></tr><tr><td>1</td><td>2</td><td>3</td></tr><tr><td>4</td><td>5</td><td>6</td></tr></table>',
            gen.generate( { 'colgroup': [ { 'span': 1, 'color': 'red' }, { 'span': 2, 'color': 'blue' } ] } ),
            "can specify multiple colgroups"
        )


    def test_col(self):
        return

        data = [
            ['a','b','c'],
            [1,2,3],
            [4,5,6],
        ]

        gen = Table( { 'data': data, 'colgroup': { 'span': 3, 'width': 100 }, 'attr_sort': 1 } );

        self.assertEqual(
            '<table><colgroup span="3" width="100"><col /></colgroup><tr><th>a</th><th>b</th><th>c</th></tr><tr><td>1</td><td>2</td><td>3</td></tr><tr><td>4</td><td>5</td><td>6</td></tr></table>',
            gen.generate( { 'col': {} } ),
            "colgroup wraps col"
        )

        self.assertEqual(
            '<table><colgroup span="3" width="100"><col /><col /><col /></colgroup><tr><th>a</th><th>b</th><th>c</th></tr><tr><td>1</td><td>2</td><td>3</td></tr><tr><td>4</td><td>5</td><td>6</td></tr></table>',
            gen.generate( { 'col': [{},{},{}] } ),
            "colgroup wraps multiple cols"
        )

        self.assertEqual(
            '<table><colgroup><col /></colgroup><tr><th>a</th><th>b</th><th>c</th></tr><tr><td>1</td><td>2</td><td>3</td></tr><tr><td>4</td><td>5</td><td>6</td></tr></table>',
            gen.generate( { 'colgroup': None, 'col': {} } ),
            "colgroup can be overriden when col is present too"
        )


        gen = Table( { 'data': data, 'col': [{},{},{}] } );

        self.assertEqual(
            '<table><colgroup><col /><col /><col /></colgroup><tr><th>a</th><th>b</th><th>c</th></tr><tr><td>1</td><td>2</td><td>3</td></tr><tr><td>4</td><td>5</td><td>6</td></tr></table>',
            gen.generate( { 'colgroup': {} } ),
            "multiple cols against single colgroup"
        )

        self.assertEqual(
            '<table><colgroup /><colgroup /><colgroup /><tr><th>a</th><th>b</th><th>c</th></tr><tr><td>1</td><td>2</td><td>3</td></tr><tr><td>4</td><td>5</td><td>6</td></tr></table>',
            gen.generate( { 'col': None, 'colgroup': [{},{},{}] } ),
            "no cols against multiple colgroups"
        )

        self.assertEqual(
            '<table><colgroup><col /><col /><col /></colgroup><colgroup><col /><col /><col /></colgroup><colgroup><col /><col /><col /></colgroup><tr><th>a</th><th>b</th><th>c</th></tr><tr><td>1</td><td>2</td><td>3</td></tr><tr><td>4</td><td>5</td><td>6</td></tr></table>',
            gen.generate( { 'colgroup': [{},{},{}] } ),
            "multiple cols against multiple colgroups"
        )


if __name__ == '__main__':
    unittest.main()
