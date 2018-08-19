from glob import glob
from PIL import Image
import os

class Resizer(Image.Image):
    def __init__(self):
        self.kindle_resolution = (758,1024)
        self.kindle_dpi = (212,212)
    
    @property    
    def isWide(self):
        if self.width > self.height:
            return True
        else:
            return False
        
    def resize2kindle(self):
        if(self.height > self.kindle_resolution[1]):
            self.resize(self.kindle_resolution,Image.HAMMING).convert('L')
        else:
            self.convert('L')

    def save2kindle(self,name,qual):
        self.save("./output/{}.jpg".format(name),'jpeg',optimize=True,quality=qual)
        
def routine():
#     for fi in files:
#         im = Image.open(fi)
#         name, ext = os.path.splitext(fi)
#         oldsize = os.stat(fi).st_size
#         newsize = os.stat("../output_test/{}.jpg".format(name)).st_size
#         percent = (oldsize-newsize)/float(oldsize)*100
#         print percent

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

if __name__== '__main__':
    print __name__