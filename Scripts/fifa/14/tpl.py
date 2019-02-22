import codecs

tpl_14 = codecs.open("teamplayerlinks14.txt", 'r', 'utf_16')
tpl_12 = codecs.open('tpl_12.txt', 'w', 'utf_16')

for column in tpl_14:
    column = column.strip().split('\t')
    out0 = list(column[4:8])
    out1 = list(column[12:13])         # 14-15
    #out1 = list(column[14:15])         # 16
    out = out0 + out1
    out2 = "\t".join(map(str, out))
    out3 = (out2 + '\n')
    tpl_12.write(out3)

tpl_12.close()