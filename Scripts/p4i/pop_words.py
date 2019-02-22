
#filename = raw_input('Enter file name: ')
fhandle = open('clown.txt')
text = fhandle.read()
words = text.split()
counts = dict()
max_key = None
max_value = None

#for line in text:
#    line = line.strip()
#    words = line.split()
for word in words:
    counts[word] = counts.get(word, 0) + 1
#    if word not in counts:
#            counts[word] = 1
#    else:
#            counts[word] += 1                  # = counts[word] + 1

for key, value in counts.items():
    if value >= max_value:
        max_value = value
        max_key = key
#    print key, value, max_key, max_value

print counts

print max(counts.values())
print max(counts.keys())
print max(counts.items())
print max_key, max_value
