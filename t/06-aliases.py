import unittest
from Spreadsheet.HTML import Table

class TestAliases(unittest.TestCase):

    def test_portrait(self):

        data = [
            ['header1', 'header2', 'header3', 'header4'],
            ['foo1', 'bar1', 'baz1', 'qux1'],
            ['foo2', 'bar2', 'baz2', 'qux2'],
            ['foo3', 'bar3', 'baz3', 'qux3'],
            ['foo4', 'bar4', 'baz4', 'qux4']
        ]

        html = '<table><tr><th>header1</th><th>header2</th><th>header3</th><th>header4</th></tr><tr><td>foo1</td><td>bar1</td><td>baz1</td><td>qux1</td></tr><tr><td>foo2</td><td>bar2</td><td>baz2</td><td>qux2</td></tr><tr><td>foo3</td><td>bar3</td><td>baz3</td><td>qux3</td></tr><tr><td>foo4</td><td>bar4</td><td>baz4</td><td>qux4</td></tr></table>'

        self.assertEqual(
            html,
            Table( { 'data': data } ).portrait(),
            "via constructor and method"
        )
        self.assertEqual(
            html,
            Table().portrait( data ),
            "with array ref"
        )
        self.assertEqual(
            html,
            Table().portrait( { 'data': data } ),
            "named args only"
        )

        self.assertEqual(
            html,
            Table( { 'data': data, 'theta': 90 } ).portrait(),
            "theta disabled via constructor and method"
        )
        self.assertEqual(
            html,
            Table().portrait( data, 'theta', 180 ),
            "theta disabled with array ref"
        )
        self.assertEqual(
            html,
            Table().portrait( { 'data': data, 'theta': 270 } ),
            "theta disabled named args only"
        )

        html = '<table><tr><td>header1</td><td>header2</td><td>header3</td><td>header4</td></tr><tr><td>foo1</td><td>bar1</td><td>baz1</td><td>qux1</td></tr><tr><td>foo2</td><td>bar2</td><td>baz2</td><td>qux2</td></tr><tr><td>foo3</td><td>bar3</td><td>baz3</td><td>qux3</td></tr><tr><td>foo4</td><td>bar4</td><td>baz4</td><td>qux4</td></tr></table>'

        self.assertEqual(
            html,
            Table( { 'data': data, 'matrix': 1 } ).portrait(),
            "matrix via constructor and method"
        )
        self.assertEqual(
            html,
            Table().portrait( data, 'matrix', 1 ),
            "matrix with array ref"
        )
        self.assertEqual(
            html,
            Table().portrait( { 'data': data, 'matrix': 1 } ),
            "matrix named args only"
        )

        html = '<table><tr><td>foo1</td><td>bar1</td><td>baz1</td><td>qux1</td></tr><tr><td>foo2</td><td>bar2</td><td>baz2</td><td>qux2</td></tr><tr><td>foo3</td><td>bar3</td><td>baz3</td><td>qux3</td></tr><tr><td>foo4</td><td>bar4</td><td>baz4</td><td>qux4</td></tr></table>'

        self.assertEqual(
            html,
            Table( { 'data': data, 'headless': 1 } ).portrait(),
            "headless via constructor and method"
        )
        self.assertEqual(
            html,
            Table().portrait( data, 'headless', 1 ),
            "headless with array ref"
        )
        self.assertEqual(
            html,
            Table().portrait( { 'data': data, 'headless': 1 } ),
            "headless named args only"
        )

    def test_landscape(self):

        data = [
            ['header1', 'header2', 'header3', 'header4'],
            ['foo1', 'bar1', 'baz1', 'qux1'],
            ['foo2', 'bar2', 'baz2', 'qux2'],
            ['foo3', 'bar3', 'baz3', 'qux3'],
            ['foo4', 'bar4', 'baz4', 'qux4']
        ]

        html = '<table><tr><th>header1</th><td>foo1</td><td>foo2</td><td>foo3</td><td>foo4</td></tr><tr><th>header2</th><td>bar1</td><td>bar2</td><td>bar3</td><td>bar4</td></tr><tr><th>header3</th><td>baz1</td><td>baz2</td><td>baz3</td><td>baz4</td></tr><tr><th>header4</th><td>qux1</td><td>qux2</td><td>qux3</td><td>qux4</td></tr></table>'

        self.assertEqual(
            html,
            Table( { 'data': data } ).landscape(),
            "via constructor and method"
        )
        self.assertEqual(
            html,
            Table().landscape( data ),
            "with array ref"
        )
        self.assertEqual(
            html,
            Table().landscape( { 'data': data } ),
            "named args only"
        )

        self.assertEqual(
            html,
            Table( { 'data': data, 'theta': 90 } ).landscape(),
            "theta disabled via constructor and method"
        )
        self.assertEqual(
            html,
            Table().landscape( data, 'theta', 180 ),
            "theta disabled with array ref"
        )
        self.assertEqual(
            html,
            Table().landscape( { 'data': data, 'theta': 270 } ),
            "theta disabled named args only"
        )

        html = '<table><tr><td>header1</td><td>foo1</td><td>foo2</td><td>foo3</td><td>foo4</td></tr><tr><td>header2</td><td>bar1</td><td>bar2</td><td>bar3</td><td>bar4</td></tr><tr><td>header3</td><td>baz1</td><td>baz2</td><td>baz3</td><td>baz4</td></tr><tr><td>header4</td><td>qux1</td><td>qux2</td><td>qux3</td><td>qux4</td></tr></table>'

        self.assertEqual(
            html,
            Table( { 'data': data, 'matrix': 1 } ).landscape(),
            "matrix via constructor and method"
        )
        self.assertEqual(
            html,
            Table().landscape( data, 'matrix', 1 ),
            "matrix with array ref"
        )
        self.assertEqual(
            html,
            Table().landscape( { 'data': data, 'matrix': 1 } ),
            "matrix named args only"
        )

        html = '<table><tr><td>foo1</td><td>foo2</td><td>foo3</td><td>foo4</td></tr><tr><td>bar1</td><td>bar2</td><td>bar3</td><td>bar4</td></tr><tr><td>baz1</td><td>baz2</td><td>baz3</td><td>baz4</td></tr><tr><td>qux1</td><td>qux2</td><td>qux3</td><td>qux4</td></tr></table>'

        self.assertEqual(
            html,
            Table( { 'data': data, 'headless': 1 } ).landscape(),
            "headless via constructor and method"
        )
        self.assertEqual(
            html,
            Table().landscape( data, 'headless', 1 ),
            "headless with array ref"
        )
        self.assertEqual(
            html,
            Table().landscape( { 'data': data, 'headless': 1 } ),
            "headless named args only"
        )

    def test_aliases(self):

        data = [
            ['header1', 'header2', 'header3', 'header4'],
            ['foo1', 'bar1', 'baz1', 'qux1'],
            ['foo2', 'bar2', 'baz2', 'qux2'],
            ['foo3', 'bar3', 'baz3', 'qux3'],
            ['foo4', 'bar4', 'baz4', 'qux4']
        ]

        self.assertEqual(
            Table( { 'data': data } ).generate(),
            Table( { 'data': data } ).portrait(),
            "portrait is generate via constructor and method"
        )
        self.assertEqual(
            Table().generate( data ),
            Table().portrait( data ),
            "portrait is generate with array ref"
        )
        self.assertEqual(
            Table().generate( { 'data': data } ),
            Table().portrait( { 'data': data } ),
            "portrait is generate named args only"
        )

        self.assertEqual(
            Table( { 'data': data } ).generate(),
            Table( { 'data': data } ).north(),
            "north is generate via constructor and method"
        )
        self.assertEqual(
            Table().generate( data ),
            Table().north( data ),
            "north is generate with array ref"
        )
        self.assertEqual(
            Table().generate( { 'data': data } ),
            Table().north( { 'data': data } ),
            "north is generate named args only"
        )

        self.assertEqual(
            Table( { 'data': data } ).west(),
            Table( { 'data': data } ).landscape(),
            "west is landscape via constructor and method"
        )
        self.assertEqual(
            Table().west( data ),
            Table().landscape( data ),
            "west is landscape with array ref"
        )
        self.assertEqual(
            Table().west( { 'data': data } ),
            Table().landscape( { 'data': data } ),
            "west is landscape named args only"
        )

        self.assertEqual(
            Table( { 'data': data } ).west(),
            Table( { 'data': data, 'theta': -270 } ).generate(),
            "west is theta -270 via constructor and method"
        )
        self.assertEqual(
            Table().west( data ),
            Table().generate( data, 'theta', -270 ),
            "west is theta -270 with array ref"
        )
        self.assertEqual(
            Table().west( { 'data': data } ),
            Table().generate( { 'data': data, 'theta': -270 } ),
            "west is theta -270 named args only"
        )

        self.assertEqual(
            Table( { 'data': data } ).east(),
            Table( { 'data': data, 'theta': 90, 'pinhead': 1 } ).generate(),
            "east is theta 90 via constructor and method"
        )
        self.assertEqual(
            Table().east( data ),
            Table().generate( data, 'theta', 90, 'pinhead', 1 ),
            "east is theta 90 with array ref"
        )
        self.assertEqual(
            Table().east( { 'data': data } ),
            Table().generate( { 'data': data, 'theta': 90, 'pinhead': 1 } ),
            "east is theta 90 named args only"
        )

        self.assertEqual(
            Table( { 'data': data } ).south(),
            Table( { 'data': data, 'theta': -180, 'pinhead': 1 } ).generate(),
            "south is theta -180 via constructor and method"
        )
        self.assertEqual(
            Table().south( data ),
            Table().generate( data, 'theta', -180, 'pinhead', 1  ),
            "south is theta -180 with array ref"
        )
        self.assertEqual(
            Table().south( { 'data': data } ),
            Table().generate( { 'data': data, 'theta': -180, 'pinhead': 1 } ),
            "south is theta -180 named args only"
        )


if __name__ == '__main__':
    unittest.main()
