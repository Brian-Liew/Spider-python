import requests 
from bs4 import BeautifulSoup
import os

#小说列表网页以及主网页
target='https://www.biqubao.com/book/13991/'
server='https://www.biqubao.com'

#注意转化编码
req=requests.get(url=target)
req.encoding='gbk'
html=req.text
#找到list
div=BeautifulSoup(html,"html.parser")
list_tag=div.div(id='list')
#小说名
title=list_tag[0].dl.dt.string
#目标文件夹
save_path='F:/Python/novel/new'
dir_path=save_path+'/'+title
if not os.path.exists(dir_path):
	os.path.join(save_path,title)
	os.mkdir(dir_path)

for dd_tag in list_tag[0].dl.find_all('dd'):
	#章节名字
	chapter_name=dd_tag.string
	#章节网址
	chapter_url=server+dd_tag.a.get('href')
	c_req=requests.get(url=chapter_url)
	c_req.encoding='gbk'
	c_soup=BeautifulSoup(c_req.text,"html.parser")
	content_tag=c_soup.div.find(id='content')
	content_text=str(content_tag.text.replace('\xa0','\n'))

	with open (dir_path+'/'+chapter_name[:]+'.txt','w') as f:
		f.write(content_text)


