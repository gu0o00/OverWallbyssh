#!/usr/bin/env python
import commands
import os
import sys

username = "ssh username"
host_ip_addr = "ssh server ip"
local_port = 7070

def start():
    os.system("ssh -qfnNT -D 127.0.0.1:%d %s@%s" % (local_port,username,host_ip_addr))
    #os.system('ssh -qfnNT -D 127.0.0.1:7070 fastssh.com-guojian-ph@us-phoenix.fastssh.com')
    #os.system('ssh -qfnNT -D 127.0.0.1:7070 fastssh.com-guojian-jp@jp-1.fastssh.com')

def kill():
    status,output = commands.getstatusoutput('ps aux|grep "ssh -qfnNT"')
    result = output.split("\n")
    for i in range(len(result)-2):
        tmp = result[i].split("    ")[1].strip()    #把pid的前面的字符去掉
        id = tmp.split("  ")[0]                     #把pid后面的字符去掉
        commands.getstatusoutput("kill "+id)
        print(id+" have been killed")

def list():
    status,output = commands.getstatusoutput('ps aux|grep "ssh -qfnNT"')
    result = output.split("\n")
    for i in range(len(result)-2):
        print(result[i])

def main():
    choose = sys.argv.pop()

    if choose == 'start':
        start()
    elif choose == 'list':
        list()
    elif choose == 'kill':
        kill()
    else:
        print("error opreator")

if __name__ == '__main__':
    main()
