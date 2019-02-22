
inp = raw_input('Enter a string to parse:  ')
colon_pos = inp.find(':')+1
print colon_pos
num = inp[colon_pos:]
print float(num)
