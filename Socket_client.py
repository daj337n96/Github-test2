import socket
import threading
import time

HEADER = 64 #msg length
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

client = socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    #Actual message in str encode to bytes based on FORMAT
    message = msg.encode(FORMAT)
    #Byte length(int)
    msg_length = len(message)
    #Encode length into bytes based on FORMAT
    send_length = str(msg_length).encode(FORMAT)
    #Padding. b = byte
    #Use len(send_length) instead of msg_length
    send_length += b' '*(HEADER - len(send_length))
    #Sends the length then the actual message to execute if msg_length:
    client.send(send_length)
    client.send(message)
    print(client.recv(2048))
while True:
    Message_to_send = input()
    send(Message_to_send)
