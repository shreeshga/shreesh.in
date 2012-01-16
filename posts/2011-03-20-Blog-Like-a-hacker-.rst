.. title:: Blog Like a hacker 
.. author:: Shreesh
.. updated:: 2011-03-20 05:23
.. timezone:: UTC
.. feed:: all
.. copyright:: Creative Commons Attribution 3.0 Unported


Blogging with Wordpress
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Even though I am not the chatter box, there were times when I wanted to blog about experiences. But
every time I opened the web console, it did not give the same kick as typing in a Vim editor with
dark background and glowing text. So, whenever I felt to talk about something, I just posted it as a
summary in relevant online forums rather than type it as a blog.

Blog like a hacker 
-----------------------------

Did I mention I liked the kick of typing in Vim and publishing from command line? yes, thats what
made me throw out Wordpress and its associated plugins in favour of a static site with hand coded
[but inspired] layout, comment-less, plugin-less blog site. [Hyde][1] suited my tastes perfectly.
Its a static site generation engine written in Python, uses Django style templating and I can use
markdown syntax to type the content. Its clean and you can blog offline and push your changes to the
serve with a single command using [Fabric][2]

Vim as an editor
----------------------------
 
Having worked with Vim editor on and off for a good 4 years, It beats any IDE. With markdown and
spell check, its as good a blog editor as any. With no repetitive mouse movements, its better for
your wrists. 


Migrating from Wordpress
----------------------------

With a csv exporter plugin, I got anice csv file with all my posts[However little there are].
What wasn't so nice was the horrible html code of my text content. With fugly tags obscuring the content I could not work with it in a normal
editor. There is a wonderful piece of python script [html2text][3], which converts a html text to
Markdown-formatted text complete with link references at the end. [1]:
https://github.com/lakshmivyas/hyde (Hyde Static Website generator) [2]: http://fabfile.org/ (Fabric
- Application deployment) [3]: https://github.com/aaronsw/html2text (HTML to Markdown-formatted
text)

