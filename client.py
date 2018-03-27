#by MrDzo python3
import socket
import threading

class ClientThread():
    def __init__(self,host,port):
        self.server_address = (host,port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.dataRecive = None

    def Start(self):
        self.connect()
        self.update()

    def connect(self):
        try:
            self.sock.connect(self.server_address)
            print('Connect Sever ', self.server_address)
        except Exception as e:
            print(e)

    def update(self):
        threading.Thread(target=self.listen, args=()).start()
        return self

    def listen(self,size=1024):
        while True:
            data = self.sock.recv(size)
            self.dataRecive = data.decode('utf-8')

    def SendData(self,message):
        try:
            self.sock.send(message)
            #self.update()
        except socket.error as e:
            print('Send error :',e)
            self.connect()

if __name__ == '__main__':
    client = ClientThread(host='10.228.29.133',port=6666)
    client.Start()
    while True:
        data = input('=>')
        client.SendData(data.encode('utf-8'))
        print(client.dataRecive)
