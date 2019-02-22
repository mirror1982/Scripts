
def computepay(h,r):

    if h > 40:
        p = ((h - 40) * 1.5 * r) + (r * 40)
    else:
        p = r * h
    return p

try:
    inp = raw_input("Enter hours: ")
    hours = float(inp)
    inp = raw_input("Enter rate: ")
    rate = float(inp)
except:
    print "error, enter a numeric symbol"
    quit()



print "Salary is ", computepay(hours,rate)
