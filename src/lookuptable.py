from pathlib import Path
import imagehash
import h5py

class LookupTable(object):
    def __init__(self, imagefolder, lookuptable):
        self.imagefolder = Path(imagefolder)    
        self.imagelist = list(self.imagefolder.glob("**/*.png"))
        self.imagenamelist = []
        self.hashalgorithm = imagehash.average_hash
        self.lookuptable = lookuptable
        self._createlookuptable()

    def additem(key):
        pass
    
    def removeitem(key):
        pass

    def finditem(key):
        pass

    def getitem(key):
        pass

    def _createlookuptable(self): 
        try: 
            with h5py.File(self.lookuptable, 'a') as h5file:
                for image in self.imagelist:
                    imagename = image.name[:-4]
                    pilimage = Image.open(image)
                    imghashvalue = self.hashalgorithm(pilimage)
                    print(f"imagename: [{imagename}], imagehash: [{imghashvalue}]")
                    h5file.create_dataset(f"{imagename}", data=pilimage, dtype='uint8', shape=(HEIGHT, WIDTH, 3))
                    h5file[f"{imagename}"].attrs.create(name=f"{imagename}", data=str(imghashvalue))        
                    self.imagenamelist.append(imagename)
        except IOError:
            print("lookup table is already opened. try to open it in the same mode")


IMAGEFOLDER = '../data/images/'
LOOKUPTABLEPATH = '../data/lookuptable.h5'

if __name__ == '__main__':
    lktable = LookupTable(IMAGEFOLDER, LOOKUPTABLEPATH)
    print(lktable.imagelist)
