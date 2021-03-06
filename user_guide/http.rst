HTTP
====

The Jax JavaScript HTTP Library has its own built-in component to handle HTTP requests
and responses. The main ``send()`` method is:

* ``jax.http.send(url, options)``

And the alias methods to send specific request methods are respectively:

* ``jax.http.get(url, options)``
* ``jax.http.head(url, options)``
* ``jax.http.options(url, options)``
* ``jax.http.post(url, options)``
* ``jax.http.put(url, options)``
* ``jax.http.delete(url, options)``

The options object can accept the the following properties:

* ``method``

  - The method to use, GET, POST, etc. (defaults to GET)

* ``headers``

  - Additional request headers to send

* ``username``

  - A username, if required

* ``password``

  - A password, if required

* ``async``

  - Boolean flag to allow asynchronous operation

* ``data``

  - Array or object of values to send over in the request

* ``type``

  - Force a specific content-type from the response (will auto-detect otherwise)

* ``status``

  - An object of status-based function handlers that will trigger based on the status of the return response

* ``progress``

  - An function to trigger on the download (GET) or upload (POST) progress of a request

* ``trace``

  - Push the response into a trace/debug function

* ``fields``

  - Boolean flag to manage and set CSV field names from the first row of data

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

Using the built-in auto-detect content feature, you can easily get a data object parsed from a URL
with a specific content-type:

**JSON content:**

.. code-block:: javascript

    var json = jax.get('/test.json');

**CSV content:**

.. code-block:: javascript

    var csv = jax.get('/test.csv', {"fields" : true});

**XML content:**

.. code-block:: javascript

    var xml = jax.get('/test.xml');

Check HTTP Status Check
-----------------------

You can check a URL and get back only status information on it by using the HTTP status methods:

* ``jax.http.status(url)``
* ``jax.http.isSuccess(url)``
* ``jax.http.isRedirect(url)``
* ``jax.http.isError(url)``

.. code-block:: javascript

    if (jax.http.getStatus('http://www.mydomain.com/') == 200) {
        console.log('The URL is OK');
    }
