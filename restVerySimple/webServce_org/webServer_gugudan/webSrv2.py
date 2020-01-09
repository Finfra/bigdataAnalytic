# httpd.py
from BaseHTTPServer import HTTPServer
from CGIHTTPServer import CGIHTTPRequestHandler
import os

#os.chdir("/xxx")
serv = HTTPServer(("", 9050), CGIHTTPRequestHandler)
serv.serve_forever()

