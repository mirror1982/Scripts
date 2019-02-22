import binascii

filename = 'tournament'
with open(filename, 'rb') as f:
    content = binascii.hexlify(f.read())

print len(content)


dif = 14041628 - len(content)

if dif >= 0:
    for i in range(1, dif+1):
        content += '0'
else:
    print "DB file is too large"
    quit()


asci = binascii.unhexlify(content)
w = open('TournamentMine', 'wb')
w.write(asci)
w.close()
