import sys, codecs
reload(sys)
sys.setdefaultencoding('utf8')


teams_16 = codecs.open("work/teams16.txt", 'r', 'utf_16')
teams_12 = codecs.open('work/new_teams12.txt', 'w', 'utf_16')


for column in teams_16:
    column = column.strip().split('\t')

    out = list(column[0:8] + column[9:15] + column[17:22] + column[26:27] + column[28:29] + column[31:33] + column[36:37] + column[38:39] + column[40:43] + column[44:46] + column[48:55] + column[56:57] + column[58:65])

    out2 = "\t".join(map(str, out))
    out3 = (out2 + '\n')
    teams_12.write(out3)

teams_12.close()
teams_16.close()
