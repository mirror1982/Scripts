import codecs

tpl_16 = codecs.open("work/teamplayerlinks16.txt", 'r', 'utf_16')
tpl_12 = codecs.open('ready/teamplayerlinks.txt', 'w', 'utf_16')

for column in tpl_16:
    column = column.strip().split('\t')
    out0 = list(column[4:8])
    out1 = list(column[14:15])
    out = out0 + out1
    out2 = "\t".join(map(str, out))
    out3 = (out2 + '\n')
    tpl_12.write(out3)

tpl_12.close()
tpl_16.close()
