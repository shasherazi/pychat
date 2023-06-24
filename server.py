import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_address = "127.0.0.1"
port = 12345
s.bind((ip_address, port))
s.listen(5)
c, addr = s.accept()
print("Connection from: " + str(addr))

while True:
    msg = input("Enter message: ")
    c.send(msg.encode("utf-8"))
    if msg == "exit":
        break
    msg = c.recv(1024)
    print(msg.decode("utf-8"))

c.close()
