from socket import *


serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Enter a valid HTTP status code: ')
clientSocket.sendto(message.encode(), ('PUT_SERVER_IP_HERE', serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()
