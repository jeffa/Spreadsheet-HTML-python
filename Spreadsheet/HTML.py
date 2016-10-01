import re
from HTML.Auto import Tag

__version__='0.0.1'

class Table:

    def __init__( self, *args ):
        self.params = args

    def generate( self, *args ):
        params = self._process( *args )

        return self._make_table( params )

    def _make_table( self, params ):
        cdata   = []
        tr_attr = params['tr'] if 'tr' in params else {}
        tb_attr = params['table'] if 'table' in params else {}

        if 'caption' in params:
            cdata.append( self._tag( 'caption', params['caption'] ) )

        for c in params['data']:
            cdata.append( { 'tag': 'tr', 'attr': tr_attr, 'cdata': c } )

        return params['auto'].tag( { 'tag': 'table', 'attr': tb_attr, 'cdata': cdata } )

    def _process( self, *args ):
        params = self._args( *args )

        empty = params['empty'] if 'empty' in params else '&nbsp;'
        tag   = 'td' if params.get( 'matrix' ) or params.get( 'headless' ) else 'th'

        if '_max_rows' in params:
            for r in range( params['_max_rows'] ):

                row = []
                for c in range( params['_max_cols'] ):
                    attr  = params['tag'] if 'tag' in params else {}
                    cdata = str( params['data'][r][c] )

                    # attr extrapolation here
                    # encoding here
                    regex = re.compile(r"^\s*$")
                    if regex.match( cdata ):
                        cdata = empty
                    row.append( { 'tag': tag, 'attr': attr, 'cdata': cdata } )

                params['data'][r] = row
                tag = 'td'

        if 'headless' in params:
            params['data'].pop(0)

        return params

    def _args( self, *thingy ):
        data = []
        params = {}

        things = list( self.params ) + list( thingy )
        while things:
            thing = things.pop(0)
            if type( thing ) is list:
                if type( thing[0] ) is list:
                    data = thing
                else:
                    data.append( thing )
            elif type(thing) is dict:
                data = thing['data'] if 'data' in thing else data
                params.update( thing )
            else:
                if thing is 'data':
                    data = things.pop(0)
                else:
                    params[thing] = things.pop(0)

        params['data'] = list( data )
        params['_max_rows'] = len( params['data'] )
        params['_max_cols'] = len( params['data'][0] )

        tag_params = {
            'level': params.get( 'level', 0 ),
            'sort': params.get( 'attr_sort', 0 )
        }
        if 'indent' in params:
            tag_params['indent'] = params['indent']
        params['auto'] = Tag( tag_params )

        return params

    def _tag( self, tag, cdata ):
        tag = { 'tag': tag, 'cdata': cdata }
        if type( cdata ) is dict:
            keys = list( cdata.keys() )
            tag['cdata'] = keys[0]
            tag['attr']  = cdata[ keys[0] ]
        return tag
