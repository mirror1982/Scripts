import numpy as np
import pickle


import array

#fhand = open('new1.txt', 'r')
#line = fhand.split()
#print arr
# for line in range(1):
#    line = fhand.readline().split()
#print line

#arr = []
#arr_new = list()
inp = open ("new1.txt","r")
#text = inp.read()
#words = text.split()
#out = []
my_file = open("some.txt", 'w')

for line in inp:
    line = line.strip()
    email = line.split()
    #print email
    #if email == []:continue
    #if email[0] != 'From':continue
    #print email[0]
    out = email[1:3]
    print " ".join(map(str, out))
    out2 = " ".join(map(str, out))
    my_file.write(out2+ '\n')
    #for l in out2:
     #   my_file.write(l+ '\n')
    #print out
    #out2 = np.array(out)
    #print(out2)
    #pickle.dump(out, my_file)
    #my_file.writelines("%s\n" for i in out2)
    #for index in out:


#for line in inp.readlines():
    #print line
 #   words = line.split()
  #  arr.append(words)

#print arr
#print arr[0]
#print len(arr[0])
#print type(arr)

#j, p, a, t, pl = arr[0]

#print j

#for word in range(2):
    #print(word)
 #   arr_new.append(arr[word])
    #print len(arr[word])

#arr2 = np.array(arr)
#print arr2
#print arr_new

#print(type(out))
#print(out)


#for index in out:

my_file.close()