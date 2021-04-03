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

        avg_kernel = Kernel.average(kernel_size=kernel_size)
        output = signal.convolve2d(img, avg_kernel)
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
        output = signal.convolve2d(img, kernel)
        print(output.shape)
        return output

    @staticmethod
    def median(img: Sequence[int], kernel_size=3) -> np.ndarray:  # RGB
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
        data_final = np.zeros((data.shape))
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
    def sobel(img: np.ndarray, direction="x", kernel_size=3, magnitude=True) -> np.ndarray:
        """sobel [summary]

        Args:
            img (np.ndarray): [description]
            direction (str, optional): [description]. Defaults to "x".
            kernel_size (int, optional): [description]. Defaults to 3.

        Returns:
            np.ndarray: [description]
        """
        if direction.lower() == "xy":
            return Filter.sobel(img, direction="x", kernel_size=kernel_size) + Filter.sobel(img, direction="y", kernel_size=kernel_size)
        else:
            sobel_kernel = Kernel.sobel(
                direction=direction, kernel_size=kernel_size)
            output = signal.convolve2d(img, sobel_kernel)

        if magnitude:
            return np.abs(output)
        else:
            return output

    @staticmethod
    def prewitt(img: np.ndarray, direction="x", kernel_size=3, magnitude=True) -> np.ndarray:
        """prewitt [summary]

        Args:
            img (np.ndarray): [description]
            direction (str, optional): [description]. Defaults to "x".

        Returns:
            np.ndarray: [description]
        """
        if direction.lower() == "xy":
            return Filter.prewitt(img, direction="x", kernel_size=kernel_size) + Filter.prewitt(img, direction="y", kernel_size=kernel_size)
        else:
            prewitt_kernel = Kernel.prewitt(
                direction=direction, kernel_size=kernel_size)
            output = signal.convolve2d(img, prewitt_kernel)
        if magnitude:
            return np.abs(output)
        else:
            return output

    # https://towardsdatascience.com/canny-edge-detection-step-by-step-in-python-computer-vision-b49c3a2d8123
    @staticmethod
    def canny(img: np.ndarray, min_value=230, max_value=250) -> np.ndarray:
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
        assert img.ndim == 2  # canny works only with grayscale images
        smoothed = Filter.gaussian(img)
        grad_x = Filter.sobel(smoothed, direction="x",
                              kernel_size=3, magnitude=True)
        grad_y = Filter.sobel(smoothed, direction="y",
                              kernel_size=3, magnitude=True)
        Grad_xy = np.hypot(grad_x, grad_y)
        Grad_xy = Grad_xy / Grad_xy.max() * 255
        theta = np.arctan2(grad_y, grad_x)

        suppressed = Filter._non_max_suppression(Grad_xy, theta)

        thresholded, weak_pixel_val, strong_pixel_val = Filter._threshold(
            suppressed, min_edge_thresh=min_value, max_edge_thresh=max_value)

        hysteresis_output = Filter._hysteresis(
            thresholded, weak=weak_pixel_val, strong=strong_pixel_val)

        return hysteresis_output

    # https://www.youtube.com/watch?v=9mLeVn8xzMw
    @staticmethod
    def low_pass_frequency(img: np.ndarray, cut_off_x=40, cut_off_y=40) -> np.ndarray:
        """low_pass_frequency [https://plotly.com/python/v3/fft-filters/]

        Args:
            img (np.ndarray): [description]
            cutoff (int): [description]

        Returns:
            np.ndarray: [description]
        """

        ncols, nrows = img.shape[0], img.shape[1]
        print(img.shape)
        gmask = Kernel.gaussian_frequency_mask(
            shape=(ncols, nrows), mode='low_pass', cut_off_x=cut_off_x, cut_off_y=cut_off_y, plot=False)
        ftimage = np.fft.fft2(img)

        ftimage = np.fft.fftshift(ftimage)
        ftimagep = ftimage * gmask.T  # product instead of convolution

        # take the inverse transform and return blurred image
        imagep = np.fft.ifft2(ftimagep)
        return imagep

    # https://www.youtube.com/watch?v=9mLeVn8xzMw
    @staticmethod
    def high_pass_frequency(img: np.ndarray, cut_off_x=50, cut_off_y=50) -> np.ndarray:
        """high_pass_frequency [https://plotly.com/python/v3/fft-filters/]

        Args:
            img (np.ndarray): [description]
            cutoff (int): [description]

        Returns:
            np.ndarray: [description]
        """
        ncols, nrows = img.shape[0], img.shape[1]
        gmask = Kernel.gaussian_frequency_mask(
            shape=(ncols, nrows), mode='high_pass', cut_off_x=cut_off_x, cut_off_y=cut_off_y, plot=False)
        ftimage = np.fft.fft2(img)

        ftimage = np.fft.fftshift(ftimage)
        ftimagep = ftimage * gmask.T  # product instead of convolution

        # take the inverse transform and return blurred image
        imagep = np.fft.ifft2(ftimagep)
        return imagep

    @classmethod
    def _non_max_suppression(cls, img, grad_direction):
        Rows, Columns = img.shape[0], img.shape[1]
        Z = np.zeros((Rows, Columns), dtype=np.int32)
        angle = grad_direction * 180. / np.pi
        angle[angle < 0] += 180

        for row in range(1, Rows-1):
            for column in range(1, Columns-1):
                try:
                    first_neighbor = 255
                    second_neighbor = 255

                    # angle 0
                    if (0 <= angle[row, column] < 22.5) or (157.5 <= angle[row, column] <= 180):
                        first_neighbor = img[row, column+1]
                        second_neighbor = img[row, column-1]
                    # angle 45
                    elif (22.5 <= angle[row, column] < 67.5):
                        first_neighbor = img[row+1, column-1]
                        second_neighbor = img[row-1, column+1]
                    # angle 90
                    elif (67.5 <= angle[row, column] < 112.5):
                        first_neighbor = img[row+1, column]
                        second_neighbor = img[row-1, column]
                    # angle 135
                    elif (112.5 <= angle[row, column] < 157.5):
                        first_neighbor = img[row-1, column-1]
                        second_neighbor = img[row+1, column+1]

                    if (img[row, column] >= first_neighbor) and (img[row, column] >= second_neighbor):
                        Z[row, column] = img[row, column]
                    else:
                        Z[row, column] = 0

                except IndexError as e:
                    pass

        return Z

    @classmethod
    def _threshold(cls, img, lowThresholdRatio=0.05, highThresholdRatio=0.09, min_edge_thresh=40, max_edge_thresh=70):

        highThreshold = np.max(img) * highThresholdRatio
        lowThreshold = highThreshold * lowThresholdRatio
        # highThreshold = max_edge_thresh
        # lowThreshold = min_edge_thresh

        M, N = img.shape[0], img.shape[1]
        res = np.zeros((M, N), dtype=np.int32)

        weak_pixel_val = np.int32(25)
        strong_pixel_val = np.int32(255)

        strong_i, strong_j = np.where(img >= highThreshold)
        weak_i, weak_j = np.where(
            (img <= highThreshold) & (img >= lowThreshold))

        res[strong_i, strong_j] = strong_pixel_val
        res[weak_i, weak_j] = weak_pixel_val

        return (res, weak_pixel_val, strong_pixel_val)

    @ classmethod
    def _hysteresis(cls, image, weak=25, strong=255):
        img = np.copy(image)
        rows, columns = img.shape[0], img.shape[1]
        for row in range(1, rows-1):
            for col in range(1, columns-1):
                if (img[row, col] == weak):
                    try:
                        if ((img[row+1, col-1] == strong) or (img[row+1, col] == strong) or (img[row+1, col+1] == strong)
                            or (img[row, col-1] == strong) or (img[row, col+1] == strong)
                                or (img[row-1, col-1] == strong) or (img[row-1, col] == strong) or (img[row-1, col+1] == strong)):

                            img[row, col] = strong
                        else:
                            img[row, col] = 0
                    except IndexError as e:
                        pass
        return img


class Kernel:
    @staticmethod
    def average(kernel_size=3, plot=False):
        avg_kernel = np.ones((kernel_size, kernel_size))
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
            Kernel._plot(gauss_kernel, mode="3d", x=x, y=y)
        return gauss_kernel

    @staticmethod
    def sobel(direction="x", kernel_size=3, plot=False):
        if direction.lower() not in ["x", "y"]:
            raise ValueError("Undefined direction, use x or y")
        a = np.ones((kernel_size, 1))
        a[(kernel_size//2), :] = 2
        b = np.arange(kernel_size//2, -(kernel_size//2+1), -
                      1).reshape(1, kernel_size)
        sobel_kernel = a@b if direction.lower() == "x" else (a@b).T
        if plot:
            Kernel._plot(sobel_kernel)
        return sobel_kernel

    @staticmethod
    def prewitt(kernel_size=3, direction="x", plot=False):
        if direction.lower() not in ["x", "y"]:
            raise ValueError("Undefined direction, use x or y")
        a = np.ones((kernel_size, 1))
        b = np.arange(kernel_size//2, -(kernel_size//2+1), -
                      1).reshape(1, kernel_size)
        prewitt_kernel = a@b if direction.lower() == "x" else (a@b).T
        if plot:
            Kernel._plot(prewitt_kernel)
        return prewitt_kernel

    @staticmethod
    def gaussian_frequency_mask(shape: tuple, mode="low_pass", cut_off_x=40, cut_off_y=40, plot=False):
        if mode.lower() not in ["low_pass", "high_pass"]:
            raise ValueError(
                "please provide a valid mode either low_pass or high_pass")
        ncols, nrows = shape[0], shape[1]
        centerY, centerX = nrows//2, ncols//2
        x = np.linspace(0, ncols, ncols)  # horizontal
        y = np.linspace(0, nrows, nrows)  # vertical
        X, Y = np.meshgrid(x, y)
        if mode.lower() == "low_pass":
            gmask = np.exp(-(((X-centerX)/cut_off_x) **
                             2 + ((Y-centerY)/cut_off_y)**2))
        else:  # high_pass
            gmask = 1 - np.exp(-(((X-centerX)/cut_off_x) **
                                 2 + ((Y-centerY)/cut_off_y)**2))
        if plot:
            Kernel._plot(gmask, mode="3d", x=X, y=Y)
        return gmask

    def circular_frequency_mask(shape: tuple, mode="low_pass", cut_off_x=40, cut_off_y=40, plot=False):
        ncols, nrows = shape[0], shape[1]
        centerY, centerX = nrows//2, ncols//2
        x = np.linspace(0, ncols, ncols)  # horizontal
        y = np.linspace(0, nrows, nrows)  # vertical
        X, Y = np.meshgrid(x, y)
        mask = np.zeros((shape))
        area = cut_off_x**2+cut_off_y**2
        if mode.lower() == "low_pass":
            mask_area = ((X-centerX))**2 + ((Y-centerY))**2   <=  area        
        else:  # high_pass
            mask_area = ((X-centerX))**2 + ((Y-centerY))**2 >= area
        if plot:
            Kernel._plot(mask, mode="3d", x=X, y=Y)
        mask[mask_area.T] = 1
        return mask.T

    @classmethod
    def _plot(cls, kernel, mode="2d", **kwargs):
        if mode.lower() == "2d":
            plt.imshow(kernel, cmap=plt.get_cmap(
                'jet'), interpolation='nearest')
            plt.colorbar()
        elif mode.lower() == "3d":
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            ax.plot_surface(kwargs["x"], kwargs["y"], kernel, cmap=plt.get_cmap(
                'coolwarm'))
        plt.show()


if __name__ == '__main__':

    img = mpimg.imread("small_img.png")
    print(img.ndim)
    def gray(rgb): return np.dot(rgb[..., :3], [0.299, 0.587, 0.114])
    img = gray(img)
    # noisy = Noise.uniform(img)
    # noisy = Noise.gaussian(img)
    # noisy = Noise.salt_pepper(img)
    # smooth = Filter.gaussian(img, kernel_size=5)
    filtered = Filter.high_pass_frequency(img,cut_off_x=35,cut_off_y=35)
    # mask = filtered[:, :] > 150
    # filtered = np.zeros((filtered.shape))
    # filtered[mask] = 255
    # Filter.gaussian(img)
    # Kernel.sobel(kernel_size=5, direction='g', plot=True)

    f, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 6))
    ax[0].imshow(np.abs(filtered), cmap="gray")
    ax[0].set_title("Noisy Image")
    # ax[1].set_title("Filtered Image")
    # ax[1].imshow(filtered,cmap="gray")
    plt.axis("off")

    plt.show()
