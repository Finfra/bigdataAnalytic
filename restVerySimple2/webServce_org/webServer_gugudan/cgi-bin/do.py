#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cgi
print "Content-Type: text/html"
print

form = cgi.FieldStorage()
dan=int(form["dan"].value)
print "<html>"
print '''<head><meta charset="utf-8" /></head>'''
print "<body border=1>"
print "<h1>%d 단 </h1>"% dan
print "    <table>"
for x in xrange(1,10):
    print "        <tr>"
    print "            <td>%d</td><td>X</td><td>%d</td><td>=</td><td>%d</td>"%(dan,x,x*dan)
    print "        </tr>"
print "    </table>"
print "</body>"
print "</html>"

