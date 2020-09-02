from pathlib import Path
import imagehash
import h5py
from PIL import Image
import os
import sys
import traceback
# Configurable parameter
HEIGHT=128
WIDTH=128
PIL_IMAGE_DTYPE = 'uint8'
PIL_IMAGE_TYPE = 'RGB'

class ImageLookupTable(object):
  def __init__(self, lookuptable=None, generate=False, imagefolder=None, hashing=imagehash.phash):
    # Need the lookup table for sure
    assert(lookuptable != None)
    self.lktablepath = Path(lookuptable)
    #self.lktablename = self.lktablepath.name
    self.imgnamelist = []
    self.hashalgo = hashing
    _isfilepresent = Path(lookuptable).exists()
    
    if not _isfilepresent or (_isfilepresent and generate):
        #irrespective of the generate flag, create the look up table.
        try:
            assert(imagefolder != None)
            self.imgfolder = Path(imagefolder)
            self.imglist = list(self.imgfolder.glob("**/*.png"))
            self._createlookuptable()
        except AssertionError:
            sys.exit("pass on the imagefolder path")

    else:
      print(f"lookup table present at: [{self.lktablepath}]")
           

  def matchimage(self, imghash):
    with h5py.File(self.lktablepath, 'r') as h5file:
      if key in h5file.keys():
        getitem(imghash)

  # TODO
  def additem(self, key):
    pass
  # TODO
  def removeitem(self, key):
    pass

  def isitem(self, key):
    """ isitem(key): take input "key" and checks if the image with 
    the hash as key is present in the lookup table or not."""
    with h5py.File(self.lktablepath, 'r') as h5file:
      return (key in h5file.keys())

  def getitem(self, key):
    """ getitem(key): Takes input "key" which is the generated hash 
    of the image and return the imagename and PIL Image."""
    with h5py.File(self.lktablepath, 'r') as h5file:
      array = h5file[str(key)][:]
      pilimage = Image.fromarray(array.astype(PIL_IMAGE_DTYPE), 'RGB')
      imagename = h5file[str(key)]
      print(imagename)
      return imagename, pilimage

  def _createlookuptable(self): 
    try:
      self.lktablepath.unlink(missing_ok=True)
      with h5py.File(self.lktablepath, 'a') as h5file:
        for image in self.imglist:
          imagename = image.name[:-4]
          pilimage = Image.open(image)
          imghashvalue = self.hashalgo(pilimage)
          print(f"imagename: [{imagename}], imagehash: [{imghashvalue}]")
          h5file.create_dataset(f"{imghashvalue}", data=pilimage, dtype='uint8', shape=(HEIGHT, WIDTH, 3))
          h5file[f"{imghashvalue}"].attrs.create(name=f"{imagename}", data=str(imagename))        
          self.imgnamelist.append(imagename)
    except IOError:
      print("ERROR: lookup table is already opened. try to open it in the same mode")
      traceback.print_exc(file=sys.stdout)

if __name__ == '__main__':
    IMAGEFOLDER = '../../data/images/bigdata'
    LOOKUPTABLEPATH = '../../data/lookuptable_bigdata_1.h5'
    lktable = ImageLookupTable(lookuptable=LOOKUPTABLEPATH, generate=False, imagefolder=IMAGEFOLDER)
