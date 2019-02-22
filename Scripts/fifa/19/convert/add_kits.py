import sys, codecs
reload(sys)
sys.setdefaultencoding('utf8')

kits_16 = codecs.open("work/teamkits16.txt", 'r', 'utf_16')
kits_18 = codecs.open("work/teamkits18.txt", 'r', 'utf_16')
kits_18_add = codecs.open("work/teamkits18_add.txt", 'w', 'utf_16')


list_18 = []
list_18_add = []
list_16 = []
list_181 = []

for line0 in kits_18:
    line0 = line0.strip().split('\t')
    list_181.append(line0)

for line2 in kits_16:
    line2 = line2.strip().split('\t')
    list_16.append(line2)

dif = len(list_16)
print dif


for l in range(dif):
    list_18.append(list_181[l])

for i in list_18:
    out2 = "\t".join(map(str, i))
    out3 = (out2 + '\n')
    kits_18_add.write(out3)

kits_18_add.close()
kits_18.close()
kits_16.close()
