from glob import glob
from PIL import Image
import os

class Resizer(Image.Image):
    def isSourceFile(self):
        pass

    def resize(self):
        pass

    def compress():
        kindle_resolution = (1024,758)
        kindle_dpi = (212,212)
        dest_size = (812,1200)
        for fi in files:
            im = Image.open(fi)
            name, ext = os.path.splitext(fi)
            oldsize = os.stat(fi).st_size
            if(im.size > dest_size):
                out = im.resize(dest_size,Image.HAMMING).convert('L')
                out.save("../output_test/{}.jpg".format(name),'jpeg',optimize=True,quality=10)
            else:
                out = im.convert('L').save("../output_test/{}.jpg".format(name),'jpeg',optimize=True,quality=10)
            newsize = os.stat("../output_test/{}.jpg".format(name)).st_size
            percent = (oldsize-newsize)/float(oldsize)*100
            print percent

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
    print __name__