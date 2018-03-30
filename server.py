# by MrDzo python3
import socket
import threading

class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        print("listen on {}:{}".format(self.host,self.port))
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            print(address)
            client.settimeout(60)
            threading.Thread(target = self.listenToClient,args = (client,address)).start()

    def listenToClient(self, client, address,size=1024):
        while True:
            try:
                data = client.recv(size)
                if data:
                    # Set the response to echo back the recieved data
                    print(data.decode('utf-8'))
                    response = data
                    client.send(response)
                else:
                    raise ImportError('Client disconnected')
            except:
                client.close()
                return False

if __name__ == "__main__":
    host = input("host: ")
    while True:
        port_num = input("Port? ")
        try:
            port_num = int(port_num)
            break
        except ValueError as e:
            print(e)
            pass

    ThreadedServer(host,port_num).listen()
