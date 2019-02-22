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

for l in list_new:
    for i in list_old:
        if l[93] == i[93]:
            l[0] = i[0]
            l[1] = i[1]
            l[2] = i[2]
            l[3] = i[3]
            l[55] = i[55]
            l[82] = i[82]

list_filt = list_new

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
