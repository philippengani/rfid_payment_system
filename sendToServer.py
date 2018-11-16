import socket
import generateData
IP = '192.168.1.103'
PORT = 1997


def send(id,action, status):

    data =generateData.generate(id,action,status)
    print(data)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
    s.send(data.encode())
    s.close()
    print("Sent data to server")

    

