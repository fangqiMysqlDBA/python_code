#!/usr/bin/python

#import traceback
#traceback.print_exc(file=self.wf_log)
import sys
import logging

import MySQLdb
import log


class sqlMysql():

    def __init__(self,host,port,user,password,database):
        self.host = host
        self.port = int(port)
        self.user = user
        self.password = password
        self.database = database
        self.charset = "utf8"
        log.init_log("log/muti")

        self.conn = MySQLdb.connect(host=self.host,
                                    port=self.port,
                                    user=self.user,
                                    passwd=self.password,
                                    db=self.database,
                                    charset=self.charset
                                    )
	self.conn.autocommit(1)
        self.cursor = self.conn.cursor()

    def query(self,sql):
        sql.strip()
        if sql.startswith("select") or \
           sql.startswith("SELECT") or \
           sql.startswith("Select"):
            try:
                self.cursor.execute(sql)
                result = self.cursor.fetchone()
                logging.getLogger('sus').info("[select:success][out:s]")
            except MySQLdb.Error, e:
                logging.getLogger('wf').error("[select:failed][sql:%s][error:%s]"%(sql,str(e)))


        elif sql.startswith("insert") or \
             sql.startswith("INSERT") or \
             sql.startswith("Insert"):

            try:
                result = self.cursor.execute(sql)
                logging.getLogger('sus').info("[insert:success][out:%s]"%result)
            except MySQLdb.Error, e:
                logging.getLogger('wf').error("[insert:failed][sql:%s][error:%s]"%(sql,str(e)))

        elif sql.startswith("update") or \
             sql.startswith("UPDATE") or \
             sql.startswith("Update"):

            try:
                result = self.cursor.execute(sql)
                logging.getLogger('sus').info("[update:success][out:%s]"%result)
            except MySQLdb.Error, e:
                logging.getLogger('wf').error("[update:failed][sql:%s][error:%s]"%(sql,str(e)))

        elif sql.startswith("delete") or \
             sql.startswith("DELETE") or \
             sql.startswith("Delete"):

            try:
                result = self.cursor.execute(sql)
                logging.getLogger('sus').info("[delete:success][out:%s]"%result)
            except:
                logging.getLogger('wf').error("[delete:failed][sql:%s][error:%s]"%(sql,str(e)))
        else:
                print "[sql:%s]"%sql


    def quit(self):
        self.cursor.close()
        self.conn.close()

if __name__ == "__main__":
    
    #def __init__(self,host,port,user,password,database):

    mysqlIns = sqlMysql("",,"","","") 
    mysqlIns.query("select * from t ")
    mysqlIns.query("insert into t value(10,'sdff')")
    mysqlIns.query("delete from t where id = 10")
    mysqlIns.query("update t set name ='yamiedie' where id = 8")
    mysqlIns.quit()

