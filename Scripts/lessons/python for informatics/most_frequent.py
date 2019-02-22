import re

def most_frequent(txt):

    letters_dic = dict()
    sorted_list = list()
    txt = txt.lower()

    for i in txt:
        letters = re.findall('[A-Za-z]', i)
        #letters = i.lower().strip().split()

        for letter in letters:
            letters_dic[letter] = letters_dic.get(letter, 0) + 1
        #print letters_dic

    for k, v in letters_dic.items():
        sorted_list.append((v, k))
        sorted_list.sort(reverse=True)

    for i in sorted_list:
        print i[1], i[0]

most_frequent('sddddddddddddddddddddddddddddferer"')