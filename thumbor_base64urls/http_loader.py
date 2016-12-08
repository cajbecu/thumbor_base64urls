#!/usr/bin/python
# -*- coding: utf-8 -*-

import base64
from thumbor.loaders.http_loader import *
from thumbor.loaders.http_loader import _normalize_url

@return_future
def load(context, url, callback, normalize_url_func=_normalize_url):
    if url and url.startswith('base64'):
        url_base64=unquote(url).decode('utf8').split('base64:')[1]
        url = base64.b64decode(url_base64)

    load_sync(context, url, callback, normalize_url_func)