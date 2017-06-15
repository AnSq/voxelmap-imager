#!/usr/bin/env python

import sys
import os
from PIL import Image


def rect_search(img, top, left, width, height, values, match, hits, total):
    """
    Params:
    img: Image to search
    top, left, width, height: rectangle to search in image
    values: list of values to search for
    match: whether to match values (True) or anti-match (False). False means that a value NOT in values results in a hit
    hits: number of hits before starting
    total: total number of tests before starting

    Returns:
    (hits, total): hits and total after searching this rectangle (added to the input parameters)
    """
    y = top
    while y < top + height:
        x = left
        while x < left + width:
            pixel = img.getpixel((x,y))
            if (match and pixel in values) or (not match and pixel not in values):
                hits += 1
            total += 1
            x += 1
        y += 1

    return (hits, total)


def search(path):
    img = Image.open(path)
    hits = 0
    total = 0

    #hits, total = rect_search(img,   0,  62,   9,  58, (9,), True,  hits, total)
    #hits, total = rect_search(img,  62,  84,  44,  10, (9,), True,  hits, total)
    #hits, total = rect_search(img,  34, 118,  10,  28, (9,), True,  hits, total)
    #hits, total = rect_search(img, 115, 122,   4,   9, (9,), True,  hits, total)
    #hits, total = rect_search(img,  83,  52,   4,   4, (9,), True,  hits, total)
    #hits, total = rect_search(img,  27,  84,  17,  22, (9,), False, hits, total)
    #hits, total = rect_search(img,  72,  35,  38,   5, (9,), False, hits, total)
    #hits, total = rect_search(img,  77,  68,   5,  51, (9,), False, hits, total)
    #hits, total = rect_search(img,   0,  30,   5,  77, (9,), False, hits, total)
    #hits, total = rect_search(img,  15,  91,  23,  12, (9,), False, hits, total)

    #hits, total = rect_search(img,  84,  48,   6,   6, (9,),     True,  hits, total)
    #hits, total = rect_search(img,  89,  73,   3,   3, (9,),     True,  hits, total)
    #hits, total = rect_search(img, 110,   9,   7,   4, (172,),   True,  hits, total)
    #hits, total = rect_search(img, 122,  22,   3,   3, (172,),   True,  hits, total)
    #hits, total = rect_search(img, 120,  34,   3,   3, (172,),   True,  hits, total)
    #hits, total = rect_search(img, 121, 110,   3,   3, (172,),   True,  hits, total)
    #hits, total = rect_search(img,  13,  91,   9,   9, (18,161), True,  hits, total)
    #hits, total = rect_search(img,  31,  91,   6,   6, (18,161), True,  hits, total)
    #hits, total = rect_search(img,  43,  74,   9,  21, (2,),     True,  hits, total)
    #hits, total = rect_search(img,  44,  29,   3,   3, (12,24),  True,  hits, total)
    #hits, total = rect_search(img,  27,  36,   6,   2, (12,24),  True,  hits, total)
    #hits, total = rect_search(img,  32,  74,   3,   2, (12,24),  True,  hits, total)
    #hits, total = rect_search(img,  68,   0, 128,  12, (9,),     False, hits, total)
    #hits, total = rect_search(img,  80,  83,  15,  48, (9,),     False, hits, total)
    #hits, total = rect_search(img,   0,  49,  15,  68, (9,),     False, hits, total)

    hits, total = rect_search(img,  91,  33,  89,   5, (1,13),   True,  hits, total)
    hits, total = rect_search(img,  96,  52,   3,  29, (1,13),   True,  hits, total)
    hits, total = rect_search(img, 119,  32,  20,   6, (1,13),   True,  hits, total)
    hits, total = rect_search(img,  65,  88,  34,  26, (1,13),   True,  hits, total)
    hits, total = rect_search(img,  96,  69,  49,  19, (1,13),   True,  hits, total)
    hits, total = rect_search(img,  39,  10,  24,  21, (1,13),   True,  hits, total)
    hits, total = rect_search(img,  16,  48,   9,   9, (18,161), True,  hits, total)
    hits, total = rect_search(img,  26,  68,   7,   2, (12,24),  True,  hits, total)
    hits, total = rect_search(img,  12, 103,  17,   5, (2,),     True,  hits, total)
    hits, total = rect_search(img,  31,  39,  47,  57, (9,),     False, hits, total)

    return float(hits) / total


def main(infolder):
    files = sorted(os.listdir(infolder))
    scores = []
    for i,fname in enumerate(files):
        score = search(os.path.join(infolder, fname))
        scores.append((score, fname))
        print "%.2f%%: %s  %.4f" % (100.0*(i+1)/len(files), fname, score)

    print

    scores.sort(reverse=True)
    for s in scores[:20]:
        print "%.4f %s" % (s[0], s[1])

if __name__ == "__main__":
    main(sys.argv[1])
