import sys
import codecs
import re
reload(sys)
sys.setdefaultencoding('utf8')

players = codecs.open("players.txt", 'r', 'utf_16')

list_pl = []

for line in players:
    line = line.strip().split('\t')
    list_pl.append(line)

print len(list_pl)

ind_name = 'playerid'

for i in list_pl:
    for ind in range(0, len(list_pl[1])):
        if re.findall(ind_name, i[ind]):
            index = ind

print index
list_hyb = list()
pid = set()
count = 0
for x in list_pl:
    if x[index] in pid:
        print x[index]
        count += 1
        continue
    pid.add(x[index])
    list_hyb.append(x)

print count
