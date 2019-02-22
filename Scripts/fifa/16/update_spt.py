import codecs

teams12_old = codecs.open('teams12.txt', 'r', 'utf_16')
teams12_new = codecs.open('new_teams12.txt', 'r', 'utf_16')
teams12_spt = codecs.open('spt_teams12.txt', 'w', 'utf_16')
list_old = []
list_new = []
list_hyb = []

for line in teams12_old:
    line = line.strip().split('\t')
    list_old.append(line)

for line2 in teams12_new:
    line2 = line2.strip().split('\t')
    list_new.append(line2)

for l in list_old:
    for i in list_new:
        if l[26] == i[26]:
            l[22] = i[22]
            l[23] = i[23]
            l[25] = i[25]
            l[29] = i[29]
            l[38] = i[38]
            l[39] = i[39]


list_hyb = list_old

for i in list_hyb:
    out2 = "\t".join(map(str, i))
    out3 = (out2 + '\n')
    teams12_spt.write(out3)

teams12_spt.close()