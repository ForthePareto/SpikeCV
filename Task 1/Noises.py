import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
class Noise:
    
    @staticmethod
    def uniform(image: np.ndarray) -> np.ndarray:
        pass
    @staticmethod    
    def gaussian(image: np.ndarray,mean=0,variance=0.1) -> np.ndarray:
        sigma = variance**0.5
        gauss = np.random.normal(mean,sigma,(image.shape))
        gauss = gauss.reshape(image.shape)*np.max(img)
        noisy = image + gauss
        return noisy
    @staticmethod
    def salt_pepper(image: np.ndarray) -> np.ndarray:
        pass

if __name__ == '__main__':
    img = mpimg.imread("EvV4-uOWYAQOM1x.jpg",)
    noisy = Noise.gaussian(img)
    plt.imshow(noisy,cmap="gray")
    plt.show()
