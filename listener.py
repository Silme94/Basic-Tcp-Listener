#!/usr/bin/python

import sys
import socket
import threading


class IPEndPoint:
    def __init__(self, IP, PORT) -> None:
        self.IP = IP
        self.PORT = PORT

    def GetEndPoint(self):
        return (self.IP, self.PORT)

   
def send(client) -> None:
    while True:
        data = input()
        if data == None:
            data = " "
        
        client.send(data.encode())


def recv(client, addr) -> None:
    while True:
        data = client.recv(1024)
        if not data:
            print(f"[!] Client disconnected {addr[0]}:{addr[1]}")
            break
        print(data.decode())


def start_server(info) -> None:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:

            server.bind(info)
            server.listen(10)

            if info[0] != "127.0.0.1":
                print(f"[!] Server is listening on {info[0]}:{info[1]}...")
            else:
                print(f"[!] Server is listening on ANY {info[1]}...")
            
            while True:
                client, addr = server.accept()

                print(f"[!] Client connected {addr[0]}:{addr[1]}")
                
                sendThread = threading.Thread(target=send, args=(client,))
                recvThread = threading.Thread(target=recv, args=(client, addr,))

                sendThread.start()
                recvThread.start()

    except Exception as ex:
        print(ex)


def main(args) -> None:
    try:
        if args[1] == None:
            raise Exception("Try: listener.py -h")
        
        if args[1] == "-h":
            raise Exception("Usage: listener.py <IP> <PORT>")
        
        localEndPoint = IPEndPoint(args[1], int(args[2]))

        threading.Thread(target=start_server, args=(localEndPoint.GetEndPoint(),)).start()

    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main(sys.argv)
