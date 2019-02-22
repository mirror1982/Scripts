import codecs

form_14 = codecs.open("formations14.txt", 'r', 'utf_16')
form_12 = codecs.open('form_12.txt', 'w', 'utf_16')
tpl_14 = codecs.open("teamplayerlinks14.txt", 'r', 'utf_16')
tpl_12 = codecs.open('tpl_12.txt', 'w', 'utf_16')

count = -1
for column in form_14:
    count += 1
    column = column.strip().split('\t')

    out = list(column[0:4] + column[5:16] + column[17:18] + column[19:26] + column[25:26] + column[26:80] + column[81:87])

    if out[23] == 'formationname':
        out.pop(23)
        out.insert(23, 'formationfullname')

    if out[68] != 'formationid':
        out.pop(68)
        out.insert(68, count)

    out2 = "\t".join(map(str, out))
    out3 = (out2 + '\n')
    form_12.write(out3)

form_12.close()
form_14.close()

out = None

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
tpl_14.close()