#!/usr/bin/python
import hashlib
import datetime

class myhash:
    def __init__(self):
        self.m=hashlib.md5()

    def string_hash(self,s):    
        self.m.update(s)
        return self.m.hexdigest()

    def time_hash(self):
        now = datetime.datetime.now()
        str=now.strftime('%Y%m%d%H%M%S')
        return self.string_hash(str)


if __name__ == '__main__':

    m=myhash()
    print m.time_hash()
