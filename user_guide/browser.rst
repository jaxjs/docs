Browser
=======

The Jax JavaScript HTTP Library has a ``browser`` object that helps to get browser-specific
information from the user client and handle specific browser-related functions.

Open a New Window
-----------------

You can open a new browser window using the method below. Accepted option object properties
are:

* ``width``
* ``height``
* ``scroll``
* ``resize``
* ``status``
* ``location``
* ``menu``
* ``tool``
* ``x``
* ``y``

.. code-block:: javascript

    jax.browser.open('http://www.domain.com/', 'my-popup', {"with" : 640, "height" : 480});

Routing Based on Device
-----------------------

You can route to a specific URL based on the device detected. You can set the ``desktop`` URL property,
the ``mobile`` URL property for a all-inclusive mobile URL, or you can set a device-specific URL property

.. code-block:: javascript

    var options = {
        "desktop" : 'http://www.mydomain.com/',
        "ipad"    : 'http://www.mydomain.com/ipad',
        "iphone"  : 'http://www.mydomain.com/iphone',
        "android" : 'http://www.mydomain.com/android',
    }
    jax.browser.route(options);
