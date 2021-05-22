import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from Filters import gray
np.seterr(divide='ignore', invalid='ignore')


class Thresholding:
    """
    Thresholding API
    """
    @staticmethod
    def optimal(img: np.ndarray, scope="global", block_length=25) -> np.ndarray:
        scope = scope.lower()
        if scope not in ["global", "local"]:
            raise ValueError(
                "Undefined scope, please choose either global or local")
        img = gray(img)
        optimalThresholder = OptimalThresholding(img)
        
        if scope == "global":
            return optimalThresholder.global_thresholding()
        elif scope == "local":
            return optimalThresholder.local_thresholding(block_length=block_length)

    @staticmethod
    def bimodal(img: np.ndarray, scope="global", block_length=25) -> np.ndarray:
        """
        local and global bimodal thresholding 
        """
        scope = scope.lower()
        if scope not in ["global", "local"]:
            raise ValueError(
                "Undefined scope, please choose either global or local")
        img = gray(img)
        OtsuThresholder = Otsu(img)
        if scope == "global":
            return OtsuThresholder.global_thresholding()
        elif scope == "local":
            return OtsuThresholder.local_thresholding(block_length=block_length)

    @staticmethod
    def spectral(img: np.ndarray, scope="global", block_length=25) -> np.ndarray:
        """
        local and global multimodal thresholding 
        """
        scope = scope.lower()
        if scope not in ["global", "local"]:
            raise ValueError(
                "Undefined scope, please choose either global or local")
        img = gray(img)
        OtsuThresholder = Otsu(img)
        if scope == "global":
            return OtsuThresholder.global_spectral_thresholding()
        elif scope == "local":
            return OtsuThresholder.local_spectral_thresholding(block_length=block_length)


class Otsu:
    def __init__(self, img: np.ndarray):

        self.img = img
        self.thresholds = []

    def global_thresholding(self, img=None, n_bins=255, plot=False):
        """Finding thresholds and applying bimodal thresholding using Otsu
        """
        if img is None:
            img = self.img
        # get pixels intensities distribution
        n_bins = int(np.max(img))
        histogram1, bin_edges = np.histogram(img, bins=n_bins)

        threshold, _, _ = self.get_best_threshold(histogram1, bin_edges)
        # add threshold to the class attributes list of thresholds
        self.thresholds = []
        self.thresholds.append(threshold)
        # binarize(black & white) the image based on the calculated threshold
        bimodal_segmented_image = Otsu._binarize(img, threshold)
        if plot:
            Otsu._plot_image_historgram_pair(
                img, bimodal_segmented_image, histogram1, n_bins, self.thresholds)
        return bimodal_segmented_image

    def global_spectral_thresholding(self, img=None, n_bins=255, plot=False):
        """Finding thresholds for spectral thresholding using Otsu 
        """
        if img is None:
            img = np.copy(self.img)
        # get pixels intensities distribution
        n_bins = int(np.max(img))
        histogram1, bin_edges = np.histogram(img, bins=n_bins)
        # get best threshold that maximizes the between class variances in the given histogram
        threshold, thresholdIdx, _ = self.get_best_threshold(
            histogram1, bin_edges)
        # Find the second threshold so the histogram is splited into 3 regions
        # choose the best threshold either right or left from the first threshold
        threshold_left, _, cost2 = self.get_best_threshold(
            histogram1[:thresholdIdx], bin_edges[:thresholdIdx+1])
        threshold_right, _, cost3 = self.get_best_threshold(
            histogram1[thresholdIdx:], bin_edges[thresholdIdx:])
        # choosing one of the left or right thresholds, based on cost
        threshold2 = threshold_left if cost2 > cost3 else threshold_right

        # save threshold to the class attributes list of thresholds to be used in histogram pl
        self.thresholds = []
        self.thresholds.append(threshold)
        self.thresholds.append(threshold2)
        # each pixel will get one of 3 colors/intesies based on it's region in the distribution
        result = Otsu._digitize(img, [threshold, threshold2])

        if plot:
            Otsu._plot_image_historgram_pair(
                img, result, histogram1, n_bins, self.thresholds)
        return result

    def get_best_threshold(self, histogram, bin_edges):
        # normalize distribution to get the probabilities of each pixel intensity
        histogram = np.divide(histogram.reshape(-1), histogram.max())
        # get midpoints of each bin
        bin_mids = (bin_edges[:-1] + bin_edges[1:]) / 2.
        # Iterate over all thresholds (indices) and get the probabilities w1(t), w2(t)
        weight1 = np.cumsum(histogram)
        weight2 = np.cumsum(histogram[::-1])[::-1]

        # Get the class means mu0(t)
        mean1 = np.divide(np.cumsum(histogram * bin_mids), weight1)
        # Get the class means mu1(t)
        mean2 = np.divide(np.cumsum((histogram * bin_mids)
                                    [::-1]), weight2[::-1])[::-1]

        between_class_variance = weight1[:-1] * \
            weight2[1:] * (mean1[:-1] - mean2[1:]) ** 2

        # Maximize the inter_class_variance function val
        index_of_max_val = np.argmax(between_class_variance)

        threshold = bin_mids[:-1][index_of_max_val]
        return threshold, index_of_max_val, np.max(between_class_variance)

    def local_thresholding(self, img=None, block_length=25, plot=False):
        if img is None:
            img = np.copy(self.img)

        locally_thresholded = local_processing(
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
        locally_thresholded = local_processing(
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

    @staticmethod
    def local_processing(img, radius=35, func=None):
        rows, cols = img.shape[0], img.shape[1]
        # The callback function to be applied
        def f(x): return func(x)

        result = np.copy(img)
        # iterate over image in strided blocks with the given size: (radius,radius)
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

        # Because many images are not in square size, there will be issues in the lower right boundaries
        # so we apply the function the these boundaries specifically

        # So, apply on the last row of blocks
        for r in range(0, rows-radius, radius):
            block = img[r:(r + radius),
                        cols-radius:]
            block_proccessed = f(block)
            result[r:(r + radius),
                   cols-radius:] = block_proccessed
        # apply on the last column of blocks
        for c in range(0, cols-radius, radius):
            block = img[rows-radius:,
                        c:(c + radius)]

            block_proccessed = f(block)
            result[rows-radius:,
                   c:(c + radius)] = block_proccessed
        block = img[rows-radius:,
                    cols-radius:]
        # apply on the lowest right corner block
        block_proccessed = f(block)
        result[rows-radius:,
               cols-radius:] = block_proccessed

        return result

    @classmethod
    def _binarize(cls, img, threshold):
        return binarize(cls, img, threshold)

    @classmethod
    def _digitize(cls, img, thresholds):      
        return digitize( img, thresholds)

    @classmethod
    def _plot_image_historgram_pair(cls, img, result, histogram, n_bins, thresholds=[]):
        f, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 6))
        ax[0].imshow(result, cmap="gray")
        ax[1].set_title("historgram")
        ax[0].axis("off")
        ax[1].hist(img.ravel(), bins=range(1, n_bins),
                   color='#0504ab', alpha=0.55, rwidth=0.57)
        ax[1].set_title("historgram")
        if len(thresholds) > 0:
            ax[1].vlines(thresholds, 0, np.max(histogram),  color='r')
        plt.show()


class OptimalThresholding:
    def __init__(self, img):
        self.img = img

    def global_thresholding(self, img=None,plot=False):
        if img is None:
            img = self.img
        # assume the 4 corners of the image contains the background pixels
        # the rest pixels contains the foreground

        # get mean of the image corners
        initial_background_mean = np.mean(get_img_corner_pixels(img))
        # get mean of the foreground pixels which is the mean of the all pixels except background
        initial_foreground_mean = np.mean(img) - initial_background_mean

        threshold = (initial_background_mean+initial_foreground_mean) / 2
        while True:
            previous_threshold = threshold
            background_pixels = img[img <= threshold]
            foreground_pixels = img[img > threshold]
            try:
                background_pixels_mean = np.mean(background_pixels)
            except:
                background_pixels_mean = 0
            try:
                foreground_pixels_mean = np.mean(foreground_pixels)
            except:
                foreground_pixels_mean = 0
            threshold = (background_pixels_mean + foreground_pixels_mean) / 2
            if previous_threshold == threshold:
                break
        result = binarize(img,threshold)
        if plot:
            n_bins = int(np.max(img))
            hist, bin_edges = np.histogram(img, bins=n_bins)
            Otsu._plot_image_historgram_pair(
                img, result, hist, n_bins, [threshold])

        return result
    


    def local_thresholding(self, img=None, block_length=25, plot=False):
        if img is None:
            img = np.copy(self.img)

        locally_thresholded = local_processing(
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

def get_img_corner_pixels(img):
    r, c = img.shape[0], img.shape[1]
    return [img[0, 0], img[0, c-1], img[r-1, c-1], img[r-1, 0]]


def local_processing(img, radius=35, func=None):
    rows, cols = img.shape[0], img.shape[1]
    # The callback function to be applied
    def f(x): return func(x)

    result = np.copy(img)
    # iterate over image in strided blocks with the given size: (radius,radius)
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

    # Because many images are not in square size, there will be issues in the lower right boundaries
    # so we apply the function the these boundaries specifically

    # So, apply on the last row of blocks
    for r in range(0, rows-radius, radius):
        block = img[r:(r + radius),
                    cols-radius:]
        block_proccessed = f(block)
        result[r:(r + radius),
               cols-radius:] = block_proccessed
    # apply on the last column of blocks
    for c in range(0, cols-radius, radius):
        block = img[rows-radius:,
                    c:(c + radius)]

        block_proccessed = f(block)
        result[rows-radius:,
               c:(c + radius)] = block_proccessed
    block = img[rows-radius:,
                cols-radius:]
    # apply on the lowest right corner block
    block_proccessed = f(block)
    result[rows-radius:,
           cols-radius:] = block_proccessed

    return result


def binarize(img, threshold):

    result = np.copy(img)
    result[img >= threshold] = 255
    result[img < threshold] = 0
    return result


def digitize(img, thresholds):
    # result = np.dstack((np.copy(img),np.zeros_like(img),np.zeros_like(img)))
    result = np.copy(img)
    low_thresh = np.min(thresholds)
    high_thresh = np.max(thresholds)
    result[img <= low_thresh] = 0
    result[img > high_thresh] = 255

    result[np.logical_and((low_thresh <= img),
                          (img <= high_thresh))] = 128
    return result


if __name__ == '__main__':
    img = mpimg.imread("testImgs/Lenna.jpg")
    img = gray(img)
    OtsuThresholder = Otsu(img)
    # OtsuThresholder.global_thresholding(plot=True)
    # OtsuThresholder.global_spectral_thresholding(plot=True)
    # OtsuThresholder.local_spectral_thresholding(plot=True, block_length=77)
    # OtsuThresholder.local_thresholding(block_length=77, plot=True)
    # Thresholding.spectral(img, scope="global")
    optimalThresholder = OptimalThresholding(img)
    # optimalThresholder.global_thresholding(plot=True)
    optimalThresholder.local_thresholding(block_length=77, plot=True)
