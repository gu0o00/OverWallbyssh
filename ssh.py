#!/usr/bin/env python
import commands
import os
import sys

def start():
    os.system("ssh -qfnNT -D 127.0.0.1:7070 root@45.114.10.211")
    #os.system('ssh -qfnNT -D 127.0.0.1:7070 fastssh.com-guojian-ph@us-phoenix.fastssh.com')
    #os.system('ssh -qfnNT -D 127.0.0.1:7070 fastssh.com-guojian-jp@jp-1.fastssh.com')

def kill():
    status,output = commands.getstatusoutput('ps aux|grep "ssh -qfnNT"')
    result = output.split("\n")
    for i in range(len(result)-2):
        id = result[i].split("  ")[1]
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
