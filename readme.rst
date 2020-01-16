++++++++++++++++
Spreadsheet-HTML
++++++++++++++++

Just another HMTL table generator.

Installing
==========

Use pip:

    $ pip install HTML-Auto Spreadsheet-HTML

Using Spreadsheet-HTML
======================

# Object oriented or procedural interface.

    from Spreadsheet.HTML import Table

    data = [ [1,2,3], [10,11,12], ['<foo>','<bar>','<baz>'] ]

    print( Table().generate( data ) )

    print( Table().generate( { 'data': data, 'indent' : "\\t" } ) )

    table = Table( { 'data': data, 'indent': "\\t" } )

    print( table.generate() )

# Encodes default entities or any specified character.

    print( table.generate( { 'encodes': 1 } ) )

    print( table.generate( { 'encode': 1 } ) )

# Supports multiple orientations.

    print( table.portrait() )

    print( table.landscape() )

# Handles grouping.

    print( table.generate( { 'tgroups': 1 } ) )

    print( table.generate( { 'tgroups': 2 } ) )

# Supports rotating attributes.

    print( table.generate( { 'tr': { 'class': [ 'odd', 'even' ] } } ) )

development
===========

* Source hosted at `GitHub <http://github.com/jeffa/Spreadsheet-HTML-python>`_

Well tested pull requests welcome. :)
