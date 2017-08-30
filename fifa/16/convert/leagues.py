import sys, codecs
reload(sys)
sys.setdefaultencoding('utf8')

leagues_16 = codecs.open("work/leagues16.txt", 'r', 'utf_16')
leagues_12 = codecs.open('ready/leagues.txt', 'w', 'utf_16')

for column in leagues_16:

    column = column.strip().split('\t')
    out = list(column[0:5])

    if out[3] == '2136':
        continue

    if out[4] == 'leaguetimeslice':
        out[4] = 'buildupplay'
    else:
        out[4] = '3'

    out2 = "\t".join(map(str, out))
    out3 = (out2 + '\n')
    leagues_12.write(out3)

out = ['217', 'Tournaments', '3', '310', '1']
out2 = "\t".join(map(str, out))
out3 = (out2 + '\n')
leagues_12.write(out3)

leagues_16.close()
leagues_12.close()
