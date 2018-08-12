from glob import glob
from PIL import Image
import os

class Resizer(object):
    def __init__(self):
        pass
    
    def savePicture(self):
        pass
    
    def closePicture(self):
        pass

    def isSourceFile(self):
        pass

    def resize(self):
        pass

    def start(self):
        pass

def routine():
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
    routine()