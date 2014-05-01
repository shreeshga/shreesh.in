:title: Share files from commandline
:timezone: UTC
:author: shreesh
:copyright: Creative Commons Attribution 3.0 Unported
:category: tech

How do you share a short temporary file right from your commandline instead
unnecessary mouse clicks on a browser?

* setup a developer account at `filepicker.io <http://filepicker.io>`_
* Get the API key
* in terminal, cd to the directory where you have the file.

.. code::

  curl -F fileUpload=@<filename> 'https://www.filepicker.io/api/<path>?key=<apikey>&filename=<filename>'

| The response will have the uploaded file path.
| IM the path to friend.
| Done.
