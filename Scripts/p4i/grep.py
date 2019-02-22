import re

fhand = open('mboxl.txt')
exp = raw_input('Enter a regular expression: ')
count = 0

for line in fhand:
    if re.search(exp, line) > 0:
        count += 1
print count
