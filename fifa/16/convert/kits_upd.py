import codecs

kits12_old = codecs.open('work/teamkits12.txt', 'r', 'utf_16')
kits12_new = codecs.open('work/new_kits12.txt', 'r', 'utf_16')
kits12_upd = codecs.open('ready/teamkits.txt', 'w', 'utf_16')
list_old = []
list_new = []

for line in kits12_old:
    line = line.strip().split('\t')
    list_old.append(line)

count = 0
for line2 in kits12_new:
    line2 = line2.strip().split('\t')
    list_new.append(line2)
    if line2[29] != 'teamkitid':
        line2[29] = count
        count += 1

for l in list_old:
    for i in list_new:
        if l[31] == i[31] and l[27] == i[27]:
            i[5] = l[5] #numberfonttype
            i[7] = l[7] #jerseynamefonttype
            i[23] = l[23]  #shortsnumberfonttype

            #i[9] = l[9] #shortsnumbercolor
            #i[20] = l[20] #numbercolor


            #i[19] = l[19] #jerseynamecolor
            #i[24] = l[24]
            #i[13] = l[13]

            #i[26] = l[26]  # jerseybacknamefontcase
            #i[8] = l[8]  # jerseynamelayouttype

            #i[2] = l[2] #shortsrenderingdetailmaptype
            #i[10] = l[10] #jerseyshapestyle
            #i[16] = l[16] #renderingmaterialtype
            #i[22] = l[22] #jerseyrenderingdetailmaptype
            #i[28] = l[28] #isinheritbasedetailmap
            #i[32] = l[32] #hasadvertisingkit
            #i[33] = l[33] #dlc

            if i[18] != 'jerseycollargeometrytype' and int(i[18]) == 15: i[18] = '14'
            if i[18] != 'jerseycollargeometrytype' and int(i[18]) == 16: i[18] = '13'
            if i[18] != 'jerseycollargeometrytype' and int(i[18]) == 17: i[18] = '10'
            if i[18] != 'jerseycollargeometrytype' and int(i[18]) == 18: i[18] = '11'
            if i[18] != 'jerseycollargeometrytype' and int(i[18]) == 19: i[18] = '5'
            if i[18] != 'jerseycollargeometrytype' and int(i[18]) == 20: i[18] = '14'
            if i[18] != 'jerseycollargeometrytype' and int(i[18]) == 21: i[18] = '7'

for i in list_new:
    out2 = "\t".join(map(str, i))
    out3 = (out2 + '\n')
    kits12_upd.write(out3)

kits12_upd.close()
