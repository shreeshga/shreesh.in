.. This is a comment (note the lack of a trailing double colon).

.. time:: HH:MM
.. The timezone must be supported by PyTZ
.. timezone:: UTC
.. author:: Your Name Here
.. updated:: YYYY-mm-dd HH:MM

.. All is not a special feed.  Content must be added to 'all' just like any
.. other feed.
.. feed:: all

.. copyright:: Creative Commons Attribution 3.0 Unported

Write Your First Post
=====================

Firmant uses the wonderful `reStructuredText <http://docutils.sourceforge.net/rst.html>`_
text markup language.

Creating Posts
--------------

Posts go into the ``posts`` directory with a filename of the same form as this
file.  The date in ``YYYY-mm-dd`` form is combined with the post slug by a
dash/minus/ASCII 0x2D (whatever you wish to call it) to create the filename.
For instance, ``posts/2010-08-12-firmant-sample-post.rst``

This post can serve as a good template for your site.

Adding Posts to Feeds
---------------------

Feeds are added with the feed directive.  This does not have to happen in the
header of the document.

.. feed:: anywhere-feed
