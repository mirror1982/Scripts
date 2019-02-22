import sys, codecs
reload(sys)
sys.setdefaultencoding('utf8')

form_16 = codecs.open("work/formations16.txt", 'r', 'utf_16')
form_18_spec = codecs.open("work/formations18.txt", 'r', 'utf_16')
form_18 = codecs.open("work/formations18_add.txt", 'r', 'utf_16')
form_18_new = codecs.open('ready/formations.txt', 'w', 'utf_16')

list_18 = []
list_18_spec = []
list_16 = []
list_fin = []
list_set = []
index_18 = []
index_16 = []

for line in form_18:
    line = line.strip().split('\t')
    list_18.append(line)

for line2 in form_16:
    line2 = line2.strip().split('\t')
    list_16.append(line2)

for line3 in form_18_spec:
    line3 = line3.strip().split('\t')
    list_18_spec.append(line3)

for l in list_18[0]:
    for l2 in list_16[0]:
        if l == l2:
            index_18.append(list_18[0].index(l)), index_16.append(list_16[0].index(l2))

for l, l2 in zip(list_18, list_16):
    for n, n2 in zip(index_18, index_16):
        l[n] = l2[n2]

tid = set()
for x in list_18:
    if x[54] in tid:
        continue
    tid.add(x[48])
    list_set.append(x)

list_fin = list_18_spec[0:13] + list_set[2:]

count = -1
for g in list_fin:
    count += 1
    if g[56] != 'formationid':
        g[56] = count

for i in list_fin:
    out2 = "\t".join(map(str, i))
    out3 = (out2 + '\n')
    form_18_new.write(out3)

form_18.close()
form_18_spec.close()
form_18_new.close()
form_16.close()
