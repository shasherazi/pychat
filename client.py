import socket
from threading import Thread

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_address = "127.0.0.1"
port = 12345

s.connect((ip_address, port))

globalMsg = ""
class Recive_Thread(Thread):
    def run(self):
        while True:
            msg = s.recv(1024)
            print(msg.decode("utf-8"))


        
class Send_Thread(Thread):
    def run(self):
        while True:
            msg = input("Enter message: ")
            s.send(msg.encode("utf-8"))
                
t1 = Recive_Thread()
t2 = Send_Thread()
t1.start()
t2.start()

t1.join()
t2.join()

s.close()