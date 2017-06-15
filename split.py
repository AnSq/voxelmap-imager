#!/usr/bin/env python

import sys
import os
from PIL import Image


def split(path, num, outfolder, offset_x, offset_y):
    img = Image.open(path)

    y = offset_y
    while y < img.height:
        x = offset_x
        while x < img.width:
            crop = img.crop((x, y, x+128, y+128))
            crop.save(os.path.join(outfolder, num, "%d,%d.png" % (x,y)))
            x += 128
        y += 128


def main(infolder, outfolder, offset_x, offset_y):
    if os.path.exists(outfolder):
        replace = raw_input("'%s' exists. Replace? [y/N]: " % outfolder) + "n"
        if replace[0].lower() != "y":
            sys.exit()
    else:
        os.mkdir(outfolder)

    for fname in sorted(os.listdir(infolder)):
        num = fname.split(".")[0]
        subdir = os.path.join(outfolder, num)
        if not os.path.exists(subdir):
            os.mkdir(subdir)
        split(os.path.join(infolder, fname), num, outfolder, offset_x, offset_y)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))
