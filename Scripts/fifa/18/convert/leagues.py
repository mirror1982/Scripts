import sys, codecs
reload(sys)
sys.setdefaultencoding('utf8')

leagues_16 = codecs.open("work/leagues16.txt", 'r', 'utf_16')
leagues_18 = codecs.open("work/leagues18_add.txt", 'r', 'utf_16')
leagues_18_new = codecs.open('ready/leagues.txt', 'w', 'utf_16')

list_18 = []
list_18_spec = []
list_16 = []
index_18 = []
index_16 = []

for line in leagues_18:
    line = line.strip().split('\t')
    list_18.append(line)

for line2 in leagues_16:
    line2 = line2.strip().split('\t')
    list_16.append(line2)

for l in list_18[0]:
    for l2 in list_16[0]:
        if l == l2:
            index_18.append(list_18[0].index(l)), index_16.append(list_16[0].index(l2))

for l, l2 in zip(list_18, list_16):
    for n, n2 in zip(index_18, index_16):
        l[n] = l2[n2]

for i in list_18:
    out2 = "\t".join(map(str, i))
    out3 = (out2 + '\n')
    leagues_18_new.write(out3)

leagues_18.close()
leagues_18_new.close()
leagues_16.close()
