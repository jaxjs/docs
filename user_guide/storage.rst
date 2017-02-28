Storage
=======

The Jax JavaScript HTTP Library has a ``storage`` object that helps to manage local storage
values for the user client.

Storing
-------

You can store a value in local stroage using the method below:

.. code-block:: javascript

    jax.storage.save('foo', 'bar');

Retrieving
----------

Then you can access the value in storage like this:

.. code-block:: javascript

    var foo = jax.storage.load('foo');

Deleting
--------

And remove the value in storage like this:

.. code-block:: javascript

    jax.storage.remove('foo');
