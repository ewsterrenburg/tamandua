#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from fontawesome_markdown import FontAwesomeExtension

AUTHOR = u"Erwin Sterrenburg"
SITENAME = u"My Sample Blog"
TAGLINE = 'Sample Tag Line'
TIMEZONE = 'Europe/Amsterdam'
LOCALE='en_US.utf8'
DEFAULT_LANG = u'en'

DEFAULT_PAGINATION = 5

# By default we enable pretty highlighing in markdown:
MD_EXTENSIONS = [FontAwesomeExtension(), 'codehilite(css_class=highlight)', 'extra', 'toc']

# Leave this blank for local development, publishconf.py has the "real" value:
SITEURL = 'http://ewsterrenburg.github.io/tamandua/'

FEED_ATOM = None
FEED_RSS = 'feeds/all.rss'
FEED_DOMAIN = SITEURL

MENUITEMS = [('Archive', 'archives.html'), ('About', 'about.html'),]
SOCIAL = (
    ('github', 'https://github.com/ewsterrenburg/'),
    ('linkedin', 'https://www.linkedin.com/in/ewsterrenburg'),
    ('rss', FEED_RSS),
)



# Static files
# Uncomment and set to the filename of your favicon:
FAVICON_FILENAME = 'favicon.ico'

# Any extra files should be added here
#STATIC_PATHS = ['images', 'extra/CNAME']
STATIC_PATHS = [
    'images',
    'extras/robots.txt',
    'extras/CNAME',
    'extras/favicon.ico',
    'extras/apple-touch-icon.png'
    ]

# Here's a sample EXTRA_PATH_METADATA that adds the favicon, an iOS touch icon and a GPG key:
EXTRA_PATH_METADATA = {
    'extras/robots.txt': {'path': 'robots.txt'},
    'extras/favicon.ico': {'path': 'favicon.ico'},
    'extras/apple-touch-icon.png': {'path': 'apple-touch-icon.png'},
    'extras/CNAME': {'path': 'CNAME'}
    }

#Theme
THEME = './themes/pure-single-master'
COVER_IMG_URL = "http://commoditychainsthatbind.files.wordpress.com/2013/03/bananas-925216.jpeg"
SINGLE_AUTHOR = True
DISPLAY_CATEGORIES_ON_MENU = False
DEFAULT_DATE_FORMAT = ('%b %m %Y')
TYPOGRIFY = True

# Cleaner page links
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
PAGE_LANG_URL = '{slug}-{lang}.html'
PAGE_LANG_SAVE_AS = '{slug}-{lang}.html'

# Cleaner Articles
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

PLUGIN_PATHS = ["/home/erwin/pelican/pelican-plugins"]
PLUGINS = ['render_math', 'extended_sitemap']

TAG_CLOUD_STEPS = 4
