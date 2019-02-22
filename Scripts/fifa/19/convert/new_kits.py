import codecs

teamkits18_old = codecs.open('work/teamkits18.txt', 'r', 'utf_16')
teamkits18_new = codecs.open('work/new_teamkits18.txt', 'r', 'utf_16')
teamkits18_hyb = codecs.open('ready/teamkits.txt', 'w', 'utf_16')
list_old = []
list_new = []
list_hyb = []
list_filt = []

for line in teamkits18_old:
    line = line.strip().split('\t')
    list_old.append(line)

for line2 in teamkits18_new:
    line2 = line2.strip().split('\t')
    list_new.append(line2)

for l in list_old:
    for i in list_new:
        if l[51] == i[51] or i[43] == '2':
            list_new.remove(i)

list_filt = list_old + list_new

# pid = set()
# count = 0
# for x in list_filt:
#     if x[51] in pid:
#         count += 1
#         continue
#     pid.add(x[51])
#     list_hyb.append(x)
#
# print count

list_hyb = list_filt

for i in list_hyb:
    out2 = "\t".join(map(str, i))
    out3 = (out2 + '\n')
    teamkits18_hyb.write(out3)

teamkits18_hyb.close()
