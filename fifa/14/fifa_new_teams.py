import codecs

teams12_old = codecs.open('D:/Scripts/fifa/teams12.txt', 'r', 'utf_16')
teams12_new = codecs.open('D:/Scripts/fifa/new_teams12.txt', 'r', 'utf_16')
teams12_hyb = codecs.open('D:/Scripts/fifa/hyb_teams12.txt', 'w', 'utf_16')
list_old = []
list_new = []

for line in teams12_old:
    line = line.strip().split('\t')
    list_old.append(line)

for line2 in teams12_new:
    line2 = line2.strip().split('\t')
    list_new.append(line2)

for l in list_old:
    for i in list_new:
        if l[26] == i[26]:
            list_new.remove(i)

list_hyb = list_old + list_new

for i in list_hyb:
    out2 = "\t".join(map(str, i))
    out3 = (out2 + '\n')
    teams12_hyb.write(out3)

teams12_hyb.close()