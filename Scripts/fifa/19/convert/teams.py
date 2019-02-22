import sys, codecs
reload(sys)
sys.setdefaultencoding('utf8')

teams_16 = codecs.open("work/teams16.txt", 'r', 'utf_16')
teams_18 = codecs.open("work/teams18_add.txt", 'r', 'utf_16')
teams_18_new = codecs.open('ready/teams.txt', 'w', 'utf_16')

list_18 = []
list_18_spec = []
list_16 = []
index_18 = []
index_16 = []

for line in teams_18:
    line = line.strip().split('\t')
    list_18.append(line)

for line2 in teams_16:
    line2 = line2.strip().split('\t')
    list_16.append(line2)

for l in list_18[0]:
    for l2 in list_16[0]:
        if l == l2:
            index_18.append(list_18[0].index(l)), index_16.append(list_16[0].index(l2))

for l, l2 in zip(list_18, list_16):
    for n, n2 in zip(index_18, index_16):
        l[n] = l2[n2]

pid = set()
list_hyb = list()
count = 0
for x in list_18:
    if x[41] in pid:
        count += 1
        continue
    pid.add(x[41])
    list_hyb.append(x)

print count

for i in list_hyb:
    out2 = "\t".join(map(str, i))
    out3 = (out2 + '\n')
    teams_18_new.write(out3)

teams_18.close()
teams_18_new.close()
teams_16.close()
