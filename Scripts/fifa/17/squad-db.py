import binascii

filename = 'squadssep'
with open(filename, 'rb') as f:
    content = binascii.hexlify(f.read())

content2 = content[292:len(content)+2]

asci = binascii.unhexlify(content2)
w = open('squadssep.db', 'wb')
w.write(asci)
w.close()