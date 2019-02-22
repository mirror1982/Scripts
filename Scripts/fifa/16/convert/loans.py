import codecs

loans_16 = codecs.open("work/playerloans16.txt", 'r', 'utf_16')
loans_12 = codecs.open('ready/playerloans.txt', 'w', 'utf_16')


for column in loans_16:
    column = column.strip().split('\t')

    out = list(column[2:3] + column[0:1] + column[1:2])

    out2 = "\t".join(map(str, out))
    out3 = (out2 + '\n')
    loans_12.write(out3)

loans_12.close()
loans_16.close()