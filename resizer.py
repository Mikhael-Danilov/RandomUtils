import os
from PIL import Image

#xs = 14
#ys = 17

xs = 28
ys = 36


nXs = 64
nYs = 64

xPad = int((nXs - xs) / 2)
yPad = int((nYs - ys) / 2)

nFrames = 19

oXs = 1024
oYs = 32


def resize(iname, oname):
    img = Image.open(iname)

    for i in range(nFrames):
        x = xs * i
        y = 0

        frame = img.crop((x, y, x + xs, y + ys))

        nx = nXs * i
        ny = 0
        out.paste(frame, (nx + xPad, ny + yPad))

        #frame.save("out" + str(i) + ".png")

    out.save(oname)


#resize("man.png", "out.png")


rootDir = '/media/mike/BigData/Nyrds/Remixed Pixel Dungeon/PixelDungeon/src/main/assets/hero/accessories'

out = Image.new('RGBA', (oXs, oYs))

for dirName, subdirList, fileList in os.walk(rootDir):

    print('Found directory: %s' % dirName)
    for fname in fileList:
        if '.png' in fname:
            print('\t%s' % fname)
            fullPath = dirName + "/" + fname
            for i in range(nFrames):
                x = xs * i
                y = 0

                frame = img.crop((x, y, x + xs, y + ys))

                nx = nXs * i
                ny = 0
                out.paste(frame, (nx + xPad, ny + yPad))

                # frame.save("out" + str(i) + ".png")
