import codecs

form_16 = codecs.open("work/formations16.txt", 'r', 'utf_16')
form_12 = codecs.open("ready/formations.txt", 'r', 'utf_16')
teams_12 = codecs.open("ready/teams.txt", 'r', 'utf_16')

list_12 = []
list_16 = []
index_12 = []
index_16 = []
tms = []
missed = []

for line in form_12:
    line = line.strip().split('\t')
    list_12.append(line)

for line2 in form_16:
    line2 = line2.strip().split('\t')
    list_16.append(line2)

for line3 in teams_12:
    line3 = line3.strip().split('\t')
    tms.append(line3)

for l in list_12:
    index_12.append(l[65])

for l2 in list_16:
    index_16.append(l2[54])

count = 0
for l in index_16:
    if not l in index_12:
        count += 1
        missed.append(l)

for l in tms:
    for l2 in missed:
        if l[26] == l2:
            print l[26], l[10]

print 'total:', count