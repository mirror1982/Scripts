import sys, codecs
reload(sys)
sys.setdefaultencoding('utf8')


players = codecs.open('players.txt', 'r', 'utf_16')
teams = codecs.open('teams.txt', 'r', 'utf_16')
teamplayerlinks = codecs.open('teamplayerlinks.txt', 'r', 'utf_16')
wcplayers = codecs.open('wcplayers.txt', 'w', 'utf_16')

list_teams = []
list_old = []
list_new = []
list_hyb = []
list_tpl = []
list_pid = []

for line in players:
    line = line.strip().split('\t')
    list_old.append(line)

for line2 in teams:
    line2 = line2.strip().split('\t')
    list_teams.append(line2)

for line3 in teamplayerlinks:
    line3 = line3.strip().split('\t')
    list_tpl.append(line3)

for l in list_tpl:
    for i in list_teams:
        if l[7] == i[52]:
            list_pid.append(l[13])

#print len(list_pid)

for i in list_old:
    for l in list_pid:
        if i[93] == l:
            list_new.append(i)

pid = set()
count = 0
for x in list_new:
    if x[93] in pid:
        count += 1
        continue
    pid.add(x[93])
    list_hyb.append(x)

print count

for i in list_hyb:
    out2 = "\t".join(map(str, i))
    out3 = (out2 + '\n')
    wcplayers.write(out3)

wcplayers.close()
