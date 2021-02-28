from socket import *


def createServer():
    serversocket = socket(AF_INET, SOCK_STREAM)
    forwarder_socket = socket(AF_INET, SOCK_STREAM)
    try :
        serversocket.bind(('localhost',8000))
        serversocket.listen(5)
        while(1):
            # Устанавливаем соединение с клиентом
            (clientsocket, address) = serversocket.accept()
            rd = clientsocket.recv(5000).decode()
            pieces = rd.split("\n")
            if len(pieces) > 0:
                print(str(pieces[0]))
                remote_data = pieces[0]+"\r\n"
                print(remote_data)
                print(1)
                # Пробрасываем сокет на удаленный сервер
                forwarder_socket.connect(("data.pr4e.org", 80))
                forwarder_socket.send(remote_data.encode())
                # Считываем ответ
                data = ""
                while True:
                    data_from_server = forwarder_socket.recv(512)
                    data += data_from_server.decode()
                    if len(data_from_server) < 1:
                        break
                    print(data_from_server.decode(), end="")
                forwarder_socket.shutdown(SHUT_WR)
                # Отправляем ответ удаленного сервера клиенту
            if data:
                clientsocket.sendall(data.encode())
            else:
                clientsocket.send("Error".encode())
            clientsocket.shutdown(SHUT_WR)

    except KeyboardInterrupt :
        print("\nShutting down...\n")
    except Exception as exc :
        print("Error:\n")
        print(exc)

    serversocket.close()


print('Access http://localhost:8000')
createServer()