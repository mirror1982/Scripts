import codecs

players12_old = codecs.open('players12.txt', 'r', 'utf_16')
players12_new = codecs.open('new_players12.txt', 'r', 'utf_16')
players12_hyb = codecs.open('hyb_players12.txt', 'w', 'utf_16')
list_old = []
list_new = []
list_hyb = []

for line in players12_old:
    line = line.strip().split('\t')
    list_old.append(line)

for line2 in players12_new:
    line2 = line2.strip().split('\t')
    list_new.append(line2)

for l in list_old:
    for i in list_new:
        if l[82] == i[82]:
            l[37] = i[37]
            l[53] = i[53]
            l[91] = i[91]
            l[93] = i[93]
            list_new.remove(i)

list_hyb = list_old + list_new

for i in list_hyb:
    out2 = "\t".join(map(str, i))
    out3 = (out2 + '\n')
    players12_hyb.write(out3)

players12_hyb.close()