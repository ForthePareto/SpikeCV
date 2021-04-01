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


    def globalThresholding(self,threshold : int) -> np.ndarray:

        img_copy = np.copy(self.img)
        pixel_depth = 2**(self.img.dtype.itemsize * 8) 
        
        print(f'pixel_depth: {pixel_depth}')
        print(f'shape: {self.img.shape}')
        
        if ( 0 <= threshold <= pixel_depth - 1):
            for i,pixel in np.ndenumerate(img_copy):
                img_copy[i] = (pixel_depth - 1) if pixel >= threshold else 0
        else: 
            raise Exception(f"Threshold valuse must be in range: [0,{pixel_depth - 1}]")
        return img_copy





if __name__ == '__main__':

    def imgReader(imgPath:str):
        im = Image.open(imgPath)
        im.show()
        return np.asarray(im,dtype=np.uint8)

    # im1 = imgReader("./img1.jpg")
    # print(f"im1 shape: {im1.shape}")
    # print(f"im1 type: {type(im1)}")

    # im2 = imgReader("./img2.jpg")
    # print(f"im2 shape: {im2.shape}")
    # print(f"im2 type: {type(im2)}")

    # im0 = np.zeros(im1.shape)
    imUtil = ImgUtils(im2)

    # thresholded = imUtil.globalThresholding(250)
    # hybrid = imUtil.hybrid(im2)

    # print(f"hybrid shape: {hybrid.shape}")
    # print(f"hybrid type: {type(hybrid)}")

    # im3 = Image.fromarray(thresholded.astype(np.uint8))
    # im3.show()



