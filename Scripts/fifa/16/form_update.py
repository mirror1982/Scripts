import sys, codecs
reload(sys)
sys.setdefaultencoding('utf8')

form_old = codecs.open("formations16_old.txt", 'r', 'utf_16')
form_16 = codecs.open("formations16.txt", 'r', 'utf_16')
form_upd = codecs.open('formations16_upd.txt', 'w', 'utf_16')

list_old = []
list_16 = []
list_upd = []

for line in form_old:
    line = line.strip().split('\t')
    list_old.append(line)

for line2 in form_16:
    line2 = line2.strip().split('\t')
    list_16.append(line2)

for g in list_16:
    if g[54] != '-1':
        list_upd.append(g)

count = 1
for i in list_old:
    if i[56] != 'formationid':
        list_upd.insert(count, i)
        count += 1
        if count == 13:
            break

count = -1
for g in list_upd:
    count += 1
    if g[56] != 'formationid':
        g[56] = count

for i in list_upd:
    out2 = "\t".join(map(str, i))
    out3 = (out2 + '\n')
    form_upd.write(out3)

form_16.close()
form_old.close()
form_upd.close()
