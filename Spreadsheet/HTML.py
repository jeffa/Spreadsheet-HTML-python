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

        if 'tgroups' in params and params['tgroups'] > 0:
            body = params['data']
            matrix = params.get( 'matrix', 0 )
            head = body.pop(0) if not matrix and len( body ) > 2 else None
            foot = body.pop()  if not matrix and params['tgroups'] > 1 and len( body ) > 2 else None

            body_rows = []
            for r in body:
                body_rows.append( { 'tag': 'tr', 'attr': tr_attr, 'cdata': r } )
            if head:
                thead_tr_attr = params['thead.tr'] if 'thead.tr' in params else {}
                thead_attr    = params['thead'] if 'thead' in params else {}
                head_row = { 'tag': 'tr', 'attr': thead_tr_attr, 'cdata': head }
                cdata.append( { 'tag': 'thead', 'attr': thead_attr, 'cdata': head_row } )
            if foot:
                tfoot_tr_attr = params['tfoot.tr'] if 'tfoot.tr' in params else {}
                tfoot_attr    = params['tfoot'] if 'tfoot' in params else {}
                foot_row = { 'tag': 'tr', 'attr': tfoot_tr_attr, 'cdata': foot }
                cdata.append( { 'tag': 'tfoot', 'attr': tfoot_attr, 'cdata': foot_row } )

            tbody_attr = params['tbody'] if 'tbody' in params else {}
            cdata.append( { 'tag': 'tbody', 'attr': tbody_attr, 'cdata': body_rows } )

        else:
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
