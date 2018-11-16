import socket
import generateData
IP = '192.168.1.103'
PORT = 1998

s1='view'

def status(id, s1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
    data =generateData.generate(id,s1)
    print(data)
    s.send(data.encode())
    state = s.recv(1024).decode()
    print(state)
    s.close()
    return state
