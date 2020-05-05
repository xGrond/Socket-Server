#!/usr/bin/env python3
import time
import socket

HOST = '78.170.31.31'  # The server's hostname or IP address
PORT = 3169        # The port used by the server

val = 0

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
while True:
    client.send("DATA " +  str(val))
    time.sleep(1)
    val = val + 1

#from_server = client.recv(4096)
#client.close()
#print from_server
