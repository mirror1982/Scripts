import codecs

players12 = codecs.open('D:/Scripts/fifa/euro12/players12.txt', 'r', 'utf_16')
teams_euro = codecs.open('D:/Scripts/fifa/euro12/teams_euro.txt', 'r', 'utf_16')
teams12 = codecs.open('D:/Scripts/fifa/euro12/teams.txt', 'r', 'utf_16')
tpl12 = codecs.open('D:/Scripts/fifa/euro12/teamplayerlinks.txt', 'r', 'utf_16')
form12 = codecs.open('D:/Scripts/fifa/euro12/formations.txt', 'r', 'utf_16')
kits12 = codecs.open('D:/Scripts/fifa/euro12/teamkits.txt', 'r', 'utf_16')

players_euro = codecs.open('D:/Scripts/fifa/euro12/players_euro.txt', 'w', 'utf_16')
tpl_euro = codecs.open('D:/Scripts/fifa/euro12/tpl_euro.txt', 'w', 'utf_16')
form_euro = codecs.open('D:/Scripts/fifa/euro12/form_euro.txt', 'w', 'utf_16')
teams_euro_new = codecs.open('D:/Scripts/fifa/euro12/teams_euro_new.txt', 'w', 'utf_16')
kits_euro = codecs.open('D:/Scripts/fifa/euro12/teamkits_euro_new.txt', 'w', 'utf_16')

players_list = []
players_new = []
players_new2 = []

tpl_list = []
tpl_new = []

teams12_list = []
teams_list = []
teams_new = []

form_list = []
form_new = []

kits_list = []
kits_new = []

count = -1

for line in players12:
    line = line.strip().split('\t')
    players_list.append(line)

for line in tpl12:
    line = line.strip().split('\t')
    tpl_list.append(line)

for line in teams_euro:
    line = line.strip().split('\t')
    teams_list.append(line)

for line in teams12:
    line = line.strip().split('\t')
    teams12_list.append(line)

for line in form12:
    line = line.strip().split('\t')
    form_list.append(line)

for line in kits12:
    line = line.strip().split('\t')
    kits_list.append(line)



for l in tpl_list:
    for tid in teams_list:
        if l[3] == tid[26] and l[3] != '111592':
            players_new.append(l[4])
            tpl_new.append(l)

for tid in teams_list:
    for l in teams12_list:
        if tid[26] == l[26]:
            teams_new.append(l)

print teams_new

count = -1
for i in tpl_new:
    count += 1
    if i[2] != 'artificialkey':
        i.pop(2)
        i.insert(2, count)

for l in form_list:
    if l[65] == '-1':
        form_new.append(l)
    for tid in teams_list:
        if l[65] == tid[26]:
            form_new.append(l)


count2 = -1
for i in form_new:
    count2 += 1
    if i[68] != 'formationid':
        i.pop(68)
        i.insert(68, count2)

for l in players_list:
    for i in players_new:
        if l[82] == i:
            players_new2.append(l)


for i in players_new2:
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

for i3 in teams_new:
    out2 = "\t".join(map(str, i3))
    out3 = (out2 + '\n')
    teams_euro_new.write(out3)

players_euro.close()
tpl_euro.close()
form_euro.close()
