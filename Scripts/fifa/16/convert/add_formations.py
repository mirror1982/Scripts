import sys, codecs
reload(sys)
sys.setdefaultencoding('utf8')

form_16 = codecs.open("work/formations16.txt", 'r', 'utf_16')
form_12 = codecs.open("work/formations12.txt", 'r', 'utf_16')
form_12_add = codecs.open("work/formations12_add.txt", 'w', 'utf_16')


list_12 = []
list_12_add = []
list_16 = []

for line0 in form_12:
    line0 = line0.strip().split('\t')
    list_12.append(line0)

for line2 in form_16:
    line2 = line2.strip().split('\t')
    list_16.append(line2)

dif = len(list_16) - len(list_12)

for l in range(dif):
    list_12.append(list_12[l+1])

for i in list_12:
    out2 = "\t".join(map(str, i))
    out3 = (out2 + '\n')
    form_12_add.write(out3)

form_12_add.close()
form_12.close()
form_16.close()
