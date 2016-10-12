#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 自动交互ssh
不能在子进程中执行
"""

from collections import OrderedDict
import pexpect
import sys

# HOSTS {'关键字1:关键字2...': [user, ip, port] }
HOSTS = OrderedDict({
    '1:45:loc': ['192.168.1.64', 22, 'root', '123456'],
})


def list_host():
    for k, v in HOSTS.iteritems():
        print '%s==>%s' % (k, v[0])


def fuzzy_get(key):
    for _key in HOSTS:
        if key in _key:
            return HOSTS[_key]


def ssh_cmd(host, port, user, password):
    try:
        child = pexpect.spawn('ssh -p %s %s@%s' % (port, user, host))
        i = child.expect(['password: ', 'continue connecting (yes/no)?'], timeout=10)
        if i == 0:
            child.sendline(password)
        elif i == 1:
            child.sendline('yes\n')
            child.expect('password: ')
            child.sendline(password)
        else:
            sys.exit('Login failed!')
        print 'Login Success! (Ctrl-D Exit)'
        child.interact()
    except Exception as e:
        sys.exit(str(e))


if __name__ == '__main__':
    print 'All Servers:'
    list_host()
    key = raw_input('Please choice a server to connect (`:` split):')
    host, port, user, password = fuzzy_get(key)
    sh_cmd(host, port, user, password)
