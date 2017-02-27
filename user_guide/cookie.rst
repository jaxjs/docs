Cookie
======

The Jax JavaScript Library has a ``cookie`` object that helps to manage cookie values
for the user client.

Storing
-------

You can store a cookie using the method below. Accepted option object properties
are ``expire``, ``domain`` and ``path``.

.. code-block:: javascript

    jax.cookie.save('foo', 'bar', {"expire" : 300});

Retrieving
----------

Then you can access the cookie value like this:

.. code-block:: javascript

    var foo = jax.cookie.load('foo');

Deleting
--------

And remove the cookie value like this:

.. code-block:: javascript

    jax.cookie.remove('foo');
