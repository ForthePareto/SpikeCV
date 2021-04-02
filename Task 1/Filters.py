import numpy as np
from scipy import signal
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from Noises import Noise
from collections import OrderedDict
from typing import Sequence


def number_of_image_channels(img):
    if len(img.shape) == 3 and img.shape[2] == 3:  # 3-channels e.g rgb img
        return 3
    elif len(img.shape) == 2 or img.shape[2] == 1:
        return 2
    else:
        raise ValueError("Undefined image size")


def is_convolution_in_bounds(img_shape: list, kernel_edges: np.array):
    rows = list(range(img_shape[0]))
    cols = list(range(img_shape[1]))
    if (kernel_edges[0] not in cols) or (kernel_edges[1] not in cols) or (kernel_edges[2] not in rows) or (kernel_edges[3] not in rows):
        return False
    else:
        return True


class Filter:

    @staticmethod
    def average(img: np.ndarray, kernel_size=3) -> np.ndarray:
        """average [summary]

        Args:
            img (np.ndarray): [description]
            kernel (int, optional): [description]. Defaults to 3.

        Returns:
            np.ndarray: [description]
        """
        n_ImgChannels = number_of_image_channels(img)
        avg_kernel = Kernel(
            "average", kernel_size=kernel_size, n_channels=n_ImgChannels)
        output = signal.convolve(img, avg_kernel)
        print(output.shape)
        return output

    @staticmethod
    def gaussian(img: np.ndarray, kernel_size=3, std=1) -> np.ndarray:
        """gaussian [summary]

        Args:
            img (np.ndarray): [description]
            kernel_size (int, optional): [description]. Defaults to 3.
            std (int, optional): [description]. Defaults to 1.

        Returns:
            np.ndarray: [description]
        """

        kernel = Kernel.gaussian(kernel_size=kernel_size, std=std)

    @staticmethod
    def median(img: Sequence[int], kernel_size=3) -> np.ndarray:
        """median [summary]

        Args:
            img (np.ndarray): [description]
            kernel (int, optional): [description]. Defaults to 3.

        Returns:
            np.ndarray: [description]
        """

        temp = []
        filter_size = kernel_size
        indexer = filter_size // 2
        data = img.copy()
        data_final = []
        data_final = np.zeros((len(data), len(data[0])))
        for i in range(len(data)):  # rows

            for j in range(len(data[0])):  # columns

                for z in range(filter_size):
                    if i + z - indexer < 0 or i + z - indexer > len(data) - 1:
                        for c in range(filter_size):
                            temp.append(0)
                    else:
                        if j + z - indexer < 0 or j + indexer > len(data[0]) - 1:
                            temp.append(0)
                        else:
                            for k in range(filter_size):
                                temp.append(
                                    data[i + z - indexer][j + k - indexer])

                temp.sort()
                data_final[i][j] = temp[len(temp) // 2]
                temp = []
        return data_final

        # n_rows, n_cols = img.shape[0], img.shape[1]
        # output= np.zeros((n_rows-kernel+1, n_cols-kernel+1))
        # output = img[1:n_rows-1,1:n_cols-1]
        # convoltution_mask = np.zeros((kernel, kernel))

        # edge_name = ["kernel_left_x", "kernel_right_x",
        #              "kernel_upper_y", "kernel_lower_y"]
        # kernel_edges = np.zeros(4)
        # count =
        # for row in range(n_rows-1):
        #     for col in range(n_cols-1):
        #         kernel_center = np.array([(kernel//2)+row, (kernel//2)+col])
        #         kernel_left_x = kernel_edges[0] = kernel_center[0] - kernel//2
        #         kernel_right_x = kernel_edges[1] = kernel_center[0] + kernel//2
        #         kernel_upper_y = kernel_edges[2] = kernel_center[1] - kernel//2
        #         kernel_lower_y = kernel_edges[3] = kernel_center[1] + kernel//2

        #         if (is_convolution_in_bounds(img.shape, kernel_edges) == False) :
        #             continue
        #         # print(kernel_center)
        #         # print(kernel_edges)
        #         convoltution_mask[:, :] = img[kernel_upper_y:(kernel_lower_y +
        #                                       1), kernel_left_x:(kernel_right_x+1)]
        #         # print(convoltution_mask.shape)
        #         sorted_mask = np.sort(
        #             convoltution_mask.flatten(), kind="mergesort")
        #         print(sorted_mask)
        #         median = sorted_mask[len(sorted_mask)//2+1]
        #         print("pixel is: ",img[row,col])
        #         print("median is :", median)
        #         # print(median)
        #         output[row, col] = median
        # return output

    @staticmethod
    def sobel(img: np.ndarray, direction="x", kernel_size=3) -> np.ndarray:
        """sobel [summary]

        Args:
            img (np.ndarray): [description]
            direction (str, optional): [description]. Defaults to "x".
            kernel_size (int, optional): [description]. Defaults to 3.

        Returns:
            np.ndarray: [description]
        """
        sobel_kernel = Kernel.sobel(
            direction=direction, kernel_size=kernel_size)
        output = signal.convolve(img, sobel_kernel)
        return output

    @staticmethod
    def prewitt(img: np.ndarray, kernel_size=3, direction="x") -> np.ndarray:
        """prewitt [summary]

        Args:
            img (np.ndarray): [description]
            direction (str, optional): [description]. Defaults to "x".

        Returns:
            np.ndarray: [description]
        """
        prewitt_kernel = Kernel.prewitt(
            direction=direction, kernel_size=kernel_size)

    @staticmethod
    def canny(img: np.ndarray, min_value: int, max_value: int) -> np.ndarray:
        """canny [The Process of Canny edge detection algorithm can be broken down to 5 different steps:

                    Apply Gaussian filter to smooth the image in order to remove the noise
                    Find the intensity gradients of the image
                    Apply gradient magnitude thresholding or lower bound cut-off suppression to get rid of spurious response to edge detection
                    Apply double threshold to determine potential edges
                    Track edge by hysteresis: Finalize the detection of edges by suppressing all the other edges that are weak and not connected to strong edges.]

        Args:
            img (np.ndarray): [description]
            min_value (int): [description]
            max_value (int): [description]

        Returns:
            np.ndarray: [description]
        """
        pass

    # https://www.youtube.com/watch?v=9mLeVn8xzMw
    def low_pass_frequency(img: np.ndarray, cut_off: int) -> np.ndarray:
        """low_pass_frequency [https://plotly.com/python/v3/fft-filters/]

        Args:
            img (np.ndarray): [description]
            cutoff (int): [description]

        Returns:
            np.ndarray: [description]
        """
        pass

    # https://www.youtube.com/watch?v=9mLeVn8xzMw
    def high_pass_frequency(img: np.ndarray, cut_off: int) -> np.ndarray:
        """low_pass_frequency [https://plotly.com/python/v3/fft-filters/]

        Args:
            img (np.ndarray): [description]
            cutoff (int): [description]

        Returns:
            np.ndarray: [description]
        """
        pass


def convolve(image, filter, padding=(1, 1)):
    # Assuming the image has channels as the last dimension.
    # filter.shape -> (kernel_size, kernel_size, channels)
    # image.shape -> (width, height, channels)
    # For this to work neatly, filter and image should have the same number of channels
    # Alternatively, filter could have just 1 channel or 2 dimensions

    if(image.ndim == 2):
        # Convert 2D grayscale images to 3D
        image = np.expand_dims(image, axis=-1)
    if(filter.ndim == 2):
        filter = np.repeat(np.expand_dims(filter, axis=-1),
                           image.shape[-1], axis=-1)  # Same with filters
    if(filter.shape[-1] == 1):
        # Give filter the same channel count as the image
        filter = np.repeat(filter, image.shape[-1], axis=-1)

    #print(filter.shape, image.shape)
    assert image.shape[-1] == filter.shape[-1]
    size_x, size_y = filter.shape[:2]
    width, height = image.shape[:2]

    output_array = np.zeros(((width - size_x + 2*padding[0]) + 1,
                             (height - size_y + 2*padding[1]) + 1,
                             image.shape[-1]))  # Convolution Output: [(W−K+2P)/S]+1

    padded_image = np.pad(image, [
        (padding[0], padding[0]),
        (padding[1], padding[1]),
        (0, 0)
    ])

    # -size_x + 1 is to keep the window within the bounds of the image
    for x in range(padded_image.shape[0] - size_x + 1):
        for y in range(padded_image.shape[1] - size_y + 1):

            # Creates the window with the same size as the filter
            window = padded_image[x:x + size_x, y:y + size_y]

            # Sums over the product of the filter and the window
            output_values = np.sum(filter * window, axis=(0, 1))

            # Places the calculated value into the output_array
            output_array[x, y] = output_values

    return output_array


class Kernel:
    @staticmethod
    def average(kernel_size=3, n_channels=2, plot=False):
        avg_kernel = np.ones((kernel_size, kernel_size)) if n_channels == 2 else np.ones(
            (kernel_size, kernel_size, 3))
        avg_kernel = (1/avg_kernel.size) * avg_kernel
        if plot:
            Kernel._plot(avg_kernel)
        return avg_kernel

    @staticmethod
    def gaussian(kernel_size=3, std=1, plot=False):
        kernel_size = kernel_size//2
        x = np.arange(-kernel_size, kernel_size+1, 1)
        print(x)
        y = np.arange(-kernel_size, kernel_size+1, 1)
        x, y = np.meshgrid(x, y)
        # gauss_kernel = (1/(2*np.pi*std**2))*np.exp(-((x**2+y**2)/(2*std**2)))
        gauss_kernel = np.exp(-((x**2+y**2)/(2*std**2)))
        gauss_kernel = gauss_kernel/np.sum(gauss_kernel)
        if plot:
            Kernel._plot(gauss_kernel)
        return gauss_kernel

    @staticmethod
    def sobel(direction="x", kernel_size=3, plot=False):
        axis = direction.lower()
        kernel_shape = (kernel_size, kernel_size)
        sobel_kernel = np.zeros(kernel_shape)
        p = [(j, i) for j in range(kernel_shape[0])
             for i in range(kernel_shape[1])
             if not (i == (kernel_shape[1] - 1)/2. and j == (kernel_shape[0] - 1)/2.)]

        for j, i in p:
            j_ = int(j - (kernel_shape[0] - 1)/2.)
            i_ = int(i - (kernel_shape[1] - 1)/2.)
            sobel_kernel[j, i] = (
                i_ if axis == "x" else j_)/float(i_*i_ + j_*j_)
        if plot:
            Kernel._plot(sobel_kernel)
        return sobel_kernel

    @staticmethod
    def Prewitt(self, **kwgs):
        pass

    @classmethod
    def _plot(cls, kernel):
        plt.imshow(kernel, cmap=plt.get_cmap(
            'jet'), interpolation='nearest')
        plt.colorbar()
        plt.show()


if __name__ == '__main__':

    img = mpimg.imread("EvV4-uOWYAQOM1x.jpg")
    noisy = Noise.uniform(img)
    # noisy = Noise.gaussian(img)
    # noisy = Noise.salt_pepper(img)
    # filtered = Filter.average(noisy, kernel_size=5)
    # Filter.gaussian(img)
    Kernel.sobel(kernel_size=5, plot=True)
    # f, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 6))
    # ax[0].imshow(noisy)
    # ax[0].set_title("Noisy Image")
    # ax[1].set_title("Filtered Image")
    # ax[1].imshow(filtered)
    # plt.show()
