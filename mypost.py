#!/usr/bin/python
#-\*-coding: utf-8-\*-


import urllib
import urllib2


class mypost:

    def __init__(self,url,sql_data):

	self.user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'
	self.headers = {'User-Agent' : self.user_agent } 
	self.sql_data_encode=urllib.urlencode(sql_data)
	self.url=url

    def post(self):

	req=urllib2.Request(self.url,self.sql_data_encode,self.headers)
	res_data=urllib2.urlopen(req)
	res=res_data.read()
	return res


if __name__=='__main__':

    
    url="http://192.168.1.192:8080/api/epoll?prettyJson=1"

    sql_data={
   'sql':"""
    	alter table orders add `o_all_localzg` tinyint(4) DEFAULT NULL comment 'aa';
    """,
    'ds':'ip:port:user:pass:db'
    }
    p=mypost(url,sql_data)  
    print p.post()
