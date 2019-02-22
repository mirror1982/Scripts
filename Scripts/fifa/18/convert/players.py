import sys, codecs
reload(sys)
sys.setdefaultencoding('utf8')

players_16 = codecs.open("work/players16.txt", 'r', 'utf_16')
players_18 = codecs.open("work/players18_add.txt", 'r', 'utf_16')
# players_18_new = codecs.open('work/new_players18.txt', 'w', 'utf_16')
players_18_new = codecs.open('ready/players.txt', 'w', 'utf_16')

list_18 = []
list_18_spec = []
list_16 = []
index_18 = []
index_16 = []

for line in players_18:
    line = line.strip().split('\t')
    list_18.append(line)

for line2 in players_16:
    line2 = line2.strip().split('\t')
    list_16.append(line2)

for l in list_18[0]:
    for l2 in list_16[0]:
        if l == l2:
            index_18.append(list_18[0].index(l)), index_16.append(list_16[0].index(l2))

for l, l2 in zip(list_18, list_16):
    for n, n2 in zip(index_18, index_16):
        l[n] = l2[n2]

for i in list_18:
    out2 = "\t".join(map(str, i))
    out3 = (out2 + '\n')
    players_18_new.write(out3)

players_18.close()
players_18_new.close()
players_16.close()
