import numpy as np 
from PIL import Image

np.seterr(over='ignore')

class ImgUtils:

    def __init__(self,img : np.ndarray):
        self.img = img


    def hybrid(self,img2 : np.ndarray) -> np.ndarray:

        # check if dimensions matche 
        shape = self.img.shape

        if (shape == img2.shape):

            hybrid = np.zeros(shape,dtype=np.uint8)

            for i , pixel in np.ndenumerate(self.img):
                hybrid[i] =  pixel + img2[i]
        else:
            raise Exception(f"input image must match size: {shape} ") 


        return hybrid



def imgReader(imgPath:str):
    im = Image.open(imgPath)
    im.show()
    return np.asarray(im,dtype=np.uint8)

im1 = imgReader("./img1.jpg")
# print(f"im1 shape: {im1.shape}")
# print(f"im1 type: {type(im1)}")

im2 = imgReader("./img2.jpg")
# print(f"im2 shape: {im2.shape}")
# print(f"im2 type: {type(im2)}")


imUtil = ImgUtils(im1)


hybrid = imUtil.hybrid(im2)
# print(f"hybrid shape: {hybrid.shape}")
# print(f"hybrid type: {type(hybrid)}")

im3 = Image.fromarray(hybrid.astype(np.uint8))
im3.show()



