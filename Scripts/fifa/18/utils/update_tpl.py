import sys, codecs
reload(sys)
sys.setdefaultencoding('utf8')

tpl12_old = codecs.open('teamplayerlinks_old.txt', 'r', 'utf_16')
tpl12_new = codecs.open('teamplayerlinks_new.txt', 'r', 'utf_16')
tpl12_upd = codecs.open('tpl_upd.txt', 'w', 'utf_16')
list_old = []
list_new = []
list_filt = []
idl = []

for line in tpl12_old:
    line = line.strip().split('\t')
    list_old.append(line)

for line2 in tpl12_new:
    line2 = line2.strip().split('\t')
    list_new.append(line2)

ID = '1357'

for l in list_new:
        if l[3] == ID:
            idl.append(l)

for l in list_old:
    if l[3] != ID:
        list_filt.append(l)

list_filt.extend(idl)

for i in list_filt:
    out2 = "\t".join(map(str, i))
    out3 = (out2 + '\n')
    tpl12_upd.write(out3)

tpl12_upd.close()
