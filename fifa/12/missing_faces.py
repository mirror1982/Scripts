import codecs

players12 = codecs.open('players_original.txt', 'r', 'utf_16')
players13 = codecs.open('players13.txt', 'r', 'utf_16')
players13_new_miss = codecs.open('players13_new_miss.txt', 'w', 'utf_16')
players12_new_miss = codecs.open('players12_new_miss.txt', 'w', 'utf_16')
lst12 = []
list_new12 = []
lst13 = []
list_new13 = []

for line in players12:
    line = line.strip().split('\t')
    lst12.append(line)

for l in lst12:
    if l[72] == "headclasscode" or l[72] == "0":
        list_new12.append(l)

for line in players13:
    line = line.strip().split('\t')
    lst13.append(line)

for l in lst13:
    if l[72] == "headclasscode" or l[72] == "0":
        list_new13.append(l)

#for l in list_new12:
#    for i in list_new13:
#        if l[82] == i[82] and l[82] != 'playerid':
#            l[37] = i[37]
#            l[53] = i[53]
#            l[91] = i[91]
#            l[93] = i[93]
#            list_new13.remove(i)

#
# for i in list_new12:
#     out2 = "\t".join(map(str, i))
#     out3 = (out2 + '\n')
#     players12_new_miss.write(out3)
#
# players12_new_miss.close()

for l in list_new13:
    for i in list_new12:
        if l[82] == i[82] and l[82] != 'playerid':
            i[37] = l[37]
            i[53] = l[53]
            i[91] = l[91]
            i[93] = l[93]
            list_new12.remove(i)

for i in list_new13:
   out2 = "\t".join(map(str, i))
   out3 = (out2 + '\n')
   players13_new_miss.write(out3)

players13_new_miss.close()