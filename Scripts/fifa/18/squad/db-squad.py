import binascii

filename = 'squads.db'
with open(filename, 'rb') as f:
    content = binascii.hexlify(f.read())

content = '46424348554e4b5301005400000098fb40004d795371756164732020202020200043010000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000053617665547970655f5371756164730000000000000000000000000000000000000000000000000000000000' + content

dif = 8517628 - len(content)

if dif >= 0:
    for i in range(1, dif-7):
        content += '0'
else:
    print "DB file is too large"
    quit()

content += '9AA9CD32'

asci = binascii.unhexlify(content)
w = open('SquadsMine', 'wb')
w.write(asci)
w.close()
