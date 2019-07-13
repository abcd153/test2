import urllib.request
import re
pat='<div class="name">(.*?)</div><div class="works-num">'
data=urllib.request.urlopen("https://read.douban.com/provider/all").read()
data=data.decode("utf_8")
result=re.compile(pat).findall(str(data))
print(result)
f=open("F:/Pythontest1/python.txt","w")
for i in range(0,len(result)):
    f.write(result[i]+'/n')
f.close()
