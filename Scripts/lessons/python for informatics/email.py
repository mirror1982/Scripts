import re

fhand = open('mboxl.txt')
mail_list = []
mail_dic = dict()
sorted_list = list()

for line in fhand:
    #line = line.strip().split()
    #if line == []:continue
    #if line[0] != 'From':continue
    #if not line.startswith('From'):continue
    #line = line.strip().split()
    #mail_list.append(line[1])
    mail_list = re.findall('^From.(.+@*)', line)

    for email in mail_list:
        mail_dic[email] = mail_dic.get(email, 0) + 1

for k, v in mail_dic.items():
    sorted_list.append((v,k))
sorted_list.sort(reverse = True)

#for k, v in sorted_list[:10]:
#    print k
#    print v

m = max(sorted_list)
print m[1], m[0]
