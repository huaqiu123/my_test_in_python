import requests
import bs4
import sys
import os
import logging
import copy
cwd=os.getcwd()
print(cwd)
cwd=cwd+'\\image'
print(len(sys.argv))
i=0

if len(sys.argv)<1:
    print("open url false")
else:
    url=sys.argv[1]
    s='https://xkcd.com'
    print(s)
    while   '#' not in url :
        print(url)
        response=requests.get(url)
        response.raise_for_status
        soup=bs4.BeautifulSoup(response.text,"html.parser")
        want=soup.select('a[rel="prev"]')
        preurl=want[0].get("href")
        file=open(cwd+'\\'+f'{i}'+'.png','wb')
        i_want=soup.select('#comic img')
        logging.debug(f"{i_want}")
        comicurl=sys.argv[1]+i_want[0].get('src')
        res=requests.get(comicurl)
        res.raise_for_status
        for chunk in res.iter_content(1000000):
            file.write(chunk)
        file.close()
        url=s+preurl
        i=i+1

        
#         漫画
# 博客和其他经常更新的网站通常有一个首页，其中有最新的帖子，以及一个“前
# 一篇”按钮，将你带到以前的帖子。然后那个帖子也有一个“前一篇”按钮，以此
# 类推。这创建了一条线索，从最近的页面，直到该网站的第一个帖子。如果你希望
# 拷贝该网站的内容，在离线的时候阅读，可以手工导航至每个页面并保存。但这是
# 很无聊的工作，所以让我们写一个程序来做这件事。
# XKCD 是一个流行的极客漫画网站，它符合这个结构（参见图 11-6）。首页
# http://xkcd.com/有一个“Prev”按钮，让用户导航到前面的漫画。手工下载每张漫
# 画要花较长的时间，但你可以写一个脚本，在几分钟内完成这件事。
# 下面是程序要做的事：
# • 加载主页；
# • 保存该页的漫画图片；
# • 转入前一张漫画的链接；
# • 重复直到第一张