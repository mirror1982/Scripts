import re

fhand = open('mboxl.txt')
rev_list = []
summ = 0

for line in fhand:
    line = line.strip()
    parse = re.findall('^New Revision: (.*[0-9])', line)
    rev_list = rev_list + parse

for i in rev_list:
    summ = summ + float(i)

print (summ/len(rev_list))




