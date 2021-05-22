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

    def global_thresholding(self, img=None, n_bins=255, plot=False):
        """Finding thresholds for bi/multispectral thresholding using Otsu
        """
        if img is None:
            img = self.img
        # get pixels intensities distribution
        n_bins = int(np.max(img))
        print(n_bins)
        histogram1, bin_edges = np.histogram(img, bins=n_bins)

        # print(histogram1.shape, bin_edges.shape)
        # Normalize distribution to get the probabilities of each pixel intensity
        histogram = np.divide(histogram1.reshape(-1), histogram1.max())
        bin_mids = (bin_edges[:-1] + bin_edges[1:]) / 2.
        # print(bin_mids)
        # Iterate over all thresholds (indices) and get the probabilities w1(t), w2(t)
        weight1 = np.cumsum(histogram)
        weight2 = np.cumsum(histogram[::-1])[::-1]

        # Get the class means mu0(t)
        mean1 = np.cumsum(histogram * bin_mids) / weight1
        # Get the class means mu1(t)
        mean2 = (np.cumsum((histogram * bin_mids)[::-1]) / weight2[::-1])[::-1]

        inter_class_variance = weight1[:-1] * \
            weight2[1:] * (mean1[:-1] - mean2[1:]) ** 2

        sorted_threshs = np.argsort(inter_class_variance)[::-1]
        # print(sorted_threshs)

        # Maximize the inter_class_variance function val
        index_of_max_val = np.argmax(inter_class_variance)
        threshold = bin_mids[:-1][index_of_max_val]
        # add threshold to the class attributes list of thresholds
        self.thresholds = []
        self.thresholds.append(threshold)
        # print("thresholding result: ", threshold)
        result = Otsu._binarize(img, threshold)
        if plot:
            Otsu._plot_image_historgram_pair(
                img, result, histogram1, n_bins, self.thresholds)
        return result

    def global_spectral_thresholding(self, img=None,n_bins=255, plot=False):
        """Finding thresholds for bi/multispectral thresholding using Otsu
        """
        if img is None:
            img = self.img
        # get pixels intensities distribution
        n_bins = int(np.max(img))
        print(n_bins)
        histogram1, bin_edges = np.histogram(img, bins=n_bins)
        threshold,thresholdIdx,_ = self.get_best_threshold(histogram1, bin_edges)
        threshold_left, _,cost2 = self.get_best_threshold(histogram1[:thresholdIdx], bin_edges[:thresholdIdx+1]) 
        threshold_right, _,cost3 = self.get_best_threshold(histogram1[thresholdIdx:], bin_edges[thresholdIdx:]) 
        # add threshold to the class attributes list of thresholds
        print(cost3.shape)
        threshold2 = threshold_left if cost2>cost3 else threshold_right
        self.thresholds = []
        self.thresholds.append(threshold)
        self.thresholds.append(threshold2)
        # print("thresholding result: ", threshold)
        result = Otsu._digitize(img, [threshold,threshold2])
        if plot:
            Otsu._plot_image_historgram_pair(
                img, result, histogram1, n_bins, self.thresholds)
        return result

    def get_best_threshold(self, histogram, bin_edges):
        # Normalize distribution to get the probabilities of each pixel intensity
        histogram = np.divide(histogram.reshape(-1), histogram.max())
        bin_mids = (bin_edges[:-1] + bin_edges[1:]) / 2.
        # print(bin_mids)
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
        return threshold, index_of_max_val , np.max(inter_class_variance)

    def local_thresholding(self, block_length=25, plot=False):
        img = np.copy(self.img)
        locally_thresholded = self.local_processing(
            img, radius=block_length, func=self.global_thresholding)
        if plot:
            f, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 6))
            ax[0].imshow(img, cmap="gray")
            ax[0].set_title("Original Image")
            ax[0].axis("off")
            ax[1].imshow(locally_thresholded, cmap="gray")
            plt.axis("off")
            plt.show()
        return locally_thresholded
    def local_spectral_thresholding(self, block_length=25, plot=False):
        img = np.copy(self.img)
        locally_thresholded = self.local_processing(
            img, radius=block_length, func=self.global_spectral_thresholding)
        if plot:
            f, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 6))
            ax[0].imshow(img, cmap="gray")
            ax[0].set_title("Original Image")
            ax[0].axis("off")
            ax[1].imshow(locally_thresholded, cmap="gray")
            plt.axis("off")
            plt.show()
        return locally_thresholded

    @classmethod
    def _binarize(cls, img, threshold):
        result = np.copy(img)
        result[img > threshold] = 255
        result[img <= threshold] = 0
        return result
    @classmethod
    def _digitize(cls, img, thresholds):
        # result = np.dstack((np.copy(img),np.zeros_like(img),np.zeros_like(img)))
        result = np.copy(img)
        print(result.shape)
        low_thresh = np.min(thresholds)
        high_thresh = np.max(thresholds)
        result[img <= low_thresh] = 0
        result[img > high_thresh] = 255
       
        result[np.logical_and((low_thresh<=img ),  (img<= high_thresh))] = 128
        return result

    @classmethod
    def _plot_image_historgram_pair(cls, img, result, histogram, n_bins, thresholds=[]):
        f, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 6))
        ax[0].imshow(result, cmap="gray")
        ax[1].set_title("historgram")
        ax[0].axis("off")
        ax[1].hist(img.ravel(), bins=range(1, n_bins),
                   color='#0504ab', alpha=0.55, rwidth=0.57)
        ax[1].set_title("historgram")
        print(np.max(histogram))
        if len(thresholds) > 0:
            ax[1].vlines(thresholds, 0, np.max(histogram),  color='r')
        plt.show()

    def local_processing(self, img, radius=35, func=None):
        rows, cols = img.shape[0], img.shape[1]
        def f(x): return func(x)

        result = np.copy(img)
        for r in range(0, rows-radius, radius):
            for c in range(0, cols-radius, radius):
                # block = img[r:(min(r + radius, rows)),
                #             c:(min(c + radius, cols))]

                block = img[r:(r + radius),
                            c:(c + radius)]
                block_proccessed = f(block)
                # result[r:min(r + radius, rows), c:min(c +
                #                                       radius, cols)] = block_proccessed
                result[r:(r + radius),
                       c:(c + radius)] = block_proccessed
        for r in range(0, rows-radius, radius):
            block = img[r:(r + radius),
                        cols-radius:]
            block_proccessed = f(block)
            result[r:(r + radius),
                   cols-radius:] = block_proccessed

        for c in range(0, cols-radius, radius):
            block = img[rows-radius:,
                        c:(c + radius)]

            block_proccessed = f(block)
            result[rows-radius:,
                   c:(c + radius)] = block_proccessed

        return result


if __name__ == '__main__':
    img = mpimg.imread("testImgs/gray3.jpg")
    img = gray(img)
    OtsuThresholder = Otsu(img)
    # OtsuThresholder.global_thresholding(plot=True)
    OtsuThresholder.global_spectral_thresholding(plot=True)
    OtsuThresholder.local_spectral_thresholding(plot=True,block_length=77)
    # OtsuThresholder.local_thresholding(block_length=75,plot=True)
