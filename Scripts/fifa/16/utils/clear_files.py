import os

for file in os.listdir('D:\\Scripts\\fifa\\16\\convert\\work'):
    os.remove('D:\\Scripts\\fifa\\16\\convert\\work\\' + file)

for file in os.listdir('D:\\Scripts\\fifa\\16\\convert\\ready'):
    os.remove('D:\\Scripts\\fifa\\16\\convert\\ready\\' + file)

for file in os.listdir('D:\\Scripts\\fifa\\16\\convert\\export\\12'):
    os.remove('D:\\Scripts\\fifa\\16\\convert\\export\\12\\' + file)

for file in os.listdir('D:\\Scripts\\fifa\\16\\convert\\export\\16'):
    os.remove('D:\\Scripts\\fifa\\16\\convert\\export\\16\\' + file)


