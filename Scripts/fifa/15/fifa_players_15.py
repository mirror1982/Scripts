import codecs

players15 = codecs.open('players15.txt', 'r', 'utf_16')
players12 = codecs.open('new_players12.txt', 'w', 'utf_16')

item = 80

for column in players15:
        column = column.strip().split('\t')
        out = list(column[41:42] + column[71:72] + column[0:4] + column[3:4] + column[4:12] + column[11:12] + column[12:20] + column[22:41] + column[42:71] + column[72:90] + column[91:92] + column[93:103])

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
players15.close()
