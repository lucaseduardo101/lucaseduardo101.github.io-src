#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Lucas Oliveira'
SITENAME = 'Lucas Oliveira'
SITEURL = ''
THEME = 'pelican-themes/bootstrap'

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Linkedin', 'https://www.linkedin.com/in/lucas-oliveira-711b712a/'),
          ('Github', 'https://github.com/lucaseduardo101'),
          ('Twitter', 'https://twitter.com/lukseduardo101'))

DEFAULT_PAGINATION = 1

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True