
try:
    inp = raw_input("Enter hours: ")
    hours = float(inp)
    inp = raw_input("Enter rate: ")
    rate = float(inp)
except:
    print "error, enter a numeric symbol"
    quit()

if hours > 40:
        pay = ((hours - 40) * 1.5 * rate) + (rate * 40)
else:
        pay = rate * hours

print "Salary is ", pay



