#!/usr/bin/env python

import sys
import os
import zipfile
import json
from PIL import Image, ImageDraw


SIZE = 256
BLOCKSIZE = 17


def render_region(region_zip, outfolder, bits):
    region_num = os.path.basename(region_zip).split(".")[0]

    with zipfile.ZipFile(region_zip, "r") as zf:
        voxeldata = zf.read("data")

    imgs = {}
    draws = {}
    for i in bits:
        imgs[i] = Image.new("L", (SIZE, SIZE))
        #draws[i] = ImageDraw.Draw(imgs[i])

    for y in range(SIZE):
        for x in range(SIZE):
            blocknum = y * SIZE + x
            blockdata = voxeldata[blocknum*BLOCKSIZE:blocknum*BLOCKSIZE+BLOCKSIZE]

            for i in bits:
                blockvalue = ord(blockdata[i])
                imgs[i].putpixel((x,y), blockvalue)
                #draws[i].point([(x,y)], blockvalue)

    for i in imgs:
        imgs[i].save(os.path.join(outfolder, str(i), "%s_%d.png" % (region_num, i)))


def main(infolder, outfolder, bits):
    if os.path.exists(outfolder):
        replace = raw_input("'%s' exists. Replace? [y/N]: " % outfolder) + "n"
        if replace[0].lower() != "y":
            sys.exit()
    else:
        os.mkdir(outfolder)

    for i in bits:
        subdir = os.path.join(outfolder, str(i))
        if not os.path.exists(subdir):
            os.mkdir(subdir)

    files = sorted(os.listdir(infolder))
    for i,fname in enumerate(files):
        render_region(os.path.join(infolder, fname), outfolder, bits)
        print "%.2f%%: %s" % (100.0*(i+1)/len(files), fname)



if __name__ == "__main__":
    if len(sys.argv) >= 4 and sys.argv[3]:
        bits = json.loads(sys.argv[3])
    else:
        bits = range(BLOCKSIZE)
    assert type(bits) == type(list())
    main(sys.argv[1], sys.argv[2], bits)
