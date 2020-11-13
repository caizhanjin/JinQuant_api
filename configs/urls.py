# encoding: utf-8

from utils.urlparse import include, url_wrapper

urls_patterns = url_wrapper([
    (r"/users", include('apps.resful.urls')),
    (r"/test", include('apps.test.urls')),
])
