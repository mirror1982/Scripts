import sys, codecs
reload(sys)
sys.setdefaultencoding('utf8')

playernames_16 = codecs.open("work/playernames16.txt", 'r', 'utf_16')
playernames_12 = codecs.open('ready/playernames.txt', 'w', 'utf_16')


for column in playernames_16:
    column = column.rstrip().split('\t')

    out = list(column[0:1] + column[2:3])

    out2 = "\t".join(map(str, out))
    out3 = (out2 + '\n')
    playernames_12.write(out3)

playernames_12.close()
playernames_16.close()
