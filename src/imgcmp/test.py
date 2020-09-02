import lookuptable as lk
import imagehash
from pathlib import Path
from PIL import Image

IMAGE="00010.png"
IMAGEDIR ="/home/rpathak/Projects/Code/Scripts/testautomation/imagecompare/data/images/imagesamehashvalue/"

lktable = lk.ImageLookupTable(lookuptable="../../data/test_1.h5", imagefolder="../../data/images/smalldata")

img = Image.open(IMAGEDIR + IMAGE)
#img.show()

imghash = imagehash.phash(img)
print(imghash)

i, h = lktable.getitem(imghash)
print(i)

#h.show()

print(lktable.isitem(imghash))

print(lktable.matchimage(IMAGEDIR+IMAGE))

