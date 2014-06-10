# -*- coding:  utf-8 -*-
from __future__ import unicode_literals

AUTHOR = 'Shreesh Ayachit'
SITENAME = "char stream"
SITEURL = 'http://shreesh.in'
TIMEZONE = "America/New_York"
THEME = "./pelican-theme"

GITHUB_URL = 'http://github.com/shreeshga/'
PDF_GENERATOR = False
REVERSE_CATEGORY_ORDER = True
DEFAULT_PAGINATION = 4
DEFAULT_DATE = (2012, 3, 2, 14, 1, 1)

FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

#LINKS = (('Biologeek', 'http://biologeek.org'),
#         ('Zubin Mithra', "http://zubin71.wordpress.com/"),)

SOCIAL = (('twitter', 'http://twitter.com/shreeshga'),
          ('github', 'http://github.com/shreeshga'),
          ('quora','https://www.quora.com/Shreesh-Ayachit'),
          ('plus','https://plus.google.com/107491169271722959755/'))

# static paths will be copied under the same name
STATIC_PATHS = ["pictures","images"]

# A list of files to copy from the source to the destination
#FILES_TO_COPY = (('extra/robots.txt', 'robots.txt'),)

FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)'
DATE_FORMATS = {
    'en': '%a, %d %b %Y'
    }
