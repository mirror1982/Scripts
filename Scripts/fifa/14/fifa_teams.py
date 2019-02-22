import codecs

teams_14 = codecs.open("teams14.txt", 'r', 'utf_16')
teams_12 = codecs.open('teams_12.txt', 'w', 'utf_16')


for column in teams_14:
    column = column.strip().split('\t')

    out = list(column[0:8] + column[9:15] + column[16:21] + column[25:26] + column[27:28] + column[30:32] + column[35:36] + column[37:38] + column[39:42] + column[43:45] + column[46:53] + column[54:55] + column[56:63])

    out2 = "\t".join(map(str, out))
    out3 = (out2 + '\n')
    #out4 = unicode(out3, 'utf_8')
    teams_12.write(out3)

teams_12.close()
teams_14.close()