import sys, codecs
reload(sys)
sys.setdefaultencoding('utf8')

teamkits_18 = codecs.open("teamkits.txt", 'r', 'utf_16')
teamkits_16 = codecs.open("teamkits16.txt", 'r', 'utf_16')
# teamkits_16_new = codecs.open('work/new_teamkits16.txt', 'w', 'utf_16')
teamkits_16_new = codecs.open('teamkits16_new.txt', 'w', 'utf_16')

list_16 = []
list_16_spec = []
list_18 = []
index_16 = []
index_18 = []

for line in teamkits_16:
    line = line.strip().split('\t')
    list_16.append(line)

for line2 in teamkits_18:
    line2 = line2.strip().split('\t')
    list_18.append(line2)

for l in list_16[0]:
    for l2 in list_18[0]:
        if l == l2:
            index_16.append(list_16[0].index(l)), index_18.append(list_18[0].index(l2))

for l, l2 in zip(list_16, list_18):
    for n, n2 in zip(index_16, index_18):
        l[n] = l2[n2]

pid = set()
list_hyb = []
count = 0
for x in list_16:
    if x[83] in pid:
        count += 1
        continue
    pid.add(x[83])
    list_hyb.append(x)

print count

for i in list_hyb:
    out2 = "\t".join(map(str, i))
    out3 = (out2 + '\n')
    teamkits_16_new.write(out3)

teamkits_16.close()
teamkits_16_new.close()
teamkits_18.close()
