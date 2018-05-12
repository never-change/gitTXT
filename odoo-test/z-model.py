HOST = '192.168.56.105'
PORT = 8069
DB = 'TT'
USER = 'admin'
PASS = '123'


#import api

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


SUPERUSER_ID = 1

class API():
    def multi(*arg,**kwargs):
        pass
    
    def model(*arg,**kwargs):
        pass
    
    
    def returns(*arg,**kwargs):
        pass
    

api = API()

class BaseModel():
    """ To Sdudy
    """

    @api.model
    def default_get(self, fields_list):
        """ default_get(fields) -> default_values

        Return default values for the fields in ``fields_list``. Default
        values are determined by the context, user defaults, and the model
        itself.

        :param fields_list: a list of field names
        :return: a dictionary mapping each field name to its corresponding
            default value, if it has one.

        """
        pass

    @api.model
    def search_count(self, args):
        """ search_count(args) -> int

        Returns the number of records in the current model matching :ref:`the
        provided domain <reference/orm/domains>`.
        """
        pass


    @api.model
    #@api.returns('self',
    #    upgrade=lambda self, value, args, offset=0, limit=None, order=None, count=False: value if count else self.browse(value),
    #    downgrade=lambda self, value, args, offset=0, limit=None, order=None, count=False: value if count else value.ids)
    def search(self, args, offset=0, limit=None, order=None, count=False):
        """ search(args[, offset=0][, limit=None][, order=None][, count=False])

        Searches for records based on the ``args``
        :ref:`search domain <reference/orm/domains>`.

        :param args: :ref:`A search domain <reference/orm/domains>`. Use an empty
                     list to match all records.
        :param int offset: number of results to ignore (default: none)
        :param int limit: maximum number of records to return (default: all)
        :param str order: sort string
        :param bool count: if True, only counts and returns the number of matching records (default: False)
        :returns: at most ``limit`` records matching the search criteria

        :raise AccessError: * if user tries to bypass access rules for read on the requested object.
        """
        pass


    @api.multi
    def name_get(self):
        """ name_get() -> [(id, name), ...]

        Returns a textual representation for the records in ``self``.
        By default this is the value of the ``display_name`` field.

        :return: list of pairs ``(id, text_repr)`` for each records
        :rtype: list(tuple)
        """
        pass


    @api.model
    def name_create(self, name):
        """ name_create(name) -> record

        Create a new record by calling :meth:`~.create` with only one value
        provided: the display name of the new record.

        The new record will be initialized with any default values
        applicable to this model, or provided through the context. The usual
        behavior of :meth:`~.create` applies.

        :param name: display name of the record to create
        :rtype: tuple
        :return: the :meth:`~.name_get` pair value of the created record
        """
        pass


    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        """ name_search(name='', args=None, operator='ilike', limit=100) -> records

        Search for records that have a display name matching the given
        ``name`` pattern when compared with the given ``operator``, while also
        matching the optional search domain (``args``).

        This is used for example to provide suggestions based on a partial
        value for a relational field. Sometimes be seen as the inverse
        function of :meth:`~.name_get`, but it is not guaranteed to be.

        This method is equivalent to calling :meth:`~.search` with a search
        domain based on ``display_name`` and then :meth:`~.name_get` on the
        result of the search.

        :param str name: the name pattern to match
        :param list args: optional search domain (see :meth:`~.search` for
                          syntax), specifying further restrictions
        :param str operator: domain operator for matching ``name``, such as
                             ``'like'`` or ``'='``.
        :param int limit: optional max number of records to return
        :rtype: list
        :return: list of pairs ``(id, text_repr)`` for all matching records.
        """
        pass


    @api.model
    def fields_get(self, allfields=None, attributes=None):
        """ fields_get([fields][, attributes])

        Return the definition of each field.

        The returned value is a dictionary (indiced by field name) of
        dictionaries. The _inherits'd fields are included. The string, help,
        and selection (if present) attributes are translated.

        :param allfields: list of fields to document, all if empty or not provided
        :param attributes: list of description attributes to return for each field, all if empty or not provided
        """
        pass


    @api.model
    def check_field_access_rights(self, operation, fields):
        """
        Check the user access rights on the given fields. This raises Access
        Denied if the user does not have the rights. Otherwise it returns the
        fields (as is if the fields is not falsy, or the readable/writable
        fields if fields is falsy).
        """
        pass


    @api.multi
    def read(self, fields=None, load='_classic_read'):
        """ read([fields])

        Reads the requested fields for the records in ``self``, low-level/RPC
        method. In Python code, prefer :meth:`~.browse`.

        :param fields: list of field names to return (default is all fields)
        :return: a list of dictionaries mapping field names to their values,
                 with one dictionary per record
        :raise AccessError: if user has no read rights on some of the given
                records
        """

    @api.multi
    def get_metadata(self):
        """
        Returns some metadata about the given records.

        :return: list of ownership dictionaries for each requested record
        :rtype: list of dictionaries with the following keys:

                    * id: object id
                    * create_uid: user who created the record
                    * create_date: date when the record was created
                    * write_uid: last user who changed the record
                    * write_date: date of the last change to the record
                    * xmlid: XML ID to use to refer to this record (if there is one), in format ``module.name``
                    * noupdate: A boolean telling if the record will be updated or not
        """
        pass
        
        
    @api.model
    def check_access_rights(self, operation, raise_exception=True):
        """ Verifies that the operation given by ``operation`` is allowed for
            the current user according to the access rights.
        """
        pass
        
        
    @api.multi
    def check_access_rule(self, operation):
        """ Verifies that the operation given by ``operation`` is allowed for
            the current user according to ir.rules.

           :param operation: one of ``write``, ``unlink``
           :raise UserError: * if current ir.rules do not permit this operation.
           :return: None if the operation is allowed
        """
        pass
        
        
    @api.multi
    def unlink(self):
        """ unlink()

        Deletes the records of the current set

        :raise AccessError: * if user has no unlink rights on the requested object
                            * if user tries to bypass access rules for unlink on the requested object
        :raise UserError: if the record is default property for other records

        """
        pass
        
        
    #
    # TODO: Validate
    #
    @api.multi
    def write(self, vals):
        """ write(vals)

        Updates all records in the current set with the provided values.

        :param dict vals: fields to update and the value to set on them e.g::

                {'foo': 1, 'bar': "Qux"}

            will set the field ``foo`` to ``1`` and the field ``bar`` to
            ``"Qux"`` if those are valid (otherwise it will trigger an error).

        :raise AccessError: * if user has no write rights on the requested object
                            * if user tries to bypass access rules for write on the requested object
        :raise ValidateError: if user tries to enter invalid value for a field that is not in selection
        :raise UserError: if a loop would be created in a hierarchy of objects a result of the operation (such as setting an object as its own parent)

        * For numeric fields (:class:`~odoo.fields.Integer`,
          :class:`~odoo.fields.Float`) the value should be of the
          corresponding type
        * For :class:`~odoo.fields.Boolean`, the value should be a
          :class:`python:bool`
        * For :class:`~odoo.fields.Selection`, the value should match the
          selection values (generally :class:`python:str`, sometimes
          :class:`python:int`)
        * For :class:`~odoo.fields.Many2one`, the value should be the
          database identifier of the record to set
        * Other non-relational fields use a string for value

          .. danger::

              for historical and compatibility reasons,
              :class:`~odoo.fields.Date` and
              :class:`~odoo.fields.Datetime` fields use strings as values
              (written and read) rather than :class:`~python:datetime.date` or
              :class:`~python:datetime.datetime`. These date strings are
              UTC-only and formatted according to
              :const:`odoo.tools.misc.DEFAULT_SERVER_DATE_FORMAT` and
              :const:`odoo.tools.misc.DEFAULT_SERVER_DATETIME_FORMAT`
        * .. _openerp/models/relationals/format:

          :class:`~odoo.fields.One2many` and
          :class:`~odoo.fields.Many2many` use a special "commands" format to
          manipulate the set of records stored in/associated with the field.

          This format is a list of triplets executed sequentially, where each
          triplet is a command to execute on the set of records. Not all
          commands apply in all situations. Possible commands are:

          ``(0, _, values)``
              adds a new record created from the provided ``value`` dict.
          ``(1, id, values)``
              updates an existing record of id ``id`` with the values in
              ``values``. Can not be used in :meth:`~.create`.
          ``(2, id, _)``
              removes the record of id ``id`` from the set, then deletes it
              (from the database). Can not be used in :meth:`~.create`.
          ``(3, id, _)``
              removes the record of id ``id`` from the set, but does not
              delete it. Can not be used on
              :class:`~odoo.fields.One2many`. Can not be used in
              :meth:`~.create`.
          ``(4, id, _)``
              adds an existing record of id ``id`` to the set. Can not be
              used on :class:`~odoo.fields.One2many`.
          ``(5, _, _)``
              removes all records from the set, equivalent to using the
              command ``3`` on every record explicitly. Can not be used on
              :class:`~odoo.fields.One2many`. Can not be used in
              :meth:`~.create`.
          ``(6, _, ids)``
              replaces all existing records in the set by the ``ids`` list,
              equivalent to using the command ``5`` followed by a command
              ``4`` for each ``id`` in ``ids``.

          .. note:: Values marked as ``_`` in the list above are ignored and
                    can be anything, generally ``0`` or ``False``.
        """
        pass
        
    #
    # TODO: Should set perm to user.xxx
    #
    @api.model
    #@api.returns('self', lambda value: value.id)
    def create(self, vals):
        """ create(vals) -> record

        Creates a new record for the model.

        The new record is initialized using the values from ``vals`` and
        if necessary those from :meth:`~.default_get`.

        :param dict vals:
            values for the model's fields, as a dictionary::

                {'field_name': field_value, ...}

            see :meth:`~.write` for details
        :return: new record created
        :raise AccessError: * if user has no create rights on the requested object
                            * if user tries to bypass access rules for create on the requested object
        :raise ValidateError: if user tries to enter invalid value for a field that is not in selection
        :raise UserError: if a loop would be created in a hierarchy of objects a result of the operation (such as setting an object as its own parent)
        """
        pass
        
    @api.model
    def search_read(self, domain=None, fields=None, offset=0, limit=None, order=None):
        """
        Performs a ``search()`` followed by a ``read()``.

        :param domain: Search domain, see ``args`` parameter in ``search()``. Defaults to an empty domain that will match all records.
        :param fields: List of fields to read, see ``fields`` parameter in ``read()``. Defaults to all fields.
        :param offset: Number of records to skip, see ``offset`` parameter in ``search()``. Defaults to 0.
        :param limit: Maximum number of records to return, see ``limit`` parameter in ``search()``. Defaults to no limit.
        :param order: Columns to sort result, see ``order`` parameter in ``search()``. Defaults to no sort.
        :return: List of dictionaries containing the asked fields.
        :rtype: List of dictionaries.

        """
        pass

    @api.multi
    def toggle_active(self):
        """ Inverse the value of the field ``active`` on the records in ``self``. """
        pass







    @api.multi
    def export_data(self, fields_to_export, raw_data=False):
        """ Export fields for selected objects

            :param fields_to_export: list of fields
            :param raw_data: True to return value in native Python type
            :rtype: dictionary with a *datas* matrix

            This method is used when exporting data via client menu
        """
        pass

    @api.model
    def load(self, fields, data):
        """
        Attempts to load the data matrix, and returns a list of ids (or
        ``False`` if there was an error and no id could be generated) and a
        list of messages.

        The ids are those of the records created and saved (in database), in
        the same order they were extracted from the file. They can be passed
        directly to :meth:`~read`

        :param fields: list of fields to import, at the same index as the corresponding data
        :type fields: list(str)
        :param data: row-major matrix of data to import
        :type data: list(list(str))
        :returns: {ids: list(int)|False, messages: [Message]}
        """
        pass

        


    @api.model
    def fields_get_keys(self):
        pass


    @api.model
    def user_has_groups(self, groups):
        """Return true if the user is member of at least one of the groups in
        ``groups``, and is not a member of any of the groups in ``groups``
        preceded by ``!``. Typically used to resolve ``groups`` attribute in
        view and model definitions.

        :param str groups: comma-separated list of fully-qualified group
            external IDs, e.g., ``base.group_user,base.group_system``,
            optionally preceded by ``!``
        :return: True if the current user is a member of one of the given groups
            not preceded by ``!`` and is not member of any of the groups
            preceded by ``!``
        """
        pass



    @classmethod
    def clear_caches(cls):
        """ Clear the caches

        This clears the caches associated to methods decorated with
        ``tools.ormcache`` or ``tools.ormcache_multi``.
        """
        pass



    @api.model
    def get_empty_list_help(self, help):
        """ Generic method giving the help message displayed when having
            no result to display in a list or kanban view. By default it returns
            the help given in parameter that is generally the help message
            defined in the action.
        """
        pass

    @api.multi
    #@api.returns(None, lambda value: value[0])
    def copy_data(self, default=None):
        """
        Copy given record's data with all its fields values

        :param default: field values to override in the original values of the copied record
        :return: list with a dictionary containing all the field values
        """
        pass

    @api.multi
    def copy_translations(old, new):
        pass

    @api.multi
    #@api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        """ copy(default=None)

        Duplicate record ``self`` updating it with default values

        :param dict default: dictionary of field values to override in the
               original values of the copied record, e.g: ``{'field_name': overridden_value, ...}``
        :returns: new record

        """
        pass

    @api.multi
    #@api.returns('self')
    def exists(self):
        """  exists() -> records

        Returns the subset of records in ``self`` that exist, and marks deleted
        records as such in cache. It can be used as a test on records::

            if record.exists():
                ...

        By convention, new records are returned as existing.
        """
        pass

    @api.multi
    def get_external_id(self):
        """Retrieve the External ID of any database record, if there
        is one. This method works as a possible implementation
        for a function field, to be able to add it to any
        model object easily, referencing it as ``Model.get_external_id``.

        When multiple External IDs exist for a record, only one
        of them is returned (randomly).

        :return: map of ids to their fully qualified XML ID,
                 defaulting to an empty string when there's none
                 (to be usable as a function field),
                 e.g.::

                     { 'id': 'module.ext_id',
                       'id2': '' }
        """
        pass

    # Transience
    @classmethod
    def is_transient(cls):
        """ Return whether the model is transient.

        See :class:`TransientModel`.

        """
        pass

    @api.model
    def resolve_2many_commands(self, field_name, commands, fields=None):
        """ Serializes one2many and many2many commands into record dictionaries
            (as if all the records came from the database via a read()).  This
            method is aimed at onchange methods on one2many and many2many fields.

            Because commands might be creation commands, not all record dicts
            will contain an ``id`` field.  Commands matching an existing record
            will have an ``id``.

            :param field_name: name of the one2many or many2many field matching the commands
            :type field_name: str
            :param commands: one2many or many2many commands to execute on ``field_name``
            :type commands: list((int|False, int|False, dict|False))
            :param fields: list of fields to read from the database, when applicable
            :type fields: list(str)
            :returns: records in a shape similar to that returned by ``read()``
                (except records may be missing the ``id`` field if they don't exist in db)
            :rtype: list(dict)
        """
        pass

    def browse(self, arg=None, prefetch=None):
        """ browse([ids]) -> records

        Returns a recordset for the ids provided as parameter in the current
        environment.

        Can take no ids, a single id or a sequence of ids.
        """
        pass

    @property
    def ids(self):
        """ List of actual record ids in this recordset (ignores placeholder
        ids for records to create)
        """
        pass

    def ensure_one(self):
        """ Verifies that the current recorset holds a single record. Raises
        an exception otherwise.
        """
        pass

    def with_env(self, env):
        """ Returns a new version of this recordset attached to the provided
        environment

        .. warning::
            The new environment will not benefit from the current
            environment's data cache, so later data access may incur extra
            delays while re-fetching from the database.
            The returned recordset has the same prefetch object as ``self``.

        :type env: :class:`~odoo.api.Environment`
        """
        pass

    def sudo(self, user=SUPERUSER_ID):
        """ sudo([user=SUPERUSER])

        Returns a new version of this recordset attached to the provided
        user.

        By default this returns a ``SUPERUSER`` recordset, where access
        control and record rules are bypassed.

        .. note::

            Using ``sudo`` could cause data access to cross the
            boundaries of record rules, possibly mixing records that
            are meant to be isolated (e.g. records from different
            companies in multi-company environments).

            It may lead to un-intuitive results in methods which select one
            record among many - for example getting the default company, or
            selecting a Bill of Materials.

        .. note::

            Because the record rules and access control will have to be
            re-evaluated, the new recordset will not benefit from the current
            environment's data cache, so later data access may incur extra
            delays while re-fetching from the database.
            The returned recordset has the same prefetch object as ``self``.

        """
        pass

    def with_context(self, *args, **kwargs):
        """ with_context([context][, **overrides]) -> records

        Returns a new version of this recordset attached to an extended
        context.

        The extended context is either the provided ``context`` in which
        ``overrides`` are merged or the *current* context in which
        ``overrides`` are merged e.g.::

            # current context is {'key1': True}
            r2 = records.with_context({}, key2=True)
            # -> r2._context is {'key2': True}
            r2 = records.with_context(key2=True)
            # -> r2._context is {'key1': True, 'key2': True}

        .. note:

            The returned recordset has the same prefetch object as ``self``.
        """
        pass

    def with_prefetch(self, prefetch=None):
        """ with_prefetch([prefetch]) -> records

        Return a new version of this recordset that uses the given prefetch
        object, or a new prefetch object if not given.
        """
        pass

    def mapped(self, func):
        """ Apply ``func`` on all records in ``self``, and return the result as a
            list or a recordset (if ``func`` return recordsets). In the latter
            case, the order of the returned recordset is arbitrary.

            :param func: a function or a dot-separated sequence of field names
                (string); any falsy value simply returns the recordset ``self``
        """
        pass

    def filtered(self, func):
        """ Select the records in ``self`` such that ``func(rec)`` is true, and
            return them as a recordset.

            :param func: a function or a dot-separated sequence of field names
        """
        pass

    def sorted(self, key=None, reverse=False):
        """ Return the recordset ``self`` ordered by ``key``.

            :param key: either a function of one argument that returns a
                comparison key for each record, or a field name, or ``None``, in
                which case records are ordered according the default model's order

            :param reverse: if ``True``, return the result in reverse order
        """
        pass

    @api.multi
    def update(self, values):
        """ Update the records in ``self`` with ``values``. """
        pass

    #
    # New records - represent records that do not exist in the database yet;
    # they are used to perform onchanges.
    #

    @api.model
    def new(self, values={}, ref=None):
        """ new([values]) -> record

        Return a new record instance attached to the current environment and
        initialized with the provided ``value``. The record is *not* created
        in database, it only exists in memory.

        One can pass a reference value to identify the record among other new
        records. The reference is encapsulated in the ``id`` of the record.
        """
        pass

    @api.model
    def refresh(self):
        """ Clear the records cache.

            .. deprecated:: 8.0
                The record cache is automatically invalidated.
        """
        pass

    @api.model
    def invalidate_cache(self, fnames=None, ids=None):
        """ Invalidate the record caches after some records have been modified.
            If both ``fnames`` and ``ids`` are ``None``, the whole cache is cleared.

            :param fnames: the list of modified fields, or ``None`` for all fields
            :param ids: the list of modified record ids, or ``None`` for all
        """
        pass

    @api.multi
    def modified(self, fnames):
        """ Notify that fields have been modified on ``self``. This invalidates
            the cache, and prepares the recomputation of stored function fields
            (new-style fields only).

            :param fnames: iterable of field names that have been modified on
                records ``self``
        """
        pass

    @api.model
    def recompute(self):
        """ Recompute stored function fields. The fields and records to
            recompute have been determined by method :meth:`modified`.
        """
        pass

    @api.multi
    def onchange(self, values, field_name, field_onchange):
        """ Perform an onchange on the given field.

            :param values: dictionary mapping field names to values, giving the
                current state of modification
            :param field_name: name of the modified field, or list of field
                names (in view order), or False
            :param field_onchange: dictionary mapping field names to their
                on_change attribute
        """
        pass

        pass

