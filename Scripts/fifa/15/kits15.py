import codecs

kits_15 = codecs.open("teamkits15.txt", 'r', 'utf_16')
kits_12 = codecs.open('new_kits12.txt', 'w', 'utf_16')


for column in kits_15:
    column = column.strip().split('\t')

    out = list(column[0:28] + column[29:30] + column[31:36])

    out2 = "\t".join(map(str, out))
    out3 = (out2 + '\n')
    kits_12.write(out3)

kits_12.close()
kits_15.close()