import sys, codecs
reload(sys)
sys.setdefaultencoding('utf8')

players12_old = codecs.open('players12.txt', 'r', 'utf_16')
players12_new = codecs.open('new_players12.txt', 'r', 'utf_16')
players12_upd = codecs.open('players_upd.txt', 'w', 'utf_16')
list_old = []
list_new = []
idl = []

for line in players12_old:
    line = line.strip().split('\t')
    list_old.append(line)

for line2 in players12_new:
    line2 = line2.strip().split('\t')
    list_new.append(line2)

ID = [231443, 231240, 227796]

for l in list_new:
    for i in ID:
        if l[82] == str(i):
            idl.append(l)

for l in list_old:
    for i in ID:
        if l[82] == str(i):
            list_old.remove(l)

list_old.extend(idl)

for i in list_old:
    out2 = "\t".join(map(str, i))
    out3 = (out2 + '\n')
    players12_upd.write(out3)

players12_upd.close()
