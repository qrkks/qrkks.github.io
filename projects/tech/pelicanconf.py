# from .custom_func.filters import format_date_zh

# AUTHOR = 'pp'
SITENAME = 'Python Website Building Learning Journal'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'zh'

DATE_FORMATS = {
    'en': '%a, %d %b %Y',
    'zh': '%Y-%m-%d',
}

# JINJA_FILTERS = {
    # 'format_date_zh': format_date_zh
# }


THEME = './themes/simple'

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

SUMMERY_MAX_LENGTH = 150 # 如果未显式指定给定帖子的摘要元数据，则 SUMMARY_MAX_LENGTH 设置可用于指定从文章开头开始有多少单词用作摘要。

# 输出文件夹
OUTPUT_PATH = 'output/'
DELETE_OUTPUT_DIRECTORY = False

DEFAULT_DATE_FORMAT = '%Y-%m-%d'


ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'


# Plugin settings
PLUGINS = [
    'obsidian',
]

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

# SUBTITLE = 'Papyrus'
# SUBTEXT = '''A fast and responsive theme built for the
# <a href="https://blog.getpelican.com/">Pelican</a> site generator.<br>
# The theme is inspired by <a href="https://github.com/adityatelange/hugo-PaperMod">Hugo-PaperMod</a>.
# It is styled using <a href="https://tailwindcss.com/">Tailwind CSS</a>.
# It supports dark mode and built in search function.
# '''
# COPYRIGHT = '©2022'
# PLUGIN_PATHS = ['pelican-plugins']
# PLUGINS = ['readtime', 'search', 'neighbors', 'pelican-toc']
# STATIC_PATHS = [
#     'images',
#     'images/favicon.ico',
#     'extra/robots.txt',
# ]
# EXTRA_PATH_METADATA = {
#     'extra/robots.txt': {'path': 'robots.txt'},
#     'images/favicon.ico': {'path': 'favicon.ico'},
# }
# DISPLAY_PAGES_ON_MENU = True
# DIRECT_TEMPLATES = (('index', 'search', 'tags', 'categories', 'archives',))
# PAGINATED_TEMPLATES = {'index': None, 'tag': None,
#                        'category': None, 'author': None, 'archives': 24, }

# # Site search plugin
# SEARCH_MODE = "output"
# SEARCH_HTML_SELECTOR = "main"
# # Table of Content Plugin
# TOC = {
#     'TOC_HEADERS': '^h[1-3]',  # What headers should be included in
#     # the generated toc
#     # Expected format is a regular expression
#     'TOC_RUN': 'true',    # Default value for toc generation,
#     # if it does not evaluate
#     # to 'true' no toc will be generated
#     'TOC_INCLUDE_TITLE': 'false',    # If 'true' include title in toc
# }

# # Feed generation is usually not desired when developing
# FEED_ALL_ATOM = 'feeds/all.atom.xml'
# CATEGORY_FEED_ATOM = None
# TRANSLATION_FEED_ATOM = None
# AUTHOR_FEED_ATOM = None
# AUTHOR_FEED_RSS = None
# RSS_FEED_SUMMARY_ONLY = True

# # Social widgets
# SOCIAL = (
#     ('github', 'https://github.com/aleylara/Papyrus/'),
#     ('twitter', 'https://twitter.com/'),
# )

# # Article share widgets
# SHARE = (
#     ("twitter", "https://twitter.com/intent/tweet/?text=Features&amp;url="),
#     ("linkedin", "https://www.linkedin.com/sharing/share-offsite/?url="),
#     ("reddit", "https://reddit.com/submit?url="),
#     ("facebook", "https://facebook.com/sharer/sharer.php?u="),
#     ("whatsapp", "https://api.whatsapp.com/send?text=Features - "),
#     ("telegram", "https://telegram.me/share/url?text=Features&amp;url="),
# )
