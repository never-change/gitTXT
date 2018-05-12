
HOST = '124.239.173.36'
PORT = 80

#HOST = '192.168.0.107'
#PORT = 8069
DB = 'odoo'
USER = 'odoo@odoo.com'
PASS = '09090909'


import odoorpc

def login():
    odoo = odoorpc.ODOO(HOST,port=PORT)
    odoo.login(DB,USER,PASS)
    return odoo


class Model():
    def __init__(self,name=None):
        odoo = login()
        self.odoo = odoo

        self.env = odoo.env
        if name:
            self._name = name

    def __getattr__(self, method):
        """Provide a dynamic access to a RPC *instance* method (which applies
        on the current recordset).

        .. doctest::

            >>> Partner = odoo.env['res.partner']
            >>> Partner.write([1], {'name': 'YourCompany'}) # Class method
            True
            >>> partner = Partner.browse(1)
            >>> partner.write({'name': 'YourCompany'})      # Instance method
            True

        """
        if method.startswith('_'):
            return super(Model, self).__getattr__(method)
        def rpc_method(*args, **kwargs):
            mdl = self.env[self._name]
            return getattr(mdl,method)(*args, **kwargs)
            
        return rpc_method




