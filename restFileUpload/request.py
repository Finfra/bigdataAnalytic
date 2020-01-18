#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests as req
import os
filename=os.getcwd()+'/'+'files/a.txt'
files = {'myfile': open(filename,'rb')}
url="http://127.0.0.1:8080/upload"
response = req.post(url, files=files )

