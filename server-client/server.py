# Importing the socket module
from socket import *

httpCodes = {
   100 : "Continue",
   101 : "Switching protocols",
   102 : "Processing",
   103 : "Early Hints",
   200 : "OK",
   201 : "Created",
   202 : "Accepted",
   203 : "Non-Authoritative Information",
   204 : "No Content",
   205 : "Reset Content",
   206 : "Partial Content",
   207 : "Multi-Status",
   208 : "Already Reported",
   226 : "IM Used",
   300 : "Multiple Choices",
   301 : "Moved Permanently",
   302 : "Found",
   303 : "See Other",
   304 : "Not Modified",
   305 : "Use Proxy",
   306 : "Switch Proxy",
   307 : "Temporary Redirect",
   308 : "Permanent Redirect",
   400 : "Bad Request",
   401 : "Unauthorized",
   402 : "Payment Required",
   403 : "Forbidden",
   404 : "Not Found",
   405 : "Method Not Allowed",
   406 : "Not Acceptable",
   407 : "Proxy Authentication Required",
   408 : "Request Timeout",
   409 : "Conflict",
   410 : "Gone",
   411 : "Length Required",
   412 : "Precondition Failed",
   413 : "Payload Too Large",
   414 : "URI Too Long",
   415 : "Unsupported Media Type",
   416 : "Range Not Satisfiable",
   417 : "Expectation Failed",
   418 : "I'm a Teapot",
   421 : "Misdirected Request",
   422 : "Unprocessable Entity",
   423 : "Locked",
   424 : "Failed Dependency",
   425 : "Too Early",
   426 : "Upgrade Required",
   428 : "Precondition Required",
   429 : "Too Many Requests",
   431 : "Request Header Fields Too Large",
   451 : "Unavailable For Legal Reasons",
   500 : "Internal Server Error",
   501 : "Not Implemented",
   502 : "Bad Gateway",
   503 : "Service Unavailable",
   504 : "Gateway Timeout",
   505 : "HTTP Version Not Supported",
   506 : "Variant Also Negotiates",
   507 : "Insufficient Storage",
   508 : "Loop Detected",
   510 : "Not Extended",
   511 : "Network Authentication Required"

}

# IP address of the server  (string)
serverName = 'PUT_SERVER_IP'

# Server port number (integer)
serverPort = 12000
""" Creating server's socket: the first parameter (AF_INET) indicates that the
underlying network is using IPv4, the second parameter (SOCK_DGRAM)
indicates that it is a UDP socket
"""
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assigning port number and server's IP address to the server's socket
serverSocket.bind((serverName, serverPort))
print('The server is ready to receive.')
""" The while loop will allow UDP server to receive and process
packets from clients indefinitely
"""
while True:
   """ The packet's data is put into the variable message
   and the packet's source address (both IP address and client's port number)
   is put into the variable clientAddress.
   """
   message, clientAddress = serverSocket.recvfrom(2048) # max. bytes the server can receive
   print(f'Code recieved: {message.decode()}')
   modifiedMessage = "Invalid Code"
   for code in httpCodes:
      if code == int(message.decode()):
         modifiedMessage = httpCodes[code]
   """ Attaching the client's address (IP address and port number)
   to the capitalized message, and sending the resulting packet
   into the server's socket; then, the server address will also
   be attached to the packet which will then be delivered to the specified client's address.
   """
   serverSocket.sendto(modifiedMessage.encode(), clientAddress)







