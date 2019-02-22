import codecs

players12_old = codecs.open('players.txt', 'r', 'utf_16')
players12_new = codecs.open('new_players12.txt', 'r', 'utf_16')
tpl = codecs.open('teamplayerlinks.txt', 'r', 'utf_16')
players12_upd = codecs.open('players_upd.txt', 'w', 'utf_16')


list_old = []
list_new = []
list_tpl = []
pid = []
idl = []

for line in players12_old:
    line = line.strip().split('\t')
    list_old.append(line)

for line2 in players12_new:
    line2 = line2.strip().split('\t')
    list_new.append(line2)

for line3 in tpl:
    line3 = line3.strip().split('\t')
    list_tpl.append(line3)

tid = '247'

for i in list_tpl:
    if i[3] == tid:
        pid.append(i[4])

print pid

for l in list_new:
    for i in pid:
        if l[82] == str(i):
            idl.append(l)

for l in list_old:
    for i in pid:
        if l[82] == str(i):
            list_old.remove(l)

list_old.extend(idl)

for i in list_old:
    out2 = "\t".join(map(str, i))
    out3 = (out2 + '\n')
    players12_upd.write(out3)

players12_upd.close()
