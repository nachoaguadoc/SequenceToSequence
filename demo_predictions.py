import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 9988))
s.sendall('What is the command to run a script?'.encode())
answer = s.recv(1024).decode("utf-8")
print(answer)
s.close()
