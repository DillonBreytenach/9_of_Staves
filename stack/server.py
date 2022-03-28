import socket

def Main():
    host = '127.0.0.1'
    port = 7000

    mySocket = socket.socket()
    mySocket.bind((host,port))

    mySocket.listen(10)

    print("ATTEMPTING: ")
    conn, addr = mySocket.accept()
    print ("Connection from: " + str(addr))
    message = 'Thank you connecting'
    conn.send(message.encode())

    while True:
        data = conn.recv(1024).decode()
        strdata = str(data)
        test_str = str(strdata)+"HELLO"
        try:
            conn.sendall(test_str.encode())
            print(strdata)
        except Exception as e:
            print(e)    

        try:
            mySocket.close()
        except Exception as e:
            print(e)

if __name__ == '__main__':
    Main()