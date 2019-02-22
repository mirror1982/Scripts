import codecs

players17_old = codecs.open('work/players17.txt', 'r', 'utf_16')
players17_new = codecs.open('work/new_players17.txt', 'r', 'utf_16')
players17_hyb = codecs.open('ready/players.txt', 'w', 'utf_16')
list_old = []
list_new = []
list_hyb = []
list_filt = []

for line in players17_old:
    line = line.strip().split('\t')
    list_old.append(line)

for line2 in players17_new:
    line2 = line2.strip().split('\t')
    list_new.append(line2)

for l in list_old:
    for i in list_new:
        if l[85] == i[85]:
            l[36] = i[36]
            l[54] = i[54]
            l[97] = i[97]
            l[99] = i[99]
            list_new.remove(i)

list_filt = list_old + list_new

pid = set()
count = 0
for x in list_filt:
    if x[85] in pid:
        count += 1
        continue
    pid.add(x[85])
    list_hyb.append(x)

print count

for i in list_hyb:
    out2 = "\t".join(map(str, i))
    out3 = (out2 + '\n')
    players17_hyb.write(out3)

players17_hyb.close()
