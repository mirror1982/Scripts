import codecs

players18 = codecs.open('players18.txt', 'r', 'utf_16')
players18_new = codecs.open('players_faces18.txt', 'w', 'utf_16')
lst = []
list_new = []

for line in players18:
    line = line.strip().split('\t')
    lst.append(line)

count = 0
for l in lst:
    # if l[82] == "headclasscode" or l[82] == "0" and l[59] != '1':
    if l[55] == "hashighqualityhead" or l[55] == "1" and l[59] != '1':
        list_new.append(l)
        count +=1

print(count)

for i in list_new:
    out2 = "\t".join(map(str, i))
    out3 = (out2 + '\n')
    players18_new.write(out3)

players18_new.close()
