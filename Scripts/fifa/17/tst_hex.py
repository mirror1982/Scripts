import binascii
filename = 'squads'
with open(filename, 'rb') as f:
    content = f.read()
out = binascii.hexlify(content)
f = open('hex.txt', 'wb')
f.write(out)
f.close()

import binascii
filename = 'hex.txt'
with open(filename, 'rb') as f:
    content = f.read()

asci = binascii.unhexlify(content)
w = open('printed-hex.txt', 'wb')
w.write(asci)
w.close()
