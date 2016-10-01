import unittest
from Spreadsheet.HTML import Table

class TestHeadless(unittest.TestCase):

    def test_0flip(self):

        data = [
            ['header1', 'header2', 'header3', 'header4'],
            ['foo1', 'bar1', 'baz1', 'qux1'],
            ['foo2', 'bar2', 'baz2', 'qux2'],
            ['foo3', 'bar3', 'baz3', 'qux3'],
            ['foo4', 'bar4', 'baz4', 'qux4']
        ]

        html = '<table><tr><th>header4</th><th>header3</th><th>header2</th><th>header1</th></tr><tr><td>qux1</td><td>baz1</td><td>bar1</td><td>foo1</td></tr><tr><td>qux2</td><td>baz2</td><td>bar2</td><td>foo2</td></tr><tr><td>qux3</td><td>baz3</td><td>bar3</td><td>foo3</td></tr><tr><td>qux4</td><td>baz4</td><td>bar4</td><td>foo4</td></tr></table>'

        self.assertEqual(
            html,
            Table( { 'data': data, 'flip': 1 } ).generate(),
            "via constructor only"
        )
        self.assertEqual(
            html,
            Table( { 'data': data } ).generate( { 'flip': 1 } ),
            "via constructor and method"
        )
        self.assertEqual(
            html,
            Table().generate( data, 'flip', 1 ),
            "with array ref"
        )
        self.assertEqual(
            html,
            Table().generate( { 'data': data, 'flip': 1 } ),
            "named args only"
        )

    def test_90(self):

        data = [
            ['header1', 'header2', 'header3', 'header4'],
            ['foo1', 'bar1', 'baz1', 'qux1'],
            ['foo2', 'bar2', 'baz2', 'qux2'],
            ['foo3', 'bar3', 'baz3', 'qux3'],
            ['foo4', 'bar4', 'baz4', 'qux4']
        ]

        html = '<table><tr><td>foo4</td><td>foo3</td><td>foo2</td><td>foo1</td><th>header1</th></tr><tr><td>bar4</td><td>bar3</td><td>bar2</td><td>bar1</td><th>header2</th></tr><tr><td>baz4</td><td>baz3</td><td>baz2</td><td>baz1</td><th>header3</th></tr><tr><td>qux4</td><td>qux3</td><td>qux2</td><td>qux1</td><th>header4</th></tr></table>'

        self.assertEqual(
            html,
            Table( { 'data': data, 'theta': 90 } ).generate(),
            "via constructor only"
        )
        self.assertEqual(
            html,
            Table( { 'data': data } ).generate( { 'theta': 90 } ),
            "via constructor and method"
        )
        self.assertEqual(
            html,
            Table().generate( data, 'theta', 90 ),
            "with array ref"
        )
        self.assertEqual(
            html,
            Table().generate( { 'data': data, 'theta': 90 } ),
            "named args only"
        )

    def test_90_pinhead(self):

        data = [
            ['header1', 'header2', 'header3', 'header4'],
            ['foo1', 'bar1', 'baz1', 'qux1'],
            ['foo2', 'bar2', 'baz2', 'qux2'],
            ['foo3', 'bar3', 'baz3', 'qux3'],
            ['foo4', 'bar4', 'baz4', 'qux4']
        ]

        html = '<table><tr><td>foo1</td><td>foo2</td><td>foo3</td><td>foo4</td><th>header1</th></tr><tr><td>bar1</td><td>bar2</td><td>bar3</td><td>bar4</td><th>header2</th></tr><tr><td>baz1</td><td>baz2</td><td>baz3</td><td>baz4</td><th>header3</th></tr><tr><td>qux1</td><td>qux2</td><td>qux3</td><td>qux4</td><th>header4</th></tr></table>'

        self.assertEqual(
            html,
            Table( { 'data': data, 'theta': 90, 'pinhead': 1 } ).generate(),
            "via constructor only"
        )
        self.assertEqual(
            html,
            Table( { 'data': data } ).generate( { 'theta': 90, 'pinhead': 1 } ),
            "via constructor and method"
        )
        self.assertEqual(
            html,
            Table().generate( data, 'theta', 90, 'pinhead', 1 ),
            "with array ref"
        )
        self.assertEqual(
            html,
            Table().generate( { 'data': data, 'theta': 90, 'pinhead': 1 } ),
            "named args only"
        )

    def test_neg90(self):

        data = [
            ['header1', 'header2', 'header3', 'header4'],
            ['foo1', 'bar1', 'baz1', 'qux1'],
            ['foo2', 'bar2', 'baz2', 'qux2'],
            ['foo3', 'bar3', 'baz3', 'qux3'],
            ['foo4', 'bar4', 'baz4', 'qux4']
        ]

        html = '<table><tr><td>qux4</td><td>qux3</td><td>qux2</td><td>qux1</td><th>header4</th></tr><tr><td>baz4</td><td>baz3</td><td>baz2</td><td>baz1</td><th>header3</th></tr><tr><td>bar4</td><td>bar3</td><td>bar2</td><td>bar1</td><th>header2</th></tr><tr><td>foo4</td><td>foo3</td><td>foo2</td><td>foo1</td><th>header1</th></tr></table>'

        self.assertEqual(
            html,
            Table( { 'data': data, 'theta': -90 } ).generate(),
            "via constructor only"
        )
        self.assertEqual(
            html,
            Table( { 'data': data } ).generate( { 'theta': -90 } ),
            "via constructor and method"
        )
        self.assertEqual(
            html,
            Table().generate( data, 'theta', -90 ),
            "with array ref"
        )
        self.assertEqual(
            html,
            Table().generate( { 'data': data, 'theta': -90 } ),
            "named args only"
        )

    def test_neg90_pinhead(self):

        data = [
            ['header1', 'header2', 'header3', 'header4'],
            ['foo1', 'bar1', 'baz1', 'qux1'],
            ['foo2', 'bar2', 'baz2', 'qux2'],
            ['foo3', 'bar3', 'baz3', 'qux3'],
            ['foo4', 'bar4', 'baz4', 'qux4']
        ]

        html = '<table><tr><td>qux1</td><td>qux2</td><td>qux3</td><td>qux4</td><th>header4</th></tr><tr><td>baz1</td><td>baz2</td><td>baz3</td><td>baz4</td><th>header3</th></tr><tr><td>bar1</td><td>bar2</td><td>bar3</td><td>bar4</td><th>header2</th></tr><tr><td>foo1</td><td>foo2</td><td>foo3</td><td>foo4</td><th>header1</th></tr></table>'

        self.assertEqual(
            html,
            Table( { 'data': data, 'theta': -90, 'pinhead': 1 } ).generate(),
            "via constructor only"
        )
        self.assertEqual(
            html,
            Table( { 'data': data } ).generate( { 'theta': -90, 'pinhead': 1 } ),
            "via constructor and method"
        )
        self.assertEqual(
            html,
            Table().generate( data, 'theta', -90, 'pinhead', 1 ),
            "with array ref"
        )
        self.assertEqual(
            html,
            Table().generate( { 'data': data, 'theta': -90, 'pinhead': 1 } ),
            "named args only"
        )

    def test_180(self):

        data = [
            ['header1', 'header2', 'header3', 'header4'],
            ['foo1', 'bar1', 'baz1', 'qux1'],
            ['foo2', 'bar2', 'baz2', 'qux2'],
            ['foo3', 'bar3', 'baz3', 'qux3'],
            ['foo4', 'bar4', 'baz4', 'qux4']
        ]

        html = '<table><tr><td>qux4</td><td>baz4</td><td>bar4</td><td>foo4</td></tr><tr><td>qux3</td><td>baz3</td><td>bar3</td><td>foo3</td></tr><tr><td>qux2</td><td>baz2</td><td>bar2</td><td>foo2</td></tr><tr><td>qux1</td><td>baz1</td><td>bar1</td><td>foo1</td></tr><tr><th>header4</th><th>header3</th><th>header2</th><th>header1</th></tr></table>'

        self.assertEqual(
            html,
            Table( { 'data': data, 'theta': 180 } ).generate(),
            "via constructor only"
        )
        self.assertEqual(
            html,
            Table( { 'data': data } ).generate( { 'theta': 180 } ),
            "via constructor and method"
        )
        self.assertEqual(
            html,
            Table().generate( data, 'theta', 180 ),
            "with array ref"
        )
        self.assertEqual(
            html,
            Table().generate( { 'data': data, 'theta': 180 } ),
            "named args only"
        )

    def test_180_pinhead(self):

        data = [
            ['header1', 'header2', 'header3', 'header4'],
            ['foo1', 'bar1', 'baz1', 'qux1'],
            ['foo2', 'bar2', 'baz2', 'qux2'],
            ['foo3', 'bar3', 'baz3', 'qux3'],
            ['foo4', 'bar4', 'baz4', 'qux4']
        ]

        html = '<table><tr><td>qux1</td><td>baz1</td><td>bar1</td><td>foo1</td></tr><tr><td>qux2</td><td>baz2</td><td>bar2</td><td>foo2</td></tr><tr><td>qux3</td><td>baz3</td><td>bar3</td><td>foo3</td></tr><tr><td>qux4</td><td>baz4</td><td>bar4</td><td>foo4</td></tr><tr><th>header4</th><th>header3</th><th>header2</th><th>header1</th></tr></table>'

        self.assertEqual(
            html,
            Table( { 'data': data, 'theta': 180, 'pinhead': 1 } ).generate(),
            "via constructor only"
        )
        self.assertEqual(
            html,
            Table( { 'data': data } ).generate( { 'theta': 180, 'pinhead': 1 } ),
            "via constructor and method"
        )
        self.assertEqual(
            html,
            Table().generate( data, 'theta', 180, 'pinhead', 1 ),
            "with array ref"
        )
        self.assertEqual(
            html,
            Table().generate( { 'data': data, 'theta': 180, 'pinhead': 1 } ),
            "named args only"
        )

    def test_neg180(self):

        data = [
            ['header1', 'header2', 'header3', 'header4'],
            ['foo1', 'bar1', 'baz1', 'qux1'],
            ['foo2', 'bar2', 'baz2', 'qux2'],
            ['foo3', 'bar3', 'baz3', 'qux3'],
            ['foo4', 'bar4', 'baz4', 'qux4']
        ]

        html = '<table><tr><td>foo4</td><td>bar4</td><td>baz4</td><td>qux4</td></tr><tr><td>foo3</td><td>bar3</td><td>baz3</td><td>qux3</td></tr><tr><td>foo2</td><td>bar2</td><td>baz2</td><td>qux2</td></tr><tr><td>foo1</td><td>bar1</td><td>baz1</td><td>qux1</td></tr><tr><th>header1</th><th>header2</th><th>header3</th><th>header4</th></tr></table>'

        self.assertEqual(
            html,
            Table( { 'data': data, 'theta': -180 } ).generate(),
            "via constructor only"
        )
        self.assertEqual(
            html,
            Table( { 'data': data } ).generate( { 'theta': -180 } ),
            "via constructor and method"
        )
        self.assertEqual(
            html,
            Table().generate( data, 'theta', -180 ),
            "with array ref"
        )
        self.assertEqual(
            html,
            Table().generate( { 'data': data, 'theta': -180 } ),
            "named args only"
        )

    def test_neg180_pinhead(self):

        data = [
            ['header1', 'header2', 'header3', 'header4'],
            ['foo1', 'bar1', 'baz1', 'qux1'],
            ['foo2', 'bar2', 'baz2', 'qux2'],
            ['foo3', 'bar3', 'baz3', 'qux3'],
            ['foo4', 'bar4', 'baz4', 'qux4']
        ]

        html = '<table><tr><td>foo1</td><td>bar1</td><td>baz1</td><td>qux1</td></tr><tr><td>foo2</td><td>bar2</td><td>baz2</td><td>qux2</td></tr><tr><td>foo3</td><td>bar3</td><td>baz3</td><td>qux3</td></tr><tr><td>foo4</td><td>bar4</td><td>baz4</td><td>qux4</td></tr><tr><th>header1</th><th>header2</th><th>header3</th><th>header4</th></tr></table>'

        self.assertEqual(
            html,
            Table( { 'data': data, 'theta': -180, 'pinhead': 1 } ).generate(),
            "via constructor only"
        )
        self.assertEqual(
            html,
            Table( { 'data': data } ).generate( { 'theta': -180, 'pinhead': 1 } ),
            "via constructor and method"
        )
        self.assertEqual(
            html,
            Table().generate( data, 'theta', -180, 'pinhead', 1 ),
            "with array ref"
        )
        self.assertEqual(
            html,
            Table().generate( { 'data': data, 'theta': -180, 'pinhead': 1 } ),
            "named args only"
        )

    def test_270(self):

        data = [
            ['header1', 'header2', 'header3', 'header4'],
            ['foo1', 'bar1', 'baz1', 'qux1'],
            ['foo2', 'bar2', 'baz2', 'qux2'],
            ['foo3', 'bar3', 'baz3', 'qux3'],
            ['foo4', 'bar4', 'baz4', 'qux4']
        ]

        html = '<table><tr><th>header4</th><td>qux1</td><td>qux2</td><td>qux3</td><td>qux4</td></tr><tr><th>header3</th><td>baz1</td><td>baz2</td><td>baz3</td><td>baz4</td></tr><tr><th>header2</th><td>bar1</td><td>bar2</td><td>bar3</td><td>bar4</td></tr><tr><th>header1</th><td>foo1</td><td>foo2</td><td>foo3</td><td>foo4</td></tr></table>'

        self.assertEqual(
            html,
            Table( { 'data': data, 'theta': 270 } ).generate(),
            "via constructor only"
        )
        self.assertEqual(
            html,
            Table( { 'data': data } ).generate( { 'theta': 270 } ),
            "via constructor and method"
        )
        self.assertEqual(
            html,
            Table().generate( data, 'theta', 270 ),
            "with array ref"
        )
        self.assertEqual(
            html,
            Table().generate( { 'data': data, 'theta': 270 } ),
            "named args only"
        )

    def test_neg270(self):

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
            Table( { 'data': data, 'theta': -270 } ).generate(),
            "via constructor only"
        )
        self.assertEqual(
            html,
            Table( { 'data': data } ).generate( { 'theta': -270 } ),
            "via constructor and method"
        )
        self.assertEqual(
            html,
            Table().generate( data, 'theta', -270 ),
            "with array ref"
        )
        self.assertEqual(
            html,
            Table().generate( { 'data': data, 'theta': -270 } ),
            "named args only"
        )

    def test_flip(self):

        data = [
            ['header1', 'header2', 'header3', 'header4'],
            ['foo1', 'bar1', 'baz1', 'qux1'],
            ['foo2', 'bar2', 'baz2', 'qux2'],
            ['foo3', 'bar3', 'baz3', 'qux3'],
            ['foo4', 'bar4', 'baz4', 'qux4']
        ]

        self.assertEqual(
            Table( { 'data': data, 'theta': 90 } ).generate(),
            Table( { 'data': data, 'theta': -90, 'flip': 1 } ).generate(),
            "90"
        )
        self.assertEqual(
            Table( { 'data': data, 'theta': 180 } ).generate(),
            Table( { 'data': data, 'theta': -180, 'flip': 1 } ).generate(),
            "180"
        )
        self.assertEqual(
            Table( { 'data': data, 'theta': 270 } ).generate(),
            Table( { 'data': data, 'theta': -270, 'flip': 1 } ).generate(),
            "270"
        )


if __name__ == '__main__':
    unittest.main()
