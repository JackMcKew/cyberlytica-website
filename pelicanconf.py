#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Jack McKew'
SITENAME = 'Cyberlytica'
SITETITLE = SITENAME
# SITEURL = 'http://localhost:8000'
# SITEURL = 'https://vibrant-mayer-d513c6.netlify.com'
SITEURL = 'https://cyberlytica.com.au'
# EXTRA_PATH_METADATA = {
#     'extra/favicon.ico': {'path': 'favicon.ico'},
# }

FAVICON = "/img/favicon.ico"

PATH = 'content'

THEME = './themes/basic'

TIMEZONE = 'Australia/Sydney'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

LINKS = (
    ("Home", "/#home"),
    ("About", "/#about"),
    ("Our Services", "/#services"),
    ('Feedback','/#feedback'),
    ("Team", "/#team"),
)

STATIC_PATHS = ['img']

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True