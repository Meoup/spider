#-*- coding:utf-8 -*-
import urllib2
import re

class Spider(object):
    """创建一个爬虫类，初始化各个属性"""
    def __init__(self):
        self.page = page

    def loadpage(self):
        #载入页面方法
        print '正在下载数据！'
        url = 'http://neihanshequ.com/'
        headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)'}
        request = urllib2.Request(url,headers = headers)
        response = urllib2.urlopen(request)
        html = response.read()

        #制定正则匹配规则，获取匹配字符串集合
        pattern = re.compile('''<h1 class="title">(.*?)</h1>''',re.S)
        context = pattern.findall(html)
        self.dealpage(context)

    def dealpage(self,context):
        #对获取的页面文档进行处理的方法
        for text in context:
            text = text.replace('<p>','').replace('</p>','')
            print '正在保存数据！'
            self.savepage(text)

    def savepage(self,text):
        #保存获取的text文件
        file_name = str(self.page) + '.txt'
        with open(file_name,'a') as f:
            f.write(text)
page = 1
neihanspider = Spider()
neihanspider.loadpage()
