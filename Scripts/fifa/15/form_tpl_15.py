import codecs

form_15 = codecs.open("formations15.txt", 'r', 'utf_16')
form_12 = codecs.open('form_12.txt', 'w', 'utf_16')
tpl_15 = codecs.open("teamplayerlinks15.txt", 'r', 'utf_16')
tpl_12 = codecs.open('tpl_12.txt', 'w', 'utf_16')

count = -1
count2 = 0
for column in form_15:
    count += 1
    column = column.strip().split('\t')

    out = list(column[0:4] + column[5:16] + column[17:18] + column[19:26] + column[25:26] + column[26:27] + column[28:33] + column[34:35] + column[37:47] + column[48:50] + column[51:57] + column[58:61] + column[62:64] + column[65:66] + column[65:76] + column[77:80] + column[81:83] + column[78:79] + column[83:89] + column[90:96])

    if out[55] == 'defensivedirection_5':
        out.pop(55)
        out.insert(55, 'issweeper')
    else:
        out.pop(55)
        out.insert(55, '0')

    if out[71] == 'defensivedirection_4':
        out.pop(71)
        out.insert(71, 'relativeformationid')
    else:
        out.pop(71)
        out.insert(71, '0')

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
form_15.close()

out = None

for column in tpl_15:
    column = column.strip().split('\t')
    out0 = list(column[4:8])
    out1 = list(column[12:13])
    out = out0 + out1
    out2 = "\t".join(map(str, out))
    out3 = (out2 + '\n')
    tpl_12.write(out3)

tpl_12.close()
tpl_15.close()