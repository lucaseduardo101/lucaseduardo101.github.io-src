#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Lucas Oliveira'
SITENAME = 'Lucas Oliveira'
SITEURL = ''
THEME = 'pelican-themes/Flex'

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'
SITEURL = 'https://lucaseduardo101.github.io/'
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
    ('Email', 'http://www.google.com/recaptcha/mailhide/d?...'),
    ('Vita', '/pdfs/HouserCV.pdf')
    )


# Blogroll
LINKS = (('Blog', '/category/blog.html'),
         ('Boas práticas', '/tag/boas-praticas.html'),
         ('Exemplos de código', '/tag/exemplos-de-codigo.html'),
         ('Java', '/tag/java.html'),
         ('Kafka', '/tag/kafka'),
         ('Micronaut', '/tag/micronaut.html'),         
         ('SQL', '/tag/sql.html'),                        
         ('Docker', '/tag/docker.html'),
         ('Kotlin', '/tag/kotlin.html'),         
         )
         

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/lucas-oliveira-711b712a/'),
          ('github', 'https://github.com/lucaseduardo101'),
          ('twitter', 'https://twitter.com/lukseduardo101'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True