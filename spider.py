# -*- coding:utf-8 -*-
#!/usr/bin/python
import sys
import csv
import MySQLdb
import re
import urllib
import urllib2
import json
import threading
from time import ctime
print ctime()

class Spider:

    #初始化
    def __init__(self,url):
        self.url = url
        self.ext = '.csv'

    #获取html
    def getHtml(self):
        try:
            url = self.url
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            page = response.read()
            return self.conv(page,'gb2312','utf-8')
        except urllib2.URLError, e:
            if hasattr(e,"reason"):
                print u"网页打开失败,错误原因",e.reason
                return None
    #匹配正则单组数据            
    def getMatch(self,html,reg):

        comp = re.search(reg,html)
        if comp:
        	return comp.group(1) 
        else:
        	return None 
    #匹配正则列表
    def getMatchAll(self,html,reg):

        comp = re.findall(reg,html)
        if comp:
        	return comp    
        else:
        	return None 
    #编码数据转化
    def conv(self,str,from_charst,to_charst):

        return  unicode(str, from_charst).encode(to_charst)
    #写入csv文件
    def csvWrite(self,f,head,data):
    	try:    		
	        csvfile = file(f + self.ext,'wb')
	        writer = csv.writer(csvfile)
	        writer.writerow(head)
	        writer.writerows(data)
	        csvfile.close()             
        except IOError,e:
            print "写入异常，原因" + e.message
        finally:
            print "写入任务完成"

if __name__ == '__main__':
	# 测试基金代码事例
	spider = Spider("http://fund.eastmoney.com/f10/jjzh_001494.html")
	html= spider.getHtml();

	reg1 = r'<tbody>(.*?)</tbody>'
	content = spider.getMatch(html,reg1)
	reg2 = r'<a\s+href="(http://fund.eastmoney.com)\/(\d+)\.html">\d+</a>'
	con = spider.getMatchAll(content,reg2)
	spider.csvWrite('001494',['url','coding'],con)

	print ctime()
