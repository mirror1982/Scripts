import codecs

players14 = codecs.open('players14.txt', 'r', 'utf_16')
players12 = codecs.open('new_players12.txt', 'w', 'utf_16')
pl_names14 = codecs.open("playernames14.txt", 'r')
pl_names12 = codecs.open('pl_names12.txt', 'w', 'utf_16')


item = 80

for column in players14:
        column = column.strip().split('\t')
        out = list(column[0:6] + column[5:6] + column[6:14] + column[13:14] + column[14:22] + column[24:90] + column[91:92] + column[93:103])

        if out[6] == 'curve':
            out.pop(6)
            out.insert(6, 'tacticalawareness')

        if out[15] == 'faceposercode':
            out.pop(15)
            out.insert(15, 'perfconsistencytype')

        if out[6] != 'tacticalawareness':
            out.pop(6)
            out.insert(6, item)

        if out[15] != 'perfconsistencytype':
            out.pop(15)
            out.insert(15, item)

        out2 = "\t".join(map(str, out))
        out3 = (out2 + '\n')
        players12.write(out3)

players12.close()
players14.close()

out = None

#for column in pl_names14:
#    column = column.strip().split('\t')
#    out = list(column[0:1]+column[2:3])
#    out2 = "\t".join(map(str, out))
#    out3 = (out2 + '\n')
#    out4 = unicode(out3)
#    pl_names12.write(out4)

#pl_names12.close()
#pl_names14.close()