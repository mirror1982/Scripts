import codecs

form_16 = codecs.open("formations16.txt", 'r', 'utf_16')
form_12 = codecs.open("formations12.txt", 'r', 'utf_16')
form_12_temp = codecs.open("formations12_temp.txt", 'w', 'utf_16')
form_12_new = codecs.open('ready/formations.txt', 'w', 'utf_16')


list_12 = []
list_12_old = []
list_16 = []
index_12 = []
index_16 = []

for line0 in form_12:
    line0 = line0.strip().split('\t')
    list_12_old.append(line0)

for line2 in form_16:
    line2 = line2.strip().split('\t')
    list_16.append(line2)

dif = len(list_16) - len(list_12_old)
print dif

count = len(list_12_old) - 1

for l in range(dif):
    list_12_old.append(list_12_old[l])


count = -1
for g in list_12:
    count += 1
    if g[68] != 'formationid':
        g[68] = count

for i in list_12_old:
    out2 = "\t".join(map(str, i))
    out3 = (out2 + '\n')
    form_12_temp.write(out3)

form_12_temp.close()

form_12_temp = codecs.open("formations12_temp.txt", 'r', 'utf_16')

for line in form_12_temp:
    line = line.strip().split('\t')
    list_12.append(line)

for l in list_12[0]:
    for l2 in list_16[0]:
        if l == l2:
            index_12.append(list_12[0].index(l)), index_16.append(list_16[0].index(l2))

for l, l2 in zip(list_12, list_16):
    for n, n2 in zip(index_12, index_16):
        l[n] = l2[n2]

# form_12 = codecs.open("formations12.txt", 'r', 'utf_16')
# for line3 in form_12:
#     line3 = line3.strip().split('\t')
#     list_12_spec.append(line3)
#
# for i in range(5):
#     list_12[i] = list_12_spec[i]
#
# count = -1
# for g in list_12:
#     count += 1
#     if g[68] != 'formationid':
#         g[68] = count
#
for i in list_12:
    out2 = "\t".join(map(str, i))
    out3 = (out2 + '\n')
    form_12_new.write(out3)

form_12.close()
form_12_new.close()
form_16.close()

execfile("missed_formations.py")
