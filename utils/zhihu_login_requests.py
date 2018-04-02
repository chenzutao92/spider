# -*- coding: utf-8 -*-

import requests
try:
    # 从本地获取cookie
    import cookielib # py2
except:
    import http.cookiejar as cookielib

import re

agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
