from socket import *

def createServer():
    serversocket1 = socket(AF_INET, SOCK_STREAM)
    try :
        serversocket1.bind(('localhost',7000))
        serversocket1.listen(5)
        while(1):
            (clientsocket1, address1) = serversocket1.accept()

            rd = clientsocket1.recv(5000).decode()
            pieces = rd.split("\n")
            if ( len(pieces) > 0 ) : print(pieces[0])

            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body>Hello World</body></html>\r\n\r\n"
            clientsocket1.sendall(data.encode())
            clientsocket1.shutdown(SHUT_WR)

    except KeyboardInterrupt :
        print("\nShutting down...\n");
    except Exception as exc :
        print("Error:\n");
        print(exc)

    serversocket1.close()

print('Access http://localhost:7000')
createServer()