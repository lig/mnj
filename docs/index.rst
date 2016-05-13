.. toctree::
   :hidden:

   examples
   contribute
   copying
   todo

Mongo Energy - Simple yet Powerful Python MongoDB Library and ODM
=================================================================

Mnj (Mongo Energy) is a Python library for working with `MongoDB <https://www.mongodb.com/>`_ in the most *pythonic* way possible.

Mnj consits of the three main layers:

* Python based DSL on top of the `PyMongo <https://api.mongodb.com/python/current/>`_-like syntax.
* Custom DSL operators implementing additional features which cover MongoDB best practices.
* ODM (Object Document Mapping) framework that defines document schema and provides a high level abstraction for the Mnj features. 

Mnj is licensed under :doc:`copying`.


Mnj DSL is handy
----------------

::

    books = col.find(q(
        author=regex_('Gibson', re.IGNORECASE),
        year=gte_(2003)
    ))

Mnj DSL can be used with any Python MongoDB driver if it is PyMongo compatible, including `Motor <https://github.com/mongodb/motor>`_ and `txmongo <https://github.com/twisted/txmongo>`_.

Still not convinced?☺ See :doc:`examples`.


Get Mnj
-------

Install
^^^^^^^

.. code-block:: shell

    pip install mnj


Source Code
^^^^^^^^^^^

`<https://github.com/lig/mnj>`_


Contribute
----------

Any contributions are always welcome! See :doc:`contribute`.
