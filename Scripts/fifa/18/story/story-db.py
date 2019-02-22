import binascii

filename = 'story'
with open(filename, 'rb') as f:
    content = binascii.hexlify(f.read())

content2 = content[428:len(content)+2]

print content[0:428]
print len(content)
asci = binascii.unhexlify(content2)
w = open('story.db', 'wb')
w.write(asci)
w.close()
