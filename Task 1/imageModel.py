import numpy as np
import matplotlib.image as mpimg

def gray(rgb):
    if (rgb.ndim == 2):
        return rgb
    else:
        return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])
        

class ImageModel():

    """
    A class that represents the ImageModel"
    """
    def __init__(self, imgPath: str):
        self.imgPath = imgPath
        print(imgPath)
        ###
        # ALL the following properties should be assigned correctly after reading imgPath 
        ###
        self.imgByte = mpimg.imread(self.imgPath)
        self.imgHeight = self.imgByte.shape[0]
        self.imgWidth = self.imgByte.shape[1]
    
    @staticmethod
    def gray(rgb):
        if (rgb.ndim == 2):
            return rgb
        else:
            return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

                