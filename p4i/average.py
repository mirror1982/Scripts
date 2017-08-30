summ = 0
count = 0
average = 0

while True:
    try:
        inp = raw_input('Enter a number:  ')
        number = float(inp)
        count = count + 1
        summ = summ + number
        average = summ / count

    except:
        if inp == 'done' or len(inp) < 1:
            break
        print 'Error, enter a numeric symbol'
        continue

print 'Average is ', average
