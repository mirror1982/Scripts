import sys, codecs
reload(sys)
sys.setdefaultencoding('utf8')

teams12_old = codecs.open('work/teams12.txt', 'r', 'utf_16')
teams12_new = codecs.open('work/new_teams12.txt', 'r', 'utf_16')
teams12_hyb = codecs.open('ready/teams.txt', 'w', 'utf_16')
list_old = []
list_new = []
list_hyb = []

for line in teams12_old:
    line = line.strip().split('\t')
    list_old.append(line)

for line2 in teams12_new:
    line2 = line2.strip().split('\t')
    list_new.append(line2)

for i in range(112998, 113013, 1):
    for l in list_old:
        if l[26] == str(i):
            list_old.remove(l)

for i in range(112998, 113013, 1):
    for l in list_new:
        if l[26] == str(i):
            list_new.remove(l)

for l in list_old:
    for i in list_new:
        if l[26] == i[26]:
            l[22] = i[22]
            l[23] = i[23]
            l[25] = i[25]
            l[29] = i[29]
            l[38] = i[38]
            l[39] = i[39]
            list_new.remove(i)

list_filt = list_old + list_new

pid = set()

count = 0
for x in list_filt:
    if x[26] in pid:
        count += 1
        continue
    pid.add(x[26])
    list_hyb.append(x)

print count

for i in list_hyb:
    out2 = "\t".join(map(str, i))
    out3 = (out2 + '\n')
    teams12_hyb.write(out3)

teams12_hyb.close()
