import os, sys
from PIL import Image
reload(sys)
sys.setdefaultencoding('utf8')

width = 150
height = 150

for name in os.listdir(os.getcwd()):
    if name[name.rfind('.'):] == '.png' and name != 'template.png' and name[0:2] != 'N_':
        try:
            template = Image.open('template.png')
            img = Image.open(name)
            img = img.resize((width, height), Image.ANTIALIAS)
            template.paste(img, (0, 0), img)
            new_name = 'N_' + name
            template.save(new_name)
        except:
            continue
