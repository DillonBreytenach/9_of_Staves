import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 80))
server_socket.listen(5)



while True:
    print("[SERVER]: accepting connections: ")
    client_sock, addr = server_socket.accept()
    print("[SERVER][CONNECTED]: ", addr)
    while True:
        data=client_sock.recv(1024 *2)
        if not data or data.decode('utf-8') == 'END':
            break
        print('[CLIENT]: ', data.decode('utf-8'))
            
        try:
            client_sock.send(bytes('CONNECTING', 'utf-8'))
        except Exception as e:
            print(e)
    client_sock.close()
    
            