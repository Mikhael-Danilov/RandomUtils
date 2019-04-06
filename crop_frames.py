import os
from PIL import Image
from PIL import ImageStat

xs = 32
ys = 32

nFrames = 20

oXs = 1024
oYs = 32

rootDir = '/media/mike/BigData/Nyrds/pixel-dungeon-remix/PixelDungeon/src/main/assets/hero_modern'


def paddedFrameRect(x, y, xs, ys, n, pad):
    if n == 0:
        return x, y, x + pad, y + ys
    if n == 1:
        return x + xs - pad, y, x + xs, y + ys
    if n == 2:
        return x, y, x + xs, y + pad
    if n == 3:
        return x, y + ys - pad, x + xs, y + ys


def computePads(inimg):
    pads = list((xs, xs, ys, ys))

    for i in range(nFrames):
        x = xs * i
        y = 0

        for nPad in range(4):
            # print(nPad, pads)
            for pad in range(pads[nPad]):
                frame = inimg.crop(paddedFrameRect(x, y, xs, ys, nPad, pad))
                stat = ImageStat.Stat(frame)

                # print(i, nPad, pad, pads[nPad], "pads:", stat.sum)

                if sum(stat.sum) > 0:
                    # print("sum:", sum(stat.sum), i, nPad, pads[nPad],pad)
                    pads[nPad] = pad - 1
                    break

    print("pads:", pads)


combined = Image.new('RGBA', (oXs, oYs))

for dirName, subdirList, fileList in os.walk(rootDir):
    print('Found directory: %s' % dirName)

    for fname in fileList:

        if 'accessories' in dirName:
            continue

        if 'left' in fname:
            continue

        if '.png' in fname:
            print('\t%s' % fname)
            fullPath = dirName + "/" + fname
            img = Image.open(fullPath)
            computePads(img)
            combined.alpha_composite(img)

    combined.save("combined.png")


computePads(combined)