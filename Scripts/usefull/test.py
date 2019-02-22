str = "Tree, box, chair, lamp, desk, cat, dog, grass, pig, box, lamp, shelf"
print(str)

subStrOld = input("Old substring: ")
subStrNew = input("New substring: ")
lenStrOld = len(subStrOld)

while str.find(subStrOld) > 0:
    i = str.find(subStrOld)
    str = str[:i] + subStrNew + str[i+lenStrOld:]

print(str)