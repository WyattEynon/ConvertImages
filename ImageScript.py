# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 12:45:04 2021

@author: wyatt
"""

import os
from PIL import Image
import sys
import re


def main():
    extRegex=".*(png)|(PNG)$"
    basedir=""
    newdir=""
    if(len(sys.argv)<2):
        basedir='./images/'
    else:
        basedir=sys.argv[1]
        if len(sys.argv)>2:
            newdir=sys.argv[2]
    names = os.listdir(basedir)
    
    for images in names:
        try:
            if re.search(extRegex, str(images)):
            
                im = Image.open(basedir+images)
                new_im = im.resize((128,128))
                new_im = new_im.rotate(90).show()
                if not im.mode == 'RGB':
                    new_im = new_im.convert('RGB')
                new_im.save(newdir+images+".jpeg")
        except:
            print(images+" is not valid")
if __name__ == "__main__":
    main()