import codecs
import re


players12_act = codecs.open('players.txt', 'r', 'utf_16')
names = codecs.open('playernames.txt', 'r', 'utf_16')
lst = []
nms = []

for line in players12_act:
    line = line.strip().split('\t')
    lst.append(line)

for line in names:
    line = line.strip().split('\t')
    nms.append(line)

for i in lst:
    if i[82] == '205897':
        nm = i[37]
        lan = i[53]
        cn = i[93]

for i in nms:
    try:
        if i[-1] == nm: nml = i[0]
        if i[-1] == lan: lnl = i[0]
        if i[-1] == cn: cnl = i[0]
    except:
        continue

try:
    if nml != '0' and lnl != '0': print nml, lnl
    if nml != '0' and lnl == '0': print nml
    if lnl != '0' and nml == '0': print lnl
    if cnl != '0': print cnl
except:
    print "ID not found"
