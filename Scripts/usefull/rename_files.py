import os

target_string = 'eng'
new_string = 'rus'

for filename in os.listdir("."):
    while filename.__contains__(target_string):
    #while filename.find(target_string) >= 0:
        i = filename.find(target_string)
        new_filename = filename[:i] + new_string + filename[i + len(target_string):]
        os.rename(filename, new_filename)
        filename = new_filename
