import codecs

players16 = codecs.open('players16.txt', 'r', 'utf_16')
players12 = codecs.open('new_players12.txt', 'w', 'utf_16')

item = 80
out = []

for column in players16:
        column = column.strip().split('\t')
        if column[51] != '1':
            out = list(column[41:42] + column[72:73] + column[0:4] + column[3:4] + column[4:12] + column[11:12] + column[12:20] + column[22:41] + column[42:51] + column[52:72] + column[73:91] + column[93:94] + column[95:105])

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

            if out[68] != 'eyecolorcode' and int(out[68]) == 8:
                out[68] = '6'
            if out[68] != 'eyecolorcode' and int(out[68]) == 9:
                out[68] = '3'
            if out[68] != 'eyecolorcode' and int(out[68]) == 10:
                out[68] = '6'

            if out[4] != 'facialhairtypecode' and int(out[4]) > 7:
                out[4] = '0'

            for h in range(2513, 2519):
                if out[36] != 'headtypecode' and out[36] == str(h):
                        out[36] = '1'

        out2 = "\t".join(map(str, out))
        out3 = (out2 + '\n')
        players12.write(out3)

players12.close()
players16.close()
