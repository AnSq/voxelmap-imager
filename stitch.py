#!/usr/bin/env python

import sys
import os
from PIL import Image


def xy_from_fname(fname):
    return [int(i) for i in fname.split("_")[0].split(",")]

def stitch(path, num, outfolder):
    files = sorted(os.listdir(path))

    max_x = None
    min_x = None
    max_y = None
    min_y = None

    for fname in files:
        x, y = xy_from_fname(fname)

        if max_x == None or x > max_x:
            max_x = x
        if min_x == None or x < min_x:
            min_x = x
        if max_y == None or y > max_y:
            max_y = y
        if min_y == None or y < min_y:
            min_y = y

    width_r  = max_x - min_x + 1
    height_r = max_y - min_y + 1

    width  = width_r * 256
    height = height_r * 256

    img = Image.new("L", (width, height))

    print "%d: stitching..." % num
    for i,fname in enumerate(files):
        x, y = xy_from_fname(fname)
        x_img = (x - min_x) * 256
        y_img = (y - min_y) * 256

        region = Image.open(os.path.join(path, fname))
        img.paste(region, (x_img, y_img))

    print "%d: saving..." % num
    img.save(os.path.join(outfolder, "%d.png" % num))


def main(infolder, outfolder):
    if os.path.exists(outfolder):
        replace = raw_input("'%s' exists. Replace? [y/N]: " % outfolder) + "n"
        if replace[0].lower() != "y":
            sys.exit()
    else:
        os.mkdir(outfolder)

    for inode in sorted(os.listdir(infolder)):
        num = int(inode)
        path = os.path.join(infolder, inode)
        if os.path.isdir(path):
            stitch(path, num, outfolder)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
