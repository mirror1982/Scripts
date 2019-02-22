import codecs

ltl_16 = codecs.open("work/leagueteamlinks16.txt", 'r', 'utf_16')
ltl_17 = codecs.open('ready/leagueteamlinks.txt', 'w', 'utf_16')


for column in ltl_16:
    column = column.strip().split('\t')

    out = list(column[0:22] + column[23:36])


    out2 = "\t".join(map(str, out))
    out3 = (out2 + '\n')
    ltl_17.write(out3)

ltl_17.close()
ltl_16.close()
