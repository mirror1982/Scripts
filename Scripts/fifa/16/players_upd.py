import codecs

players12_act = codecs.open('players_act.txt', 'r', 'utf_16')
players12_upd = codecs.open('players12_upd.txt', 'w', 'utf_16')
list_act = []

for line in players12_act:
    line = line.strip().split('\t')
    list_act.append(line)


for i in list_act:
    for h in range(1022, 1028, 1):
        if i[36] != 'headtypecode' and i[36] == str(h):
            i[36] = '1000'

    for h in range(2022, 2031, 1):
        if i[36] != 'headtypecode' and i[36] == str(h):
            i[36] = '2000'

    for h in range(2513, 2519, 1):
        if i[36] != 'headtypecode' and i[36] == str(h):
            i[36] = '2500'

    if i[12] != 'hairtypecode' and int(i[12]) > 112 or i[12] == '0':
        i[12] = '75'

    if i[87] != 'skintonecode' and int(i[87]) > 3:
        i[68] = 3

for i in list_act:
    out2 = "\t".join(map(str, i))
    out3 = (out2 + '\n')
    players12_upd.write(out3)

players12_upd.close()