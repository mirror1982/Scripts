import sys, codecs
reload(sys)
sys.setdefaultencoding('utf8')

players18_old = codecs.open('players.txt', 'r', 'utf_16')
players18_new = codecs.open('new_players.txt', 'r', 'utf_16')
players18_upd = codecs.open('players_upd.txt', 'w', 'utf_16')
tpl = codecs.open('teamplayerlinks.txt', 'r', 'utf_16')
list_old = []
list_new = []
idl = []
pid = []
list_tpl = []

for line in players18_old:
    line = line.strip().split('\t')
    list_old.append(line)

for line2 in players18_new:
    line2 = line2.strip().split('\t')
    list_new.append(line2)

for line3 in tpl:
    line3 = line3.strip().split('\t')
    list_tpl.append(line3)

tid = '100769'

for i in list_tpl:
    if i[7] == tid:
        pid.append(str(i[13]))

#ID = [192086]

for l in list_new:
    for i in pid:
        if l[93] == str(i):
            idl.append(l)

for l in list_old:
    for i in pid:
        if l[93] == str(i):
            list_old.remove(l)

list_old.extend(idl)

for i in list_old:
    out2 = "\t".join(map(str, i))
    out3 = (out2 + '\n')
    players18_upd.write(out3)

players18_upd.close()
