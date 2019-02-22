import codecs

players13 = codecs.open('players16.txt', 'r', 'utf_16')
players13_new = codecs.open('players16_new.txt', 'w', 'utf_16')
lst = []
list_new = []

for line in players13:
    line = line.strip().split('\t')
    lst.append(line)

for l in lst:
    if l[73] == "headclasscode" or l[73] == "0" and l[51] != '1':
        list_new.append(l)

for i in list_new:
    out2 = "\t".join(map(str, i))
    out3 = (out2 + '\n')
    players13_new.write(out3)

players13_new.close()
