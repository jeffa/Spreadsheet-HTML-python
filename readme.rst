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

Development
===========

Spreadsheet-HTML is far from complete. What is the point of writing all this code to
merely generate some tables if it cannot provide some USEFUL presets that are consistent
yet FLEXIBLE? The following still needs to be implemented:

* Parameters
   * file - read and convert from XLS, CSV, JSON, YAML, HTML, GIF, PNG and JPG
   * wrap - turn one dimension arrays into tables
   * headings - apply callback to each cell in headings row

* Methods
   * calendar - generate calenders
   * tic-tac-toe - easy game to implemenent with JavaScript
   * chess - a bit more adventurous but doable
   * sudoku - another doable game
   * conway - game of life 

* Source hosted at `GitHub <http://github.com/jeffa/Spreadsheet-HTML-python>`_

Well tested pull requests welcome. :)
