import os
from PIL import Image

xs = 64
ys = 64

nFrames = 20

rootDir = '/media/mike/BigData/Nyrds/pixel-dungeon-remix/RemixedDungeon/src/main/assets/hero_modern'

def getFrame(img, fn):
    x = xs * fn
    y = 0

    return img.crop((x, y, x + xs, y + ys))

def putFrame(img, frame, fn, dx, dy):
    x = xs * fn
    y = 0

    img.paste(frame, (x+dx, y+dy))


for dirName, subdirList, fileList in os.walk(rootDir):
    print('Found directory: %s' % dirName)

    for fname in fileList:

        if 'accessories' in dirName:
            if '.png' in fname:
                print('\t%s' % fname)
                fullPath = dirName + "/" + fname
                img = Image.open(fullPath)
                putFrame(img, getFrame(img, 13), 14, 0, 2)

                img.save(fullPath)
            #continue

        if 'left' in fname:
            continue

        # if '.png' in fname:
        #     print('\t%s' % fname)
        #     fullPath = dirName + "/" + fname
        #     img = Image.open(fullPath)
        #     putFrame(img, getFrame(img,13),14,0,1)
        #
        #     img.save(fullPath)
