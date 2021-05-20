import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from Filters import gray


class Thresholding:
    """
    Thresholding API
    """
    @staticmethod
    def otsu(img: np.ndarray, scope="global") -> np.ndarray:
        """
        local and global bimodal thresholding 
        """
        pass

    @staticmethod
    def spectral(img: np.ndarray, scope="global") -> np.ndarray:
        """
        local and global multimodal thresholding 
        """
        pass


class Otsu:
    def __init__(self, img: np.ndarray):

        self.img = img
        self.thresholds = []

    def find_global_thresholds(self, n_bins=255, show=False):
        # get pixels intensities distribution
        histogram1, bin_edges = np.histogram(self.img, bins=n_bins)
        # Normalize distribution to get the probabilities of each pixel intensity
        histogram = np.divide(histogram1.reshape(-1), histogram1.max())
        bin_mids = (bin_edges[:-1] + bin_edges[1:]) / 2.
        print(bin_mids)
        # Iterate over all thresholds (indices) and get the probabilities w1(t), w2(t)

        weight1 = np.cumsum(histogram)

        weight2 = np.cumsum(histogram[::-1])[::-1]

        # Get the class means mu0(t)

        mean1 = np.cumsum(histogram * bin_mids) / weight1
        # Get the class means mu1(t)
        mean2 = (np.cumsum((histogram * bin_mids)[::-1]) / weight2[::-1])[::-1]

        inter_class_variance = weight1[:-1] * \
            weight2[1:] * (mean1[:-1] - mean2[1:]) ** 2

        # Maximize the inter_class_variance function val

        index_of_max_val = np.argmax(inter_class_variance)
        threshold = bin_mids[:-1][index_of_max_val]

        print("thresholding result: ", threshold)
        if show:
            result = np.copy(img)
            result[img > threshold] = 255
            result[img <= threshold] = 0
            f, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 6))
            ax[0].imshow(result, cmap="gray")
            ax[1].hist(histogram1, bins=list(range(n_bins)))
            plt.show()
        self.thresholds = []
        self.thresholds.append(threshold)


if __name__ == '__main__':
    img = mpimg.imread("testImgs/gray3.jpg")
    img = gray(img)
    thresholder = Otsu(img)
    thresholder.find_global_thresholds()
