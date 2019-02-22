import sys, codecs
reload(sys)
sys.setdefaultencoding('utf8')

form_16 = codecs.open("work/formations16.txt", 'r', 'utf_16')
form_12_spec = codecs.open("work/formations12.txt", 'r', 'utf_16')
form_12 = codecs.open("work/formations12_add.txt", 'r', 'utf_16')
form_12_new = codecs.open('ready/formations.txt', 'w', 'utf_16')

list_12 = []
list_12_spec = []
list_16 = []
list_fin = []
index_12 = []
index_16 = []

for line in form_12:
    line = line.strip().split('\t')
    list_12.append(line)

for line2 in form_16:
    line2 = line2.strip().split('\t')
    list_16.append(line2)

for line3 in form_12_spec:
    line3 = line3.strip().split('\t')
    list_12_spec.append(line3)

for l in list_12[0]:
    for l2 in list_16[0]:
        if l == l2:
            index_12.append(list_12[0].index(l)), index_16.append(list_16[0].index(l2))

for l, l2 in zip(list_12, list_16):
    for n, n2 in zip(index_12, index_16):
        l[n] = l2[n2]

for i in range(5):
    list_12[i] = list_12_spec[i]

tid = set()
for x in list_12:
    if x[65] in tid and x[65] != '-1':
        continue
    tid.add(x[65])
    list_fin.append(x)

count = -1
for g in list_fin:
    count += 1
    if g[68] != 'formationid':
        g[68] = count

for i in list_fin:
    out2 = "\t".join(map(str, i))
    out3 = (out2 + '\n')
    form_12_new.write(out3)

form_12.close()
form_12_spec.close()
form_12_new.close()
form_16.close()
