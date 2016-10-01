Spreadsheet-HTML (python)
=====================
Just another HTML table generator for Python.  [![pypi package](https://badge.fury.io/py/Spreadsheet-HTML.svg)](https://pypi.python.org/pypi/Spreadsheet-HTML) [![Build Status](https://api.travis-ci.org/jeffa/Spreadsheet-HTML-python.svg?branch=master)](https://travis-ci.org/jeffa/Spreadsheet-HTML-python)

Description
-----------
Generate HTML tables with ease (HTML4, HTML5, XHTML and SVG).

Synopsis
--------
```python
from Spreadsheet.HTML import Table

data = [ [1,2,3], [4,5,6], [7,8,9] ]
generator = Table()
puts generator.generate( data )
puts generator.generate( { 'data': data } )

generator = Table( { 'data': data, 'indent': "\t" } )
puts generator.portrait( { 'encodes': 1 } )
puts generator.landscape( { 'encode': 1 } )

puts generator.generate( { 'tgroups': 1 } )
puts generator.generate( { 'tgroups': 2, 'indent': None } )

puts generator.generate( { 'tr': { 'class': [ 'odd', 'even' ] } )
```

Installation
------------
```
pip install Spreadsheet-HTML
```

License and Copyright
---------------------
See [License](License.md).
