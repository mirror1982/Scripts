import codecs

form_16 = codecs.open("formations16.txt", 'r', 'utf_16')
form_12 = codecs.open("formations12.txt", 'r', 'utf_16')
form_12_new = codecs.open('form_12_new.txt', 'w', 'utf_16')

list_12 = []
list_16 = []
index_12 = []
index_16 = []

for line, line2 in zip(form_12, form_16):
    line = line.strip().split('\t')
    line2 = line2.strip().split('\t')
    list_12.append(line)
    list_16.append(line2)

for l in list_12[0]:
    for l2 in list_16[0]:
        if l == l2:
            index_12.append(list_12[0].index(l)), index_16.append(list_16[0].index(l2))

for l, l2 in zip(list_12, list_16):
    for n, n2 in zip(index_12, index_16):
        l[n] = l2[n2]

for i in list_12:
    out2 = "\t".join(map(str, i))
    out3 = (out2 + '\n')
    form_12_new.write(out3)

form_12.close()
form_12_new.close()
form_16.close()