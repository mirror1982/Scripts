import re

fhand = open('mbox.txt')
time_list = list()
time_dic = dict()
sorted_list = list()
hours = list()

for line in fhand:
    #line = line.strip().split()
    #if line == []:continueerer
    #if line[0] != 'From':continue
    line = line.strip()
    time_list = re.findall('^From.*?([0-9][0-9]):', line)
    #print(time_list)
    #hours = line[5].split(':')
    #time_list.append(hours[0])

    for hour in time_list:
        time_dic[hour] = time_dic.get(hour, 0) + 1

for k, v in time_dic.items():
    sorted_list.append((k, v))
sorted_list.sort()

for i in sorted_list:
    print i[0], i[1]