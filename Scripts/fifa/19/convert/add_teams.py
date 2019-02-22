import sys, codecs
reload(sys)
sys.setdefaultencoding('utf8')

teams_16 = codecs.open("work/teams16.txt", 'r', 'utf_16')
teams_18 = codecs.open("work/teams18.txt", 'r', 'utf_16')
teams_18_add = codecs.open("work/teams18_add.txt", 'w', 'utf_16')


list_18 = []
list_18_add = []
list_16 = []

for line0 in teams_18:
    line0 = line0.strip().split('\t')
    list_18.append(line0)

for line2 in teams_16:
    line2 = line2.strip().split('\t')
    list_16.append(line2)

dif = len(list_16) - len(list_18)

for l in range(dif):
    list_18.append(list_18[l+1])

for i in list_18:
    out2 = "\t".join(map(str, i))
    out3 = (out2 + '\n')
    teams_18_add.write(out3)

teams_18_add.close()
teams_18.close()
teams_16.close()
