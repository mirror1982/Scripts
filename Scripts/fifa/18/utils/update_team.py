import codecs

players18_old = codecs.open('players.txt', 'r', 'utf_16')
players18_new = codecs.open('new_players.txt', 'r', 'utf_16')
tpl = codecs.open('teamplayerlinks.txt', 'r', 'utf_16')
players18_upd = codecs.open('players_upd.txt', 'w', 'utf_16')


list_old = []
list_new = []
list_tpl = []
pid = []
idl = []

for line in players18_old:
    line = line.strip().split('\t')
    list_old.append(line)

for line2 in players18_new:
    line2 = line2.strip().split('\t')
    list_new.append(line2)

for line3 in tpl:
    line3 = line3.strip().split('\t')
    list_tpl.append(line3)

# for l in list_new:
#     for i in list_old:
#         if l[93] == i[93]:
#             l[0] = i[0]
#             l[1] = i[1]
#             l[2] = i[2]
#             l[3] = i[3]

tid = '100769'

for i in list_tpl:
    if i[7] == tid:
        pid.append(str(i[13]))

print pid

cnt = 0
for l in list_new:
    for i in pid:
        if l[93] == str(i):
            cnt +=1
            idl.append(l)

cnt2 = 0
for l in list_old:
    for i in pid:
        if l[93] == str(i):
            cnt2 +=1
            list_old.remove(l)

print(cnt)
list_old.extend(idl)


list_hyb = list()
pid = set()
count = 0
for x in list_old:
    if x[93] in pid:
        count += 1
        continue
    pid.add(x[93])
    list_hyb.append(x)
print count


for i in list_hyb:
    out2 = "\t".join(map(str, i))
    out3 = (out2 + '\n')
    players18_upd.write(out3)

players18_upd.close()
