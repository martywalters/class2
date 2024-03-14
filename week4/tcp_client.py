# Name:        tcp_client

import socket
tcp1 = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
tcp_ip = "192.168.0.2"
port = 9000
buffer_size = 1024
msg = ("Client test.")


tcp1.connect((tcp_ip , port))
print ("Sending message: " + msg)
tcp1.send(msg.encode('utf8'))

data = tcp1.recv(buffer_size).decode('utf-8')

print ("Data reveived: " +  data)
