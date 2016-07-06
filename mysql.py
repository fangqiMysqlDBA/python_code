#!/usr/bin/python
# _*_ coding:utf8 _*_

import MySQLdb
from MySQLdb.times import *
import MySQLdb.converters
from MySQLdb.constants import FIELD_TYPE
from datetime import date, datetime, time, timedelta




def DateTime_or_None_with_Millisecond(s):
    if ' ' in s:
        sep = ' '
    elif 'T' in s:
        sep = 'T'
    else:
        return Date_or_None(s)

    try:
        d, t = s.split(sep, 1)
        d = Date_or_None(d)
        t = Time_or_None(t)
        return datetime.combine(d,t)
    except:
        return Date_or_None(s)

class  mysql:

    """
    args: ip,端口,用户名,密码
    func: 设置字符集为utf8,超时时间为20s,开启自动提交,select的返回结果为字典类型
    """
   
    def __init__(self,host,port,user,passwd,db):

        self.host=host
        self.port=port
        self.user=user
        self.passwd=passwd
        self.db=db
        self.charset='utf8'
        self.connect_timeout=20
        self.conn=''
        self.cursor=''

        #处理python2.6在处理datetime,和timestamp毫秒级别的问题
        self.conv=MySQLdb.converters.conversions
        self.conv[FIELD_TYPE.DATETIME] = DateTime_or_None_with_Millisecond
        self.conv[FIELD_TYPE.TIMESTAMP] =DateTime_or_None_with_Millisecond

    def connect(self):
        self.conn=MySQLdb.Connection(
                host=self.host,
                port=self.port,
                user=self.user,
                passwd=self.passwd,
                db=self.db,
                charset=self.charset,
                connect_timeout=self.connect_timeout,
                conv=self.conv)
        self.conn.autocommit(1)
        self.cursor=self.conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    #return self.cursor

    def select(self,sql):
        ret=self.cursor.execute(sql)
        out=self.cursor.fetchall()
        return out


    def modify(self,sql):
        ret=self.cursor.execute(sql)
	return ret

    def quit(self):
        self.conn.close()

    @staticmethod
    def type_return(s):

        if type(s) == type(u'abc') or type(s) == type('abc'):
            return '"' + str(s) + '"' + ','
        elif s == None:
            return  '"",'
        elif type(s) == type(1) or type(s) == type(1L):
            return str(s) +  ','
        else:
            return '"' + str(s) + '"' + ','

    @staticmethod
    def get_insert(data,table,column_list):
        """
        args:带关键字的字典数组,表名,列的顺序数组        
        func:输出insert的完整sql
        """
        for row in data:
            string_insert='insert into %s(%s) value('%(table,','.join([ '`' + s + '`'   for s in column_list]))
            for column in column_list:
                string_insert += "'%s',"%row[column]
            string_insert = string_insert.rstrip(',') + ');'
            print string_insert
