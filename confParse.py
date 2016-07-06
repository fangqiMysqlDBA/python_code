#!/usr/bin/python 

import ConfigParser
import os

class mysqlConfig():
    """
    use 
        import confParse
        cnf = confParse.mysqlConfig("conf/.db.conf")
        (user,password,host,port,database) = cnf.parse()

    return 
        (user,password,host,port,database)
    """

    def __init__(self,filename):
        self.conf_file = filename
        self.fh = ConfigParser.ConfigParser()


    def parse(self):

        if os.path.exists(self.conf_file):
            self.fh.read(self.conf_file)
            self.user = self.fh.get('mysql','user')
            self.password = self.fh.get('mysql','password')
            self.host = self.fh.get('mysql','host')
            self.port = self.fh.get('mysql','port')
            self.database = self.fh.get('mysql','database')
            return (self.user,self.password,self.host,self.port,self.database)
        else:
            print "file:%s no exist"%(self.conf_file)

if __name__ == '__main__':

    cnf = mysqlConfig('./db.conf')
    print cnf.parse()
