import codecs

players18_old = codecs.open('work/players18.txt', 'r', 'utf_16')
players18_new = codecs.open('work/new_players18.txt', 'r', 'utf_16')
players18_hyb = codecs.open('ready/players.txt', 'w', 'utf_16')
list_old = []
list_new = []
list_hyb = []
list_filt = []

for line in players18_old:
    line = line.strip().split('\t')
    list_old.append(line)

for line2 in players18_new:
    line2 = line2.strip().split('\t')
    list_new.append(line2)

for l in list_old:
    for i in list_new:
        if l[93] == i[93]:
            l[0] = i[0]
            l[1] = i[1]
            l[2] = i[2]
            l[3] = i[3]
            l[48] = i[48]
            l[17] = i[17]
            l[45] = i[45]
            l[49] = i[49]
            l[111] = i[111]
            l[108] = i[108]
            l[43] = i[43]
            l[54] = i[54]
            l[85] = i[85]
            l[61] = i[61]
            l[84] = i[84]
            l[78] = i[78]
            l[77] = i[77]
            l[98] = i[98]

            list_new.remove(i)

list_filt = list_old + list_new

pid = set()
count = 0
for x in list_filt:
    if x[93] in pid:
        count += 1
        continue
    pid.add(x[93])
    list_hyb.append(x)

print count

for i in list_hyb:
    out2 = "\t".join(map(str, i))
    out3 = (out2 + '\n')
    players18_hyb.write(out3)

players18_hyb.close()
