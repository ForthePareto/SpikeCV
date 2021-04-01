import numpy as np
from scipy import signal
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from Noises import Noise
from collections import OrderedDict
from typing import Sequence


class Filter:

    @staticmethod
    def average(img: np.ndarray, kernel=3) -> np.ndarray:
        """average [summary]

        Args:
            img (np.ndarray): [description]
            kernel (int, optional): [description]. Defaults to 3.

        Returns:
            np.ndarray: [description]
        """

        avg_kernel = np.ones((kernel, kernel))
        avg_kernel = (1/avg_kernel.size) * avg_kernel
        output = signal.convolve(img, avg_kernel)
        return output

    @staticmethod
    def gaussian(img: np.ndarray, kernel=3) -> np.ndarray:
        """gaussian [summary]

        Args:
            img (np.ndarray): [description]
            kernel (int, optional): [description]. Defaults to 3.

        Returns:
            np.ndarray: [description]
        """
        pass

    @staticmethod
    def _is_convolution_in_bounds(img_shape: list, kernel_edges: np.array):
        rows = list(range(img_shape[0]))
        cols = list(range(img_shape[1]))
        if (kernel_edges[0] not in cols) or (kernel_edges[1] not in cols) or (kernel_edges[2] not in rows) or (kernel_edges[3] not in rows):
            return False
        else:
            return True

    @staticmethod
    def median(img: Sequence[int], kernel=3) -> np.ndarray:
        """median [summary]

        Args:
            img (np.ndarray): [description]
            kernel (int, optional): [description]. Defaults to 3.

        Returns:
            np.ndarray: [description]
        """

        temp = []
        filter_size = kernel
        indexer = filter_size // 2
        data = img.copy()
        data_final = []
        data_final = np.zeros((len(data),len(data[0])))
        for i in range(len(data)):

            for j in range(len(data[0])):

                for z in range(filter_size):
                    if i + z - indexer < 0 or i + z - indexer > len(data) - 1:
                        for c in range(filter_size):
                            temp.append(0)
                    else:
                        if j + z - indexer < 0 or j + indexer > len(data[0]) - 1:
                            temp.append(0)
                        else:
                            for k in range(filter_size):
                                temp.append(data[i + z - indexer][j + k - indexer])

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
                
        #         if (Filter._is_convolution_in_bounds(img.shape, kernel_edges) == False) :
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
    def sobel(img: np.ndarray, direction="x") -> np.ndarray:
        """sobel [summary]

        Args:
            img (np.ndarray): [description]
            direction (str, optional): [description]. Defaults to "x".

        Returns:
            np.ndarray: [description]
        """
        pass

    @staticmethod
    def Prewitt(img: np.ndarray, direction="x") -> np.ndarray:
        """Prewitt [summary]

        Args:
            img (np.ndarray): [description]
            direction (str, optional): [description]. Defaults to "x".

        Returns:
            np.ndarray: [description]
        """
        pass

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


if __name__ == '__main__':

    img = mpimg.imread("emHn_NO-.jpg")
    # noisy = Noise.uniform(img)
    # noisy = Noise.gaussian(img)
    noisy = Noise.salt_pepper(img)
    print()
    filtered = Filter.median(noisy, kernel=5)
    f, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 6))
    ax[0].imshow(noisy, cmap="gray")
    ax[0].set_title("Noisy Image")
    ax[1].set_title("Filtered Image")
    ax[1].imshow(filtered, cmap="gray")
    plt.show()
