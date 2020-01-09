import urllib
url = 'http://localhost:9997/getString'
u = urllib.urlopen(url)
data = u.read()# u is a file-like object
j=eval(data)
print "%s,%s"%(j["x"],j["y"])
