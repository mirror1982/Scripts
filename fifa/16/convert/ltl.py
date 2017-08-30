import codecs

ltl_16 = codecs.open("work/leagueteamlinks16.txt", 'r', 'utf_16')
ltl_12 = codecs.open('ready/leagueteamlinks.txt', 'w', 'utf_16')


for column in ltl_16:
    column = column.strip().split('\t')

    out = list(column[12:15] + column[19:20] + column[21:22] + column[1:2])

    if out[5] == 'previousyeartableposition': out[5] = 'tableposition'

    out2 = "\t".join(map(str, out))
    out3 = (out2 + '\n')
    ltl_12.write(out3)

ltl_12.close()
ltl_16.close()
