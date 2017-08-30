import codecs
import re


target = codecs.open('formations12.txt', 'r', 'utf_16')
lst = []

for line in target:
    line = line.strip().split('\t')
    lst.append(line)

ind_name = 'team'

for i in lst:
    for ind in range(0, len(lst[1])):
        if re.findall(ind_name, i[ind]): print ind, i[ind]
