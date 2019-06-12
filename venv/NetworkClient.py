#!/usr/bin/python3

import socket

host='localhost'

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr=(host, 22)
mysock.connect(addr)

try:
    msg=b"Test Message\n"
    mysock.sendall(msg)

# try opening a socketusing netcat sudo nc -l 22

except socket.error:
    print("Socket error")

finally:
    mysock.close()