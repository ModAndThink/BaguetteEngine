import socket
import threading
import random
import time

class Client(object):
    def __init__(self,port=5050,ip="0.0.0.0"):
        self.PORT = port
        self.HEADER = 64
        self.SERVER = ip
        self.FORMAT = "utf-8"
        self.DISCONNECT_MESSAGE = "!DISCONNECT"
        self.ADDR = (self.SERVER,self.PORT)

        self.ClientNumber = 0
        self.VCN = False

        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.client.connect(self.ADDR)

    def UpdateCN(self,new_value):
        self.ClientNumber = new_value
        self.VCN = True

    def UpdateValue(self,lm):
        pass

    def send(self,msg):
        message = msg.encode(self.FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(self.FORMAT)
        send_length += b" " * (self.HEADER - len(send_length))
        self.client.send(send_length)
        self.client.send(message)

    def run(self):
        self.start()
        thread = threading.Thread(target=self.listenToMessage)
        thread.start()

    def start(self):
        pass
    
    def listenToMessage(self):
        while True:
            msg_length = self.client.recv(self.HEADER).decode(self.FORMAT)
            if msg_length:
                msg_length = int(msg_length)
                msg = self.client.recv(msg_length).decode(self.FORMAT)
                lm = msg.split("|")
                if lm[0] == "cn":
                    self.UpdateCN(int(lm[1]))
                else:
                    self.UpdateValue(lm)
                

    def left(self):
        self.send(self.DISCONNECT_MESSAGE)
