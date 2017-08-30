import os
from PIL import Image

width = 128
height = 128

for name in os.listdir(os.getcwd()):
    if name[name.rfind('.'):] == '.png' and name[0:2] != 'N_':
        img = Image.open(name)
        img = img.resize((width, height), Image.ANTIALIAS)
        new_name = 'N_' + name
        img.save(new_name)
