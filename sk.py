import socket
s=socket.socket()
host=socket.gethostname()
print(host)
port=12345
s.bind((host,port))


s.listen(5)
while 1:
    c,address=s.accept()
    print('连接地址',address)

    c.send('喔驲尼忠于连上了'.encode('utf-8'))
    c.close()
