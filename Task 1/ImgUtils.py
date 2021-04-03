import numpy as np 
from PIL import Image

np.seterr(over='ignore')

class ImgUtils:

    def __init__(self,img : np.ndarray):
        self.img = img

    def histogramEqualization(self):

        shape = self.img.shape
        pixel_depth = 2**(self.img.dtype.itemsize * 8) 
        # no_channel = shape[-1]
        # print(f"no_channels : {no_channel}")
        img_copy = np.copy(self.img)
        #  separete each color channel  
        b, g, r    = img_copy[:, :, 0], img_copy[:, :, 1], img_copy[:, :, 2]
        # count each pixel value in each color channel 
        r_hist = np.bincount(r.flatten())
        # print(F"r_hist.shape {r_hist.shape}")
        # print(F"r_hist.shape {r_hist[255]}")
        # print(F"r_hist.shape {(r == 255).sum()}")
        g_hist = np.bincount(g.flatten())
        b_hist = np.bincount(b.flatten())
        r_sum = 0 
        g_sum = 0
        b_sum = 0
        r_cdf = [0] * pixel_depth  
        g_cdf = [0] * pixel_depth
        b_cdf = [0] * pixel_depth
        
        
        # compute CDF over each channel 
        for i in range(pixel_depth):
            r_sum = r_sum + r_hist[i]
            r_cdf[i] = r_sum 

            g_sum = g_sum + g_hist[i]
            g_cdf[i] = g_sum 

            b_sum = b_sum + b_hist[i]
            b_cdf[i] = b_sum 

        # print(f"r_hist {(r_hist[-1])}")
        # print(f"r_cdf {(r_cdf[-1])}")
        # print(f"g_cdf {(g_cdf[-1])}")
        r_cdf_min = r_cdf[0] 
        g_cdf_min = g_cdf[0]
        b_cdf_min = b_cdf[0]
        # print(f"b_cdf_min {(b_cdf[0])}")
        # print(f"b_cdf_min {(b_cdf_min)}")

        r_fin = [0] * pixel_depth  
        g_fin = [0] * pixel_depth
        b_fin = [0] * pixel_depth
        tot_pixels = (shape[0] * shape [1])
        # compute  histogram equalization
        for i in range(pixel_depth):
            r_fin[i] = round( ((r_cdf[i] - r_cdf_min ) / (tot_pixels - r_cdf_min) ) * (pixel_depth - 1) )
            g_fin[i] = round( ((g_cdf[i] - g_cdf_min ) / (tot_pixels - g_cdf_min) ) * (pixel_depth - 1) )
            b_fin[i] = round( ((b_cdf[i] - b_cdf_min ) / (tot_pixels - b_cdf_min) ) * (pixel_depth - 1) )

        # map old pixel vals
        # print(f"old r: {r}")
        # print(f"old r: {r.shape}")
        for i , pixel in np.ndenumerate(r):
            r[i] = r_fin[r[i]]
            g[i] = g_fin[g[i]]
            b[i] = b_fin[b[i]]

        # print(r_hist[0:10])
        # print(r_cdf[0:10])
        # print(r_fin[0:10])
        # print(f"new r {r}")
        # print(f"new r {r.shape}")

        img_copy[:,:,0] =  b 
        img_copy[:,:,1] =  g 
        img_copy[:,:,2] =  r 

        # print(f"b_hist : {b_hist}")
        # print(f"g_hist : {g_hist}")
        # print(f"r_hist : {r_hist}")
        print(img_copy.shape)
        return img_copy

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

    im1 = imgReader("./img1.jpg")
    print(f"im1 shape: {im1.shape}")
    # print(f"im1 type: {type(im1)}")

    # im2 = imgReader("./img2.jpg")
    # print(f"im2 shape: {im2.shape}")
    # print(f"im2 type: {type(im2)}")

    # im0 = np.zeros(im1.shape)
    imUtil = ImgUtils(im1)
    equalized = imUtil.histogramEqualization()
    # thresholded = imUtil.globalThresholding(250)
    # hybrid = imUtil.hybrid(im2)

    # print(f"hybrid shape: {hybrid.shape}")
    # print(f"hybrid type: {type(hybrid)}")

    im3 = Image.fromarray(equalized.astype(np.uint8))
    im3.show()



