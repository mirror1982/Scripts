import sys, codecs
reload(sys)
sys.setdefaultencoding('utf8')

teams18_old = codecs.open('work/teams18.txt', 'r', 'utf_16')
teams18_new = codecs.open('work/new_teams18.txt', 'r', 'utf_16')
teams18_hyb = codecs.open('ready/teams.txt', 'w', 'utf_16')
list_old = []
list_new = []
list_hyb = []

for line in teams18_old:
    line = line.strip().split('\t')
    list_old.append(line)

for line2 in teams18_new:
    line2 = line2.strip().split('\t')
    list_new.append(line2)

# for i in range(118998, 113013, 1):
#     for l in list_old:
#         if l[26] == str(i):
#             list_old.remove(l)
#
# for i in range(118998, 113013, 1):
#     for l in list_new:
#         if l[26] == str(i):
#             list_new.remove(l)

for l in list_old:
    for i in list_new:
        if l[52] == i[52]:
            l[57] = i[57]
            l[41] = i[41]
            l[20] = i[20]
            l[59] = i[59]
            l[72] = i[72]
            l[71] = i[71]
            l[45] = i[45]
            l[50] = i[50]
            list_new.remove(i)

list_filt = list_old + list_new

pid = set()

count = 0
for x in list_filt:
    if x[52] in pid:
        count += 1
        continue
    pid.add(x[52])
    list_hyb.append(x)

print count

for i in list_hyb:
    out2 = "\t".join(map(str, i))
    out3 = (out2 + '\n')
    teams18_hyb.write(out3)

teams18_hyb.close()
