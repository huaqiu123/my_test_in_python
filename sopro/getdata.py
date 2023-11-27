import urllib
import os
import re
import zipfile
import requests
import bs4
import string
url="http://www.shuyy8.com/book/2034/"
res = requests.get(url)
try:
	res.raise_for_status()
except Exception as exc:
	print('There was a problem: %s' % (exc))
zip1 = bs4.BeautifulSoup(res.text)
url2=zip1.select('a[rel="nofollow"]')
print(url2)
url3=url2[0]
url4=url3.get('href')
print(url4)
DATA_DIR = './sopro/TextAnalyzer'
DATA_NAME = 'hlm.zip'
filename = DATA_NAME
filepath = os.path.join(DATA_DIR, filename)
n_url = urllib.parse.quote(url4, safe=string.printable).replace(" ", "%20")
print(n_url)
with zipfile.ZipFile(filepath, 'r') as zip:
    zip.extractall(DATA_DIR)
