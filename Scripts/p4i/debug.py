fhand = open('mbox.txt')
for line in fhand:
    line = line.strip()
    words = line.split()
    #print words
    if words == []:continue
    if words[0] != 'From':continue
    print words[1]
