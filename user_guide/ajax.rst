AJAX
====

The Jax JavaScript Library has its own built-in component to handle AJAX requests
and responses. When performing an AJAX request, you will pass the URL just an object
that accepts the the following properties:

* ``method``

  - The method to use, GET, POST, etc. (defaults to GET)

* ``async``

  - Boolean flag to allow asynchronous operation

* ``data``

  - Array or object of values to send over in the request

* ``headers``

  - Additional request headers to send

* ``status``

  - An object of status-based function handlers that will trigger based on the status of the return response

* ``fields``

  - Boolean flag to manage CSV field names

* ``type``

  - Force a specific content type from the response (will auto-detect otherwise)

* ``delim``

  - Force a specific delimiter for CSV data

* ``trace``

  - Push the response into a trace/debug function

Here's a basic GET call to a URL:

.. code-block:: javascript

    var text = jax.ajax('http://www.mydomain.com/text');


Shorthand Methods
-----------------

