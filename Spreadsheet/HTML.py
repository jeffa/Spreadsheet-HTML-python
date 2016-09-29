from HTML.Auto import Tag

__version__='0.0.1'

class Table:

    def generate( self, *args ):
        params = self._process( *args )

        return self._make_table( params )

    def __init__( self, *args ):
        self.params = self._process( *args )

    def _make_table( self, params ):
        cdata = []
        return params['auto'].tag({ 'tag': 'table' })

    def _process( self, *args ):
        params = self._args( *args )
        return params

    def _args( self, *thingy ):
        data = []
        args = {}

        things = list( thingy )
        while things:
            thing = things.pop(0)
            if type( thing ) is list:
                if type( thing[0] ) is list:
                    data = thing
                else:
                    data.append( thing )
            elif type(thing) is dict:
                data = thing.pop( 'data', None )
                args = thing
            else:
                if thing is 'data':
                    data = things.pop(0)
                else:
                    args[thing] = things.pop(0)

        args['auto'] = Tag({
            'indent': args.get( 'indent', '' ),
            'level': args.get( 'level', 0 ),
            'sort': args.get( 'attr_sort', 0 )
        })

        self.data = data
        return args
