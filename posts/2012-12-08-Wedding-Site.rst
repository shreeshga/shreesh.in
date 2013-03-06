.. title:: The art of creating wedding invitations
.. author:: Shreesh
.. time::  00:34
.. updated:: Sun Dec  12 19:27:30 2012
.. timezone:: UTC
.. feed:: all
.. copyright:: Creative Commons Attribution 3.0 Unported

The art of creating wedding invitations
=========================================
Turns out; I am getting married. So, I wanted to create a web site instead of
mailing everyone with a Megabytes of scanned invitation [I know, not very Indian of me].

Being a  programmer, using e-wedding or such other hosting sites is wholly
*unacceptable*.

I had worked with Python Flask before, so I quickly put together a static site 
using the Flask-Bootstrap-Responsive_ plugin [see? How easily I  put together
a site with best of the breed] and threw it in my AWS micro instance.


I had the idea of creating a joint-timeline of Prerna & me, with special
moments along with some pictures. Turns out Facebook has the feature in "See
Friendship" [who knew?]. I found an awesome js library `TimelineJS
<http://timeline.verite.co/>`_ which reads data from  published Google
spreadsheet, parses the data and displays a nice timeline of events.

So, We both started filling in the event details in a shared Google drive `Spreadsheet <https://docs.google.com/spreadsheet/pub?key=0AtNxSwigiymodHR5ZEFnOUN0T3ZhUWJNRWEzTXFJemc&single=true&gid=0&output=html>`_. 
I, for the most part, edited the sheet from the Android Google *Drive App*.


I wanted to have a message board to get people to leave  a message. 
[I hate the guest book feature which is essentially a text box and submit
button] Sadly, Google+ does not yet support a writable comment box plugin. 
So, went with the least desirable FB comment box.


TL;DR: `HDFU <http://www.youtube.com/watch?v=unkIVvjZc9Y>`_ and write your own
wedding site.

Also, `Wedding! <http://prerna.shreesh.in>`_

.. _Flask-Bootstrap-Responsive: https://github.com/mbr/flask-bootstrap
