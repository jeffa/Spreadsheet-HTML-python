from HTML.Auto import Tag

__version__='0.0.1'

class Table:

    def __init__( self, *args ):
        self.params = self._process( *args )

    def generate( self, *args ):
        self.params.update( self._process( *args ) )

        return self._make_table()

    def _make_table( self ):
        cdata   = []
        tr_attr = self.params['tr'] if 'tr' in self.params else {}
        tb_attr = self.params['table'] if 'table' in self.params else {}

        for c in self.params['data']:
            cdata.append( { 'tag': 'tr', 'attr': tr_attr, 'cdata': c } )

        return self.params['auto'].tag({ 'tag': 'table', 'attr': tb_attr, 'cdata': cdata })

    def _process( self, *args ):
        params = self._params( *args )

        empty = params['empty'] if 'empty' in params else '&nbsp;'
        tag   = 'th'

        if '_max_rows' in params:
            for r in range( params['_max_rows'] ):

                row = []
                for c in range( params['_max_cols'] ):
                    attr  = params['tag'] if 'tag' in params else {}
                    cdata = params['data'][r][c]
                    row.append( { 'tag': tag, 'attr': attr, 'cdata': cdata } )

                params['data'][r] = row
                tag = 'td'

        return params

    def _params( self, *thingy ):
        data   = []
        params = {}

        things = list( thingy )
        while things:
            thing = things.pop(0)
            if type( thing ) is list:
                if type( thing[0] ) is list:
                    data = thing
                else:
                    data.append( thing )
            elif type(thing) is dict:
                data   = thing.pop( 'data', None )
                params = thing
            else:
                if thing is 'data':
                    data = things.pop(0)
                else:
                    params[thing] = things.pop(0)

        if len(data):
            params['data']      = list( data )
            params['_max_rows'] = len( data )
            params['_max_cols'] = len( data[0] )

        params['auto'] = Tag({
            #'indent': params.get( 'indent', '' ),
            'level': params.get( 'level', 0 ),
            'sort': params.get( 'attr_sort', 0 )
        })

        return params
