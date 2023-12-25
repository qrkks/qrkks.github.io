# AUTHOR = 'pp'
SITENAME = 'Trading Site Building Journal'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'zh'

DATE_FORMATS = {
    'en': '%a, %d %b %Y',
    'zh': '%Y年%m月%d日 %A %H:%M',
}

THEME = './themes/myidea'

STATIC_PATHS = ['images', 'static']


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Ciyetrading", "https://ciyetrading.com/"),
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
)

# Social widget
SOCIAL = (
    # ("Email", "mailto:qrkks3@gmail.com"),
    # ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Basic settings
USE_FOLDER_AS_CATEGORY = False
DISPLAY_CATEGORIES_ON_MENU = True
DEFAULT_CATEGORY = '杂项'

# 输出文件夹
OUTPUT_PATH = 'output/'
DELETE_OUTPUT_DIRECTORY = False

DEFAULT_DATE_FORMAT = '%Y-%m-%d'


ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'


# Plugin settings
IMAGE_PROCESS = {
    "article-image": ["scale_in 300 300 True"],
    "thumb": ["crop 0 0 50% 50%", "scale_out 150 150 True", "crop 0 0 150 150"],
}

SITEMAP = {
    "exclude": [
        "^/noindex/",  # starts with "/noindex/"
        "/tag/",       # contains "/tag/"
        "\.json$",     # ends with ".json"
    ]
}

# pelicanconf.py or publishconf.py
# SEO_REPORT = True  # SEO report is enabled by default
# SEO_ENHANCER = False  # SEO enhancer is disabled by default
# SEO_ENHANCER_OPEN_GRAPH = False # Subfeature of SEO enhancer
# SEO_ENHANCER_TWITTER_CARDS = False # Subfeature of SEO enhancer
