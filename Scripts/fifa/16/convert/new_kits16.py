import codecs

kits_16 = codecs.open("work/teamkits16.txt", 'r', 'utf_16')
kits_12 = codecs.open('work/new_kits12.txt', 'w', 'utf_16')


for column in kits_16:
    column = column.strip().split('\t')

    out = list(column[0:28] + column[29:30] + column[31:36])

    out2 = "\t".join(map(str, out))
    out3 = (out2 + '\n')
    kits_12.write(out3)

kits_12.close()
kits_16.close()
