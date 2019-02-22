import codecs

players12_old = codecs.open('work/players12.txt', 'r', 'utf_16')
players12_new = codecs.open('work/new_players12.txt', 'r', 'utf_16')
players12_hyb = codecs.open('ready/players.txt', 'w', 'utf_16')
list_old = []
list_new = []
list_hyb = []

for line in players12_old:
    line = line.strip().split('\t')
    list_old.append(line)


pid = set()

for x in list_old:
    if x[82] in pid:
        continue
    pid.add(x[82])
    list_hyb.append(x)


for i in list_hyb:
    out2 = "\t".join(map(str, i))
    out3 = (out2 + '\n')
    players12_hyb.write(out3)

players12_hyb.close()