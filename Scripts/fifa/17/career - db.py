import binascii

filename = 'CareerKloppLiverpool'
with open(filename, 'rb') as f:
    content = binascii.hexlify(f.read())
#print content[1410948:len(content)+2]

#print len(content)
#print content[0:422252]
z = content[1410950:len(content) + 2]

content2 = content[422252:1410950]


#1410948
asci = binascii.unhexlify(content2)
w = open('CareerKloppLiverpool.db', 'wb')
w.write(asci)
w.close()

x = binascii.unhexlify(z)
y = open('car_end', 'wb')
y.write(x)
y.close()
