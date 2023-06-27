#!/usr/bin/env python

import requests
rawpyurl = input('paste the github raw url below:\n> ')
rawpycode = requests.get(rawpyurl)
exec(rawpycode.text)