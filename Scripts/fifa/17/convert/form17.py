import sys, codecs
reload(sys)
sys.setdefaultencoding('utf8')

form_16 = codecs.open("work/formations16.txt", 'r', 'utf_16')
form_17_spec = codecs.open("work/formations17.txt", 'r', 'utf_16')
form_17 = codecs.open("work/formations17_add.txt", 'r', 'utf_16')
form_17_new = codecs.open('ready/formations.txt', 'w', 'utf_16')

list_17 = []
list_17_spec = []
list_16 = []
list_fin = []
list_set = []
index_17 = []
index_16 = []

for line in form_17:
    line = line.strip().split('\t')
    list_17.append(line)

for line2 in form_16:
    line2 = line2.strip().split('\t')
    list_16.append(line2)

for line3 in form_17_spec:
    line3 = line3.strip().split('\t')
    list_17_spec.append(line3)

for l in list_17[0]:
    for l2 in list_16[0]:
        if l == l2:
            index_17.append(list_17[0].index(l)), index_16.append(list_16[0].index(l2))

for l, l2 in zip(list_17, list_16):
    for n, n2 in zip(index_17, index_16):
        l[n] = l2[n2]

tid = set()
for x in list_17:
    if x[48] in tid:
        continue
    tid.add(x[48])
    list_set.append(x)

list_fin = list_17_spec[0:13] + list_set[2:]

count = -1
for g in list_fin:
    count += 1
    if g[51] != 'formationid':
        g[51] = count

for i in list_fin:
    out2 = "\t".join(map(str, i))
    out3 = (out2 + '\n')
    form_17_new.write(out3)

form_17.close()
form_17_spec.close()
form_17_new.close()
form_16.close()
