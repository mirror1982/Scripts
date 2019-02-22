

while True:
    inp = raw_input('Enter filename: ')
    try:
        fhandle = open(inp)
        break
    except:
        print('Error. File not found')
        continue
for line in fhandle:
    print line.upper().strip()
