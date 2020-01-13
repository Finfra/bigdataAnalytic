import urllib
url = 'http://finfra.com:9000/getString'
u = urllib.urlopen(url)
data = u.read()# u is a file-like object
print data