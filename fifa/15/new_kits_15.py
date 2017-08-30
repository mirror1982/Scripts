import codecs

kits12_old = codecs.open('teamkits12.txt', 'r', 'utf_16')
kits12_new = codecs.open('new_kits12.txt', 'r', 'utf_16')
kits12_hyb = codecs.open('hyb_kits12.txt', 'w', 'utf_16')
list_old = []
list_new = []
list_hyb = []

for line in kits12_old:
    line = line.strip().split('\t')
    list_old.append(line)

for line2 in kits12_new:
    line2 = line2.strip().split('\t')
    list_new.append(line2)

for l in list_old:
    for i in list_new:
        if l[31] == i[31]:
            list_new.remove(i)

list_hyb = list_old + list_new

for i in list_hyb:
    out2 = "\t".join(map(str, i))
    out3 = (out2 + '\n')
    kits12_hyb.write(out3)

kits12_hyb.close()