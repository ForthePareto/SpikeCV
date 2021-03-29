import numpy as np
from scipy import signal
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from Noises import Noise


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
    def median(img: np.ndarray, kernel=3) -> np.ndarray:
        """median [summary]

        Args:
            img (np.ndarray): [description]
            kernel (int, optional): [description]. Defaults to 3.

        Returns:
            np.ndarray: [description]
        """
        pass

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

    img = mpimg.imread("emHn_NO-.jpg",)
    # noisy = Noise.uniform(img)
    # noisy = Noise.gaussian(img)
    noisy = Noise.salt_pepper(img)
    filtered = Filter.average(noisy, kernel=5)
    f, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 6))
    ax[0].imshow(noisy, cmap="gray")
    ax[0].set_title("Noisy Image")
    ax[1].set_title("Filtered Image")
    ax[1].imshow(filtered, cmap="gray")
    plt.show()
