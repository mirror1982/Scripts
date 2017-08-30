def computepay (hours, rate):
    try:
        hours = float(hours)
        rate = float(rate)
    except:
        print "error, enter a numeric symbol"
        quit()

    if hours > 40:
            pay = ((hours - 40) * 1.5 * rate) + (rate * 40)
    else:
            pay = rate * hours
    print "Salary is ", pay

computepay(45,10)

