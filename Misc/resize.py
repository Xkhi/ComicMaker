from glob import glob
from PIL import Image
import os

count = 0
avg = 0
hor = 0

lista_archivos = glob('*.jpg')
if(not os.path.exists('Resized')):
    os.mkdir('Resized')
output = open('Resized/Summary.txt','w')
    
for imagen in lista_archivos:
    filename = imagen.split('.')[0]
    im = Image.open(imagen)
    width, height = im.size
    ratio = float(width)/float(height)
    if(height>width):
        count = count+1
        avg = avg+int(1200*ratio)
    else:
        hor = hor+1
    new_im = im.resize((int(1200*ratio),1200),Image.BICUBIC)
    im.close()
    new_im = new_im.convert('L')
    new_im.save('Resized/'+filename+'.jpeg','jpeg',quality=20)
    ##new_im.save('opt'+imagen)
    new_im.close()

output.write('Number of horizontal files: '+str(hor)+'\n')
output.write('Number of vertical files: '+str(count)+'\n')
output.write('Average width: '+str(avg/count))
output.close()

