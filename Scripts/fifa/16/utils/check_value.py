import codecs
import re


players12_act = codecs.open('players12.txt', 'r', 'utf_16')
names = codecs.open('playernames.txt', 'r', 'utf_16')
lst = []
nms = []
attr = {}

for line in players12_act:
    line = line.strip().split('\t')
    lst.append(line)

for line in names:
    line = line.strip().split('\t')
    nms.append(line)

for i in lst:
    for ind in range(0, len(lst[1])):
        if re.findall(r'head', i[ind]):
            attr[ind] = i[ind]
    if i[82] == '213000':
        nm = i[37]
        lan = i[53]
        for k, v in attr.items():
            print v,  i[k]

for i in nms:
    if i[-1] == nm: nml = i[0]
    if i[-1] == lan: lnl = i[0]

print nml, lnl
