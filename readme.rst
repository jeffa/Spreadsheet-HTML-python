++++++++++++++++
Spreadsheet-HTML
++++++++++++++++

Just another HMTL table generator.

Installing
==========

Use pip:

    $ pip install Spreadsheet-HTML

Using Spreadsheet-HTML
======================

Generate HTML tables with ease (HTML4, HTML5, XHTML).

    from Spreadsheet.HTML import Table

    data = [ [1,2,3], [10,11,12], ['<foo>','<bar>','<baz>'] ]

    print( Table().generate( data ) )

    print( Table().generate( { 'data': data } ) )

Supports multiple orientations.

    generator = Table( { 'data': data, 'indent': "\t" } ) )

    print( generator.portrait( { 'encodes': 1 } ) )

    print( generator.landscape( { 'encode': 1 } ) )

Handles grouping.

    print( generator.generate( { 'tgroups': 1 } ) )

    print( generator.generate( { 'tgroups': 2, 'indent': None } ) )

Supports rotating attributes.

    print( generator.generate( { 'tr': { 'class': [ 'odd', 'even' ] } ) )

development
===========

* Source hosted at `GitHub <http://github.com/jeffa/Spreadsheet-HTML-python>`_

Pull requests welcomed. Make sure your patches are well tested.
