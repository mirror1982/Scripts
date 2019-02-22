import sys, codecs
reload(sys)
sys.setdefaultencoding('utf8')

players18_old = codecs.open('players.txt', 'r', 'utf_16')
players18_new = codecs.open('new_players.txt', 'r', 'utf_16')
players18_upd = codecs.open('players_upd.txt', 'w', 'utf_16')
list_old = []
list_new = []
idl = []

for line in players18_old:
    line = line.strip().split('\t')
    list_old.append(line)

for line2 in players18_new:
    line2 = line2.strip().split('\t')
    list_new.append(line2)

ID = ['229909', '187347', '178372', '221551', '173208', '215259', '203629', '207439', '154950', '221125', '192086', '216336', '216742', '222265', '214977', '200094', '167005', '201452', '211542', '166744', '211308', '148217', '210610', '239870', '223058', '231225', '234067', '210604']

for l in list_new:
    for i in ID:
        if l[93] == str(i):
            idl.append(l)

for l in list_old:
    for i in ID:
        if l[93] == str(i):
            list_old.remove(l)

list_old.extend(idl)

list_hyb = list()
pid = set()
count = 0
for x in list_old:
    if x[93] in pid:
        count += 1
        print x[93]
        continue
    pid.add(x[93])
    list_hyb.append(x)
print count

for i in list_hyb:
    out2 = "\t".join(map(str, i))
    out3 = (out2 + '\n')
    players18_upd.write(out3)

players18_upd.close()
