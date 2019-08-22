#!/usr/bin/env python3

from socket import *

s = socket()
s.bind(('0.0.0.0',8001))
s.listen(3)

c,addr = s.accept()
data = c.recv(1024)
print(data)
