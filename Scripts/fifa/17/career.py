import binascii

filename = 'career'
with open(filename, 'rb') as f:
    content = binascii.hexlify(f.read())

content2 = content[422252:len(content)+2]

asci = binascii.unhexlify(content2)
w = open('career.db', 'wb')
w.write(asci)
w.close()
