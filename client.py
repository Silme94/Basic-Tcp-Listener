#!/usr/bin/python

import socket


def start_client(server_address):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(server_address)
    
    print(f"[!] Connected to server at {server_address[0]}:{server_address[1]}")

    while True:
        message = input("Enter a message to send: ")
        client.send(message.encode())
        
        if message.lower() == "exit":
            break

        response = client.recv(1024)
        print("Received response:", response.decode())

    client.close()
    print("[!] Connection closed.")


if __name__ == "__main__":
    server_address = ("localhost", 80)  
    start_client(server_address)
