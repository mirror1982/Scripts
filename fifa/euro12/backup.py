import codecs

players12 = codecs.open('D:/Scripts/fifa/euro12/players12.txt', 'r', 'utf_16')
teams_euro = codecs.open('D:/Scripts/fifa/euro12/teams_euro.txt', 'r', 'utf_16')
tpl12 = codecs.open('D:/Scripts/fifa/euro12/teamplayerlinks.txt', 'r', 'utf_16')
form12 = codecs.open('D:/Scripts/fifa/euro12/formations.txt', 'r', 'utf_16')

players_euro = codecs.open('D:/Scripts/fifa/euro12/players_euro.txt', 'w', 'utf_16')
tpl_euro = codecs.open('D:/Scripts/fifa/euro12/tpl_euro.txt', 'w', 'utf_16')
form_euro = codecs.open('D:/Scripts/fifa/euro12/form_euro.txt', 'w', 'utf_16')

players_list = []
players_new = []

tpl_list = []
tpl_new = []

teams_list = []
teams_new = []

form_list = []
form_new = []

for line in players12:
    line = line.strip().split('\t')
    players_list.append(line)

for line in tpl12:
    line = line.strip().split('\t')
    tpl_list.append(line)

for line in teams_euro:
    line = line.strip().split('\t')
    teams_list.append(line)

for line in form12:
    line = line.strip().split('\t')
    form_list.append(line)


for l in tpl_list:
    for tid in teams_list:
        if l[3] == tid[0]:
            players_new.append(l[4])
            tpl_new.append(l)

for l in form_list:
    for tid in teams_list:
        if l[54] == tid[0]:
            form_new.append(l)

for l in teams_list:
    for i in players_new:
        if l[82] == i:
            players_new.append(l)

for i in players_new:
    out2 = "\t".join(map(str, i))
    out3 = (out2 + '\n')
    players_euro.write(out3)

for i2 in tpl_new:
    out2 = "\t".join(map(str, i2))
    out3 = (out2 + '\n')
    tpl_euro.write(out3)

for i3 in form_new:
    out2 = "\t".join(map(str, i3))
    out3 = (out2 + '\n')
    form_euro.write(out3)

players_euro.close()
tpl_euro.close()
form_euro.close()
