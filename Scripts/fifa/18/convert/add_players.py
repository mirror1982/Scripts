import sys, codecs
reload(sys)
sys.setdefaultencoding('utf8')

players_16 = codecs.open("work/players16.txt", 'r', 'utf_16')
players_18 = codecs.open("work/players18.txt", 'r', 'utf_16')
players_18_add = codecs.open("work/players18_add.txt", 'w', 'utf_16')


list_18 = []
list_18_add = []
list_16 = []

for line0 in players_18:
    line0 = line0.strip().split('\t')
    list_18.append(line0)

for line2 in players_16:
    line2 = line2.strip().split('\t')
    list_16.append(line2)

dif = len(list_16) - len(list_18)
print dif

for l in range(dif):
    list_18.append(list_18[l+1])

for i in list_18:
    out2 = "\t".join(map(str, i))
    out3 = (out2 + '\n')
    players_18_add.write(out3)

players_18_add.close()
players_18.close()
players_16.close()
