import urllib
url = 'http://localhost:8080/getString'
u = urllib.urlopen(url)
data = u.read()# u is a file-like object
data2=eval(data)
#print data2["y"]
for i in data2:
    print("%s = %i"%(i,data2[i]))
