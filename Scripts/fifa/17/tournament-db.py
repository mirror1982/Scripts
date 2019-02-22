import binascii
filename = 'tournament'
with open(filename, 'rb') as f:
    content = f.read()
content = binascii.hexlify(content)
content = content[292:len(content)+2]
#2299950
f = open('tour_hex.txt', 'wb')
f.write(content)
f.close()

import binascii
filename = 'tour_hex.txt'
with open(filename, 'rb') as f:
    content = f.read()

asci = binascii.unhexlify(content)
w = open('tournament.db', 'wb')
w.write(asci)
w.close()
