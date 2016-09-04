import os
import urllib.request
#3001-6000
#maxValue = 3001
#page = list(range(2808,maxValue))

#创建文件夹
fileName = "dnc_emalis_collection"
files = os.listdir('.\\')
if fileName not in files:
    os.mkdir(".\\"+fileName)
basePath = ".\\"+fileName

i = 9000
url = "https://wikileaks.org/dnc-emails//get/%s" % i
f = urllib.request.urlopen(url)
content = f.read()
file = open(basePath+"\\"+"%s.txt"%i, "wb")
file.write(content)
#file.flush()
print(i)
file.close()
