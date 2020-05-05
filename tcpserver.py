import socket

HOST = '0.0.0.0'  # Standard loopback interface address (localhost)
PORT = 3169        # Port to listen on (non-privileged ports are > 1023)


import socket
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind((HOST, PORT))
serv.listen(5)
while True:
    conn, addr = serv.accept()
    from_client = ''
    while True:
        data = conn.recv(4096)
        if not data: break
        from_client = data
        print from_client
        #conn.send("I am SERVER<br>"))
    #conn.close()
    print 'client disconnected'
