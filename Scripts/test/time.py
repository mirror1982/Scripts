import time

print time.time()
print (time.mktime(time.strptime('2018-10-11 18:24:00', '%Y-%m-%d %H:%M:%S')))
print time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(1539271440))
print time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
print time.localtime()
