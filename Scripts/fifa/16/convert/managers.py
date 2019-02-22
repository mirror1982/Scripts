import sys, codecs
reload(sys)
sys.setdefaultencoding('utf8')

manager_16 = codecs.open("work/manager16.txt", 'r', 'utf_16')
manager_12 = codecs.open('ready/manager.txt', 'w', 'utf_16')


for column in manager_16:
    column = column.rstrip().split('\t')

    out = list(column[0:2] + column[3:4])

    out2 = "\t".join(map(str, out))
    out3 = (out2 + '\n')
    manager_12.write(out3)

manager_12.close()
manager_16.close()
