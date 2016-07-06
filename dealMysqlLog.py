#!/usr/bin/python
# coding: utf8

import re
import sys


class dealMysqlLog():

    def  __init__(self,line):
        self.line     = line
        self.time     = ''
        self.threadid = ''
        self.command  = ''
        self.sql      = ''
        self.l=re.compile(r"""(\d{6}\s+\d{1,2}:\d\d:\d\d)?  #time
                        \s+
                        (\d+)                               #thread id
                        \s+
                        (Query|Connect|Quit)                #commad
                        \s+
                        (.+)                                #sql
                         """,re.X)
        self.run()
    
    def run(self):
        m=self.l.search(self.line.strip('\n')) 
        if m:
            self.time     = m.group(1) if m.group(1) else ' ' 
            self.threadid = m.group(2) if m.group(2) else ' ' 
            self.command  = m.group(3) if m.group(3) else ' ' 
            self.sql      = m.group(4) if m.group(4) else ' ' 

    def get(self):
        return (self.time,self.threadid,self.command,self.sql)

if __name__ == "__main__":

    logfile=sys.argv[1]

    with open(logfile) as LOG:   
        for line in LOG:
            l=dealMysqlLog(line)
            (time,threadid,command,sql)=l.get()
            if command == 'Query':
                print sql
            
