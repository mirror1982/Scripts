import sys, codecs
reload(sys)
sys.setdefaultencoding('utf8')

players16 = codecs.open('work/players16.txt', 'r', 'utf_16')
players17 = codecs.open('work/new_players17.txt', 'w', 'utf_16')

for column in players16:
    column = column.strip().split('\t')
    out = list(column[0:11] + column[12:27] + column[17:18] + column[27:29] + column[17:18] + column[29:67] + column[17:18] + column[67:105])

    if out[26] == 'isretiring':
        out.pop(26)
        out.insert(26, 'composure')

    if out[29] == 'isretiring':
        out.pop(29)
        out.insert(29, 'animpenaltiesapproachcode')

    if out[68] == 'isretiring':
        out.pop(68)
        out.insert(68, 'modifier')

    if out[26] != 'composure':
        out.pop(26)
        out.insert(26, '80')

    if out[29] != 'animpenaltiesapproachcode':
        out.pop(29)
        out.insert(29, '1')

    if out[68] != 'modifier':
        out.pop(68)
        out.insert(68, '1')

    out2 = "\t".join(map(str, out))
    out3 = (out2 + '\n')
    players17.write(out3)

players17.close()
players16.close()
