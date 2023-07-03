#!/usr/bin/env python
# to run me: py P:/ath/to/this/file.py

import requests, sys
try:
    inputurl = sys.argv[1]
    subargs = sys.argv[2:]
    # print(inputurl, subargs)
except:
    print('---caution: ONLY use with urls/files you trust---')
    inputurl = input('paste the GitHub url below:\n> ')
rawpyurl = inputurl.replace('github.com', 'raw.githubusercontent.com').replace('/blob', '')
rawpycode = requests.get(rawpyurl)
exec(rawpycode.text)