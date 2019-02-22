import socket

#sock_hand = raw_input('Enter a web-address: ')
sock_hand = 'ya.ru'

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((sock_hand, 80))
mysock.send('GET http://www.ru/ HTTP/1.0\n\n')

while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    print data

mysock.close()
