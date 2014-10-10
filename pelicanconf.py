#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from fontawesome_markdown import FontAwesomeExtension
import os

AUTHOR = u"Erwin Sterrenburg"
SITENAME = u"PILOSA.EU"
TAGLINE = 'Scribblings of World\'s Most Curious Anteater'
TIMEZONE = 'Europe/Amsterdam'
LOCALE='en_US.utf8'
DEFAULT_LANG = u'en'

DEFAULT_PAGINATION = 5

# By default we enable pretty highlighing in markdown:
MD_EXTENSIONS = [FontAwesomeExtension(), 'codehilite(css_class=highlight,linenums=False)', 'extra', 'toc']

# Leave this blank for local development, publishconf.py has the "real" value:
SITEURL = ''
RELATIVE_URLS = True

# Feed generation is usually not desired when developing
FEED_ALL_RSS = 'feed.xml'
CATEGORY_FEED_RSS = None
TRANSLATION_FEED_RSS = None
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
FEED_DOMAIN = SITEURL

MENUITEMS = [('Archive', 'archives.html'), ('About', 'about.html'),]
SOCIAL = (
    ('envelope-o', 'mailto:ewsterrenburg@gmail.com'),
    ('github', 'https://github.com/ewsterrenburg/'),
    ('linkedin', 'https://www.linkedin.com/in/ewsterrenburg'),
    ('rss', FEED_ALL_RSS),
)



# Static files
# Uncomment and set to the filename of your favicon:
FAVICON_FILENAME = 'favicon.ico'

# Any extra files should be added here
#STATIC_PATHS = ['images', 'extra/CNAME']
STATIC_PATHS = [
    'images',
    os.path.join('extras','robots.txt'),
    'extras/CNAME',
    'extras/favicon.ico',
    'extras/apple-touch-icon.png'
    ]

# Here's a sample EXTRA_PATH_METADATA that adds the favicon, an iOS touch icon and a GPG key:
EXTRA_PATH_METADATA = dict()
for f in os.listdir('content/extras'):
    STATIC_PATHS.append('extras' + os.sep + '{0}'.format(f))
    EXTRA_PATH_METADATA['extras' + os.sep + '{0}'.format(f)]={'path': f}



#Theme
THEME = os.path.join(os.getcwd(), "themes", "pure-single-master")
COVER_IMG_URL = "/images/bananas.jpeg"
SINGLE_AUTHOR = True
# Sole author and don't use categories ... disable these features
AUTHOR_SAVE_AS = False
AUTHORS_SAVE_AS = False


DISPLAY_CATEGORIES_ON_MENU = False
DEFAULT_DATE_FORMAT = ('%b %d %Y')
TYPOGRIFY = True

# Cleaner page links
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
PAGE_LANG_URL = '{slug}-{lang}.html'
PAGE_LANG_SAVE_AS = '{slug}-{lang}.html'

# Cleaner Articles
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

PLUGIN_PATHS = [os.path.join(os.getcwd(), "..", "pelican-plugins")]
#PLUGINS = ['render_math', 'extended_sitemap', 'better_codeblock_line_numbering']
PLUGINS = ['extended_sitemap', 'better_codeblock_line_numbering']

TAG_CLOUD_STEPS = 4

# Setting for the better_figures_and_images plugin
RESPONSIVE_IMAGES = True
