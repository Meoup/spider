# -*- coding:utf-8 -*-
import urllib
import urllib2
import random

def loadpage(url):
    """根据URL发送响应服务器请求"""

    ua_list = [
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
    'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'
              ]
    #随机选取一个user-agent
    user_agent = random.choice(ua_list)
    #请求报头
    headers = {'User-Agent':user_agent}
    #填写请求
    request = urllib2.Request(url,headers = headers)
    #发送请求并返回一个响应
    response = urllib2.urlopen(request)
    html = response.read()
    return html

def writepage(begin_page,end_page,url):
    """保存爬取的内容"""
    for i in range(begin_page,end_page + 1):
        #对个页面的url值进行处理
        page = (i - 1) * 50
        
        #组合完整的页面url
        full_url = url + k + '&pn=' + str(page)
        file_name = str(i) + '.html'

        #载入页面
        html = loadpage(full_url)
        
        #保存返回的html文档
        with open(file_name,'w') as f:
            f.write(html)
        print ('正在保存' + file_name)

if __name__ == '__main__':
    url = 'tieba.baidu.com/f?'
    kw = raw_input('请输入要爬取的贴吧名：')
    k = urllib.urlencode({'kw':kw})
    begin_page = int(raw_input('请输入起始页：'))
    end_page = int(raw_input('请输入终止页：'))
    writepage(begin_page,end_page,url)
