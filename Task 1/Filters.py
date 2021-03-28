import numpy as np


class Filter:
    def __init__(self, img):
        pass

    @staticmethod
    def average(img: np.ndarray, kernel=3) -> np.ndarray:
        """average [summary]

        Args:
            img (np.ndarray): [description]
            kernel (int, optional): [description]. Defaults to 3.

        Returns:
            np.ndarray: [description]
        """

        pass

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
    def canny(img: np.ndarray, direction="x") -> np.ndarray:
        """canny: The Process of Canny edge detection algorithm can be broken down to 5 different steps:

                    Apply Gaussian filter to smooth the image in order to remove the noise
                    Find the intensity gradients of the image
                    Apply gradient magnitude thresholding or lower bound cut-off suppression to get rid of spurious response to edge detection
                    Apply double threshold to determine potential edges
                    Track edge by hysteresis: Finalize the detection of edges by suppressing all the other edges that are weak and not connected to strong edges.

        Args:
            img (np.ndarray): [description]
            direction (str, optional): [description]. Defaults to "x".

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
