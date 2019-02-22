import codecs

teamkits18 = codecs.open('teamkits18.txt', 'r', 'utf_16')
teamkitswc = codecs.open('teamkits_wc.txt', 'r', 'utf_16')
teamkits_new = codecs.open('teamkits.txt', 'w', 'utf_16')
list_18 = []
list_wc = []
list_hyb = []
list_filt = []

for line in teamkits18:
    line = line.strip().split('\t')
    list_18.append(line)

for line2 in teamkitswc:
    line2 = line2.strip().split('\t')
    list_wc.append(line2)

for l in list_wc:
    if l[43] == '10': l[43] = '0'
    if l[43] == '11': l[43] = '1'
    if l[43] == '12': l[43] = '2'

for l in list_wc:
    for i in list_18:
        if l[51] == i[51]:
            list_18.remove(i)

list_filt = list_wc + list_18

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
    teamkits_new.write(out3)

teamkits_new.close()
