import binascii

filename = 'story.db'
with open(filename, 'rb') as f:
    content = binascii.hexlify(f.read())

content = '46424348554e4b53010054000000bc746100d0afd187d0b5d0b9d0bad0b02049492022d098d181d182d0bed180d0b8d0b822202d20d0b0d0b2d182d0bed181d0bed185d1802e203200000000000000baa2119c9e7528215af045a8bb3f1b5f46279d0100000053617665547970655f53746f7279320048d3b807510000009c9e7528215af045a8bb3f1b5f46279d00000000856700000100000000000000010000000000c841000000000700000001000000486f6d6500696e67006d6d61727900006070414d000000006070414d00000000ffffffff' + content

dif = 12773956 - len(content)

if dif >= 0:
    for i in range(1, dif+1):
        content += '0'
else:
    print "DB file is too large"
    quit()

# content += '9AA9CD32'

asci = binascii.unhexlify(content)
w = open('StoryMine', 'wb')
w.write(asci)
w.close()
