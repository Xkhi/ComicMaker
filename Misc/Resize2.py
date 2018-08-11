from glob import glob
from PIL import Image
import os

count = 0
avg = 0
hor = 0

class Resizer:
    def __init__(self,source,destination='D:/StdOut/',quality=20,height=1200):
        self.source = source
        self.destination = destination
        self.quality = quality
        self.height = height
        self.imageOriginal = None
        self.imageCopy = None

    def savePicture(self):
        self.imageCopy.save(self.destination+self.source)
        self.imageCopy.close()

    def closePicture(self,image):
        image.close()

    def isSourceFile(self):
        return os.path.isfile(self.destination)

    def resize(self):
        self.imageCopy = self.imageOriginal.resize((width,self.height),Image.BICUBIC)

    def start(self):
        if(self.isSourceFile()):
            self.imageOriginal = Image.open(self.source)
            self.savePicture()
            
            
            

folderlist = glob('*')
destination = '../Scott Pilgrim Resized/'

for folder in folderlist:
    try:
        os.chdir(folder)
    except:
        print os.getcwd()
        print 'Invalid folder ',folder
    lista_archivos = glob('*.[jp][pn][g]')
    if(not os.path.exists(destination+folder)):
        os.mkdir(destination+folder)      
        for imagen in lista_archivos:
            filename = imagen.split('.')[0]
            im = Image.open(imagen)
            width, height = im.size
            ratio = float(width)/float(height)
            new_im = im.resize((int(1200*ratio),1200),Image.BICUBIC)
            new_im = new_im.convert('L')
            if(width>height):
                new_width, new_height = new_im.size
                im_left = new_im.crop((0,0,(new_width/2-1),new_height))
                im_right = new_im.crop((new_width/2,0,new_width,new_height))
                im_left.save(destination+folder+'/'+filename+'-01.jpeg','jpeg',quality=20)
                im_right.save(destination+folder+'/'+filename+'-02.jpeg','jpeg',quality=20)
                im_left.close()
                im_right.close()
            else:
                new_im.save(destination+folder+'/'+filename+'.jpeg','jpeg',quality=20)
            im.close()
            new_im.close()
    os.chdir('..')
