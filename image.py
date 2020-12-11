import numpy as np
import cv2
import os
from sys import platform
from log import Log


class Img():
    """
    Egy képet reprezentáló osztály, amely tárol az adott képről pár fontos információt
    """
    def __init__(self, path):
        if platform == "linux" or platform == "linux2": # Az opericós rendszer ellenörzése
            self.nev = path.split('/')[-1] # Ha linux
        else:
            self.nev = path.split("\\")[-1] # Ha bármi más
        self.mtrx = cv2.imread(path,cv2.IMREAD_UNCHANGED)
        self.height = self.mtrx.shape[0]
        self.width = self.mtrx.shape[1]

@Log    
def forgatas90FokkalJobbra(img):
    img.mtrx = cv2.rotate(img.mtrx, cv2.ROTATE_90_CLOCKWISE)
    return img

@Log
def forgatas90FokkalBalra(img):
    img.mtrx = cv2.rotate(img.mtrx, cv2.ROTATE_90_COUNTERCLOCKWISE)
    return img

@Log
def forgatas180FokkalBalra(img):
    img.mtrx = cv2.rotate(img.mtrx, cv2.ROTATE_180)
    return img

@Log
def kepMegjelelitese(img): 
    cv2.imshow(img.nev,img.mtrx)
    while True:
        k = cv2.waitKey(100)
        if k == 27:
            print('ESC')
            cv2.destroyAllWindows()
            break        
        if cv2.getWindowProperty(img.nev,cv2.WND_PROP_VISIBLE) < 1:        
            break        
    cv2.destroyAllWindows()

@Log
def szazalekosAtmeretezes(img, precent):
    im = np.array(img.mtrx).astype(np.uint8) # Átkonvertálás np.array-ra, Másképp nem lehetett átméretezni
    Width = int(img.width * precent) # Szélesség skálázása
    Height = int(img.height * precent) # Magasság skálázása
    dim = (Width,Height)
    resized = cv2.resize(im, dim, interpolation = cv2.INTER_AREA)
    img.mtrx = resized # Vissza konvertálás cv2.img objektummá
    return img
@Log
def adottMeretuKep(img,st):
    im = np.array(img.mtrx).astype(np.uint8)
    tmp = st.split(':')
    if len(tmp) == 4:
        Width = int(tmp[1])
        Height = int(tmp[3])
    else:
        if tmp[0] == "W":
            Width = int(tmp[1])
            Height = img.height
        else:
            Height = int(tmp[1])
            Width = img.width
    dim = (Width, Height)
    resized = cv2.resize(im, dim, interpolation = cv2.INTER_AREA)
    img.mtrx = resized
    return img

# Nem helyes tarja az arányokat valami félre megy.
@Log
def adottMeretKepAranyokMegtartasaval(img,st):
    im = np.array(img.mtrx).astype(np.uint8)
    tmp = st.split(':')
    if tmp[0] == "W":
        Width = int(tmp[1])
        Height = int(img.height / (img.width/Width))
    else:
        Height = int(tmp[1])
        Width = int(img.width / (img.height/Height))
    dim = (Width, Height)
    resized = cv2.resize(im, dim, interpolation = cv2.INTER_AREA)
    img.mtrx = resized
    img.width, img.height,_ = resized.shape
    return img

@Log
def blur(img, meret):
    im = np.array(img.mtrx).astype(np.uint8)
    kernel = (meret,meret)
    img.mtrx = cv2.blur(im,kernel)
    return img

@Log
def rgbToHvs(img):
    im = np.array(img.mtrx).astype(np.uint8)
    img.mtrx = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
    return img

@Log
def rgbToLab(img):
    im = np.array(img.mtrx).astype(np.uint8)
    img.mtrx = cv2.cvtColor(im, cv2.COLOR_BGR2LAB)
    return img

@Log
def rgbToGrey(img):
    im = np.array(img.mtrx).astype(np.uint8)
    img.mtrx = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    return img

@Log
def elekKeresese(img, minv, maxv):
    im = np.array(img.mtrx).astype(np.uint8)
    elek = cv2.Canny(im,minv,maxv)
    img.mtrx = elek
    return img

@Log
def kepMentese(img, name):
    im = np.array(img.mtrx).astype(np.uint8)
    status = cv2.imwrite('{}/{}.png'.format(os.getcwd(),name.split('.')[0]),im)
