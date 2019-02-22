import sys, codecs
reload(sys)
sys.setdefaultencoding('utf8')

form_16 = codecs.open("work/formations16.txt", 'r', 'utf_16')
form_17 = codecs.open("work/formations17.txt", 'r', 'utf_16')
form_17_add = codecs.open("work/formations17_add.txt", 'w', 'utf_16')


list_17 = []
list_17_add = []
list_16 = []

for line0 in form_17:
    line0 = line0.strip().split('\t')
    list_17.append(line0)

for line2 in form_16:
    line2 = line2.strip().split('\t')
    list_16.append(line2)

dif = len(list_16) - len(list_17)

for l in range(dif):
    list_17.append(list_17[l+1])

for i in list_17:
    out2 = "\t".join(map(str, i))
    out3 = (out2 + '\n')
    form_17_add.write(out3)

form_17_add.close()
form_17.close()
form_16.close()
