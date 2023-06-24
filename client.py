import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_address = "127.0.0.1"
port = 12345

s.connect((ip_address, port))


while True:
    msg = s.recv(1024)
    print(msg.decode("utf-8"))
    if msg == "exit":
        break
    msg = input("Enter message: ")
    s.send(msg.encode("utf-8"))

s.close()
