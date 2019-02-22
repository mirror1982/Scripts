import sys, codecs
reload(sys)
sys.setdefaultencoding('utf8')

kits_16 = codecs.open("work/teamkits16.txt", 'r', 'utf_16')
kits_18 = codecs.open("work/teamkits18_add.txt", 'r', 'utf_16')
kits_18_new = codecs.open('work/new_teamkits18.txt', 'w', 'utf_16')

list_18 = []
list_18_spec = []
list_16 = []
index_18 = []
index_16 = []

for line in kits_18:
    line = line.strip().split('\t')
    list_18.append(line)

for line2 in kits_16:
    line2 = line2.strip().split('\t')
    list_16.append(line2)

for l in list_18[0]:
    for l2 in list_16[0]:
        if l == l2:
            index_18.append(list_18[0].index(l)), index_16.append(list_16[0].index(l2))

for l, l2 in zip(list_18, list_16):
    for n, n2 in zip(index_18, index_16):
        l[n] = l2[n2]

for i in list_18:
    out2 = "\t".join(map(str, i))
    out3 = (out2 + '\n')
    kits_18_new.write(out3)

kits_18.close()
kits_18_new.close()
kits_16.close()
