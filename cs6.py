#!/usr/bin/python
#_*_ coding:utf8 _*_

from os import system
import curses
import curses.wrapper
import sys

reload(sys)
sys.setdefaultencoding('utf8')

global screen

# 暂时没有用到
def get_param(prompt_string):
    screen.clear()
    screen.border(0)
    screen.addstr(2,2,prompt_string)
    screen.refresh()
    # 从指定的地方获取输入，会回显
    input = screen.getstr(10,10,60)
    return input

# 暂时没有用到
def execute_cmd(cmd_string):
    a = system("clear") 
    a = system(cmd_string)
    print ""
    if a == 0:
        print "command ok"
    else:
        print "command no"
    # 将程序阻塞在这里
    raw_input("press enter to return main")
    # 换行
    print ""

def display_host(row_init,hostlist,my_cursor):

    global screen
    column_init=4
    screen = curses.initscr()
    # 重置窗口
    curses.endwin()
    # 清屏
    screen.clear()
    # 制作边框
    screen.border(0)
    # 设置颜色
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    # 增加标题头
    screen.addstr(2,2,"host list:",curses.color_pair(2))
    # 制作主机host 列表
    for i,host in enumerate(hostlist):
        if i == my_cursor - row_init  :
            screen.addstr(row_init+i,column_init - 3,"-> %s - %s -[%s]"%(str(i+1),host['host'],host['info']),curses.color_pair(1))
        else:
            screen.addstr(row_init+i,column_init,"%s - %s -[%s]"%(str(i+1),host['host'],host['info']))

    #curses.cbreak()
    # row,column,string

    # 将光标移动到指定的地方
    screen.move(cursor,4)
    # 将之前设置的给展示出来
    screen.refresh()

hostlist=[
        {"user":"root","host":"192.168.1.1","info":"A "},
        {"user":"root","host":"192.168.1.2","info":"B "},
        {"user":"root","host":"192.168.1.3","info":"C "},
        {"user":"root","host":"192.168.1.4","info":"D "},
        {"user":"root","host":"192.168.1.5","info":"E "},
        {"user":"root","host":"192.168.1.6","info":"F "}
        ]

x = 0

# idx 为展示的第几个选项：cursor - first  + 1= idx 

idx = 1
first=cursor=4
length=len(hostlist)
last = first + length - 1

try:
    while x !=  ord('q'):


        display_host(first,hostlist,cursor)

        x=screen.getch()

        if x == ord('\n'):
            idx = cursor - first + 1
            screen.clear()
            break

        if x == ord('j'):
            if cursor >= last   :
                cursor=last  
            else:
                cursor+=1

        if x == ord('k'):
            if cursor <= first:
                cursor=first
            else:
                cursor-=1
    curses.endwin()

except:
    curses.endwin()



if x == ord('q'):
    sys.exit(0)
else:
    cmd= "ssh %s@%s"%(hostlist[idx-1]['user'],hostlist[idx-1]['host'])
    system("clear")
    system(cmd)
