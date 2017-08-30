import codecs

players16 = codecs.open('players16.txt', 'r', 'utf_16')
players12_wom = codecs.open('players12_wom.txt', 'r', 'utf_16')
players12_no_wom = codecs.open('players12_no_wom.txt', 'w', 'utf_16')
list_women = []
list_new = []
list_hyb = []

for line in players16:
    line = line.strip().split('\t')
    if line[51] == '1':
        list_women.append(line)

for line2 in players12_wom:
    line2 = line2.strip().split('\t')
    list_new.append(line2)

for l in list_women:
    for i in list_new:
        if l[83] == i[82]:
            list_new.remove(i)


for i in list_new:
    out2 = "\t".join(map(str, i))
    out3 = (out2 + '\n')
    players12_no_wom.write(out3)

players12_no_wom.close()