#!/usr/bin/env python
# to run me on Windows: py P:/ath/to/this/file.py

import requests, sys
try:
    inputurl = sys.argv[1]
    subargs = sys.argv[2:]
except:
    inputurl = input('paste the GitHub url below:\n> ')
if '/WinnieSchLin/' in inputurl:
    rawpyurl = inputurl.replace('github.com', 'raw.githubusercontent.com').replace('/blob', '')
    rawpycode = requests.get(rawpyurl)
    exec(rawpycode.text)
else:
    print('\n--- This file can ONLY be used for code written by Winnie Schwaid-Lindner.\n--- If you would like help running code from other trusted sources,\n    please reach out to me at w@wn.ie\n')