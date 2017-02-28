AJAX
====

The Jax JavaScript Library has its own built-in component to handle AJAX requests
and responses. The basic API is:

* ``jax.ajax(url, options)``
* ``jax.get(url, options)``
* ``jax.post(url, options)``

The ``get()`` and ``post()`` methods above are simply shorthand methods for those
request methods. The options object can accept the the following properties:

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

* ``type``

  - Force a specific content type from the response (will auto-detect otherwise)

* ``fields``

  - Boolean flag to manage and set CSV field names

* ``delim``

  - Force a specific delimiter for CSV data

* ``trace``

  - Push the response into a trace/debug function

Here's a basic GET call to a URL:

.. code-block:: javascript

    var text = jax.ajax('/test.txt', {
        "status" : {
            "200" : function(response) {
                console.log(response.text);
            }
        }
    });

If you wanted to control what happened on an error, you could set the status to:

.. code-block:: javascript

    var text = jax.ajax('/test.txt', {
        "status" : {
            "200" : function(response) {
                console.log(response.text);
            },
            "404" : function(response) {
                console.log('Whoops, something bad happened.');
            }
        }
    });

Auto-Detect Content
-------------------

Using the built-in auto-detect content feature, you can easily get a JSON object from a URL that
sends JSON content:

.. code-block:: javascript

    var json = jax.get('/test.json');


HTTP Status Methods
-------------------

You can check a URL and get back status information on it by using the HTTP status methods:

* ``jax.http.getStatus(url)``
* ``jax.http.isSuccess(url)``
* ``jax.http.isRedirect(url)``
* ``jax.http.isError(url)``

.. code-block:: javascript

    if (jax.http.getStatus('http://www.mydomain.com/') == 200) {
        console.log('The URL is OK');
    }
