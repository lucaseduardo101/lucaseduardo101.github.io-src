#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Lucas Oliveira'
SITENAME = 'Lucas Oliveira'
SITEURL = ''
THEME = 'pelican-themes/Flex'

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'
SITEURL = 'http://localhost:8000/'
SITELOGO = SITEURL + '/profile.png'

DEFAULT_LANG = 'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True


MENUITEMS = (
    ('About', '/pages/about.html'),
    ('Blog', '/category/blog.html'),
    ('Email', 'http://www.google.com/recaptcha/mailhide/d?...'),
    ('Vita', '/pdfs/HouserCV.pdf')
    )


# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/lucas-oliveira-711b712a/'),
          ('github', 'https://github.com/lucaseduardo101'),
          ('twitter', 'https://twitter.com/lukseduardo101'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True