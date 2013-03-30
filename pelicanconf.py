#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'me'
SITENAME = u'Pelican DEMO'
SITEURL = 'http://soulne4ny.github.com/pelican-demo'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Blogroll
LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
          ('Python.org', 'http://python.org'),
          ('Jinja2', 'http://jinja.pocoo.org'),
)

# Social widget
SOCIAL = (('LDN', 'http://ldn.lv'),
          ('Another social link', '#'),)

FILENAME_METADATA = ('(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)')

THEME = 'bootstrap2'

FILES_TO_COPY = (
    ('/dev/null', '.nojekyll'),
)


DEFAULT_PAGINATION = 3
