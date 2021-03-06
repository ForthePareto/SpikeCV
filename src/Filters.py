import numpy as np
from scipy import signal
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from PIL import Image
import math


def rgba2rgb(rgba):
    return rgba[:, :, :-1]


def gray(rgb):
    if (rgb.ndim == 2):
        return rgb
    elif rgb.shape[-1] == 4:
        print("rgba image to gray")
        rgb = rgba2rgb(rgb)
        return np.dot(rgb[..., :3], [0.299, 0.587, 0.114])
    else:
        return np.dot(rgb[..., :3], [0.299, 0.587, 0.114])


class Filter:

    @staticmethod
    def average(img: np.ndarray, kernel_size=3) -> np.ndarray:
        """
        average [summary]

        Parameters
        ----------
        img : np.ndarray
            [description]
        kernel_size : int, optional
            [description], by default 3

        Returns
        -------
        np.ndarray
            [description]
        """

        avg_kernel = Kernel.average(kernel_size=kernel_size)
        output = signal.convolve2d(img, avg_kernel, mode="same")
        return output

    @staticmethod
    def gaussian(img: np.ndarray, kernel_size=3, std=1) -> np.ndarray:
        """
        gaussian [summary]

        Parameters
        ----------
        img : np.ndarray
            [description]
        kernel_size : int, optional
            [description], by default 3
        std : int, optional
            [description], by default 1

        Returns
        -------
        np.ndarray
            [description]
        """

        kernel = Kernel.gaussian(kernel_size=kernel_size, std=std)
        output = signal.convolve2d(img, kernel, mode="same")
        return output

    @staticmethod
    def median(img: np.ndarray, kernel_size=3) -> np.ndarray:
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

        for row in range(data.shape[0]):  # rows

            for column in range(data.shape[1]):  # columns

                for z in range(filter_size):
                    if row + z - indexer < 0 or row + z - indexer > len(data) - 1:
                        for c in range(filter_size):
                            temp.append(0)
                    else:
                        if column + z - indexer < 0 or column + indexer > len(data[0]) - 1:
                            temp.append(0)
                        else:
                            for k in range(filter_size):
                                temp.append(
                                    data[row + z - indexer][column + k - indexer])

                temp.sort()
                data_final[row][column] = temp[len(temp) // 2]
                temp = []
        return data_final

    @staticmethod
    def sobel(img: np.ndarray, direction="x", kernel_size=3, magnitude=True) -> np.ndarray:
        """
        sobel [summary: The Process of Canny edge detection algorithm can be broken down to 5 different steps:

                    Apply Gaussian filter to smooth the image in order to remove the noise
                    Find the intensity gradients of the image
                    Apply gradient magnitude thresholding or lower bound cut-off suppression to get rid of spurious response to edge detection
                    Apply double threshold to determine potential edges
                    Track edge by hysteresis: Finalize the detection of edges by suppressing all the other edges that are weak and not connected to strong edges.]

        Parameters
        ----------
        img : np.ndarray
            [description]
        direction : str, optional
            [description], by default "x"
        kernel_size : int, optional
            [description], by default 3
        magnitude : bool, optional
            [description], by default True

        Returns
        -------
        np.ndarray
            [description]
        """
        if direction.lower() == "xy":
            return Filter.sobel(img, direction="x", kernel_size=kernel_size) + Filter.sobel(img, direction="y", kernel_size=kernel_size)
        else:
            sobel_kernel = Kernel.sobel(
                direction=direction, kernel_size=kernel_size)
            output = signal.convolve2d(img, sobel_kernel, mode="same")

        if magnitude:
            return np.abs(output)
        else:
            return output

    @staticmethod
    def prewitt(img: np.ndarray, direction="x", kernel_size=3, magnitude=True) -> np.ndarray:
        """
        prewitt [summary]

        Parameters
        ----------
        img : np.ndarray
            [description]
        direction : str, optional
            [description], by default "x"
        kernel_size : int, optional
            [description], by default 3
        magnitude : bool, optional
            [description], by default True

        Returns
        -------
        np.ndarray
            [description]

        Raises
        ------
        ValueError
            [description]
        """
        if direction.lower() not in ["x", "y", "xy"]:
            raise ValueError("direction must be 'x' or 'y' or 'xy' ")
        if direction.lower() == "xy":
            return Filter.prewitt(img, direction="x", kernel_size=kernel_size) + Filter.prewitt(img, direction="y", kernel_size=kernel_size)
        else:
            prewitt_kernel = Kernel.prewitt(
                direction=direction, kernel_size=kernel_size)
            output = signal.convolve2d(img, prewitt_kernel, mode="same")
        if magnitude:
            return np.abs(output)
        else:
            return output

    # https://towardsdatascience.com/canny-edge-detection-step-by-step-in-python-computer-vision-b49c3a2d8123

    @staticmethod
    def canny(img: np.ndarray, min_value=100, max_value=200):
        """
        canny [summary]

        Parameters
        ----------
        img : np.ndarray
            [description]
        min_value : int, optional
            [description], by default 230
        max_value : int, optional
            [description], by default 250

        Returns
        -------
        np.ndarray
            [description]

        Raises
        ------
        ValueError
            [description]
        """
        if not (img.ndim == 2):
            img = gray(img)
        smoothed = Filter.gaussian(img, kernel_size=7)
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

    @classmethod
    def _superimpose(cls, img: np.ndarray, binary: np.ndarray, color="blue") -> np.ndarray:
        colors = {"red": (255, 0, 0),
                  "green": (0, 255, 0),
                  "blue": (0, 0, 255),
                  "yellow": (255, 255, 0)
                  }
        if color.lower() not in colors.keys():
            print("invalid edge color")
            color = "red"
        if img.shape[-1] == 4:
            img = rgba2rgb(img)
        super_imposed = np.copy(img)
        if img.ndim == 2:
            super_imposed[binary == 255] = 255
        elif (img.ndim == 3) and img.shape[-1] == 3:
            super_imposed[binary == 255] = colors.get(color.lower())

        else:
            print("undefined case")

        return super_imposed

    @staticmethod
    def canny_superImpose(img: np.ndarray, min_value=40, max_value=220, edge_color="blue") -> np.ndarray:
        """
        canny_superImpose [summary]

        Parameters
        ----------
        img : np.ndarray
            [description]
        min_value : int, optional
            [description], by default 40
        max_value : int, optional
            [description], by default 220
        edge_color : str, optional
            [description], by default "blues"

        Returns
        -------
        np.ndarray
            [description]
        """
        if img.shape[-1] == 4:
            img = rgba2rgb(img)
        edges = Filter.canny(img, min_value=min_value, max_value=max_value)
        super_imposed = Filter._superimpose(img, edges, color=edge_color)

        return super_imposed

    @staticmethod
    def lines_superImpose(img: np.ndarray, histress_low=40, histress_high=220, angle_step=1, value_threshold=26, min_line_votes=90, edge_color="red") -> np.ndarray:
        edges = Filter.canny(img, min_value=histress_low,
                             max_value=histress_high)
        lines_binary = Filter.hough_line(
            edges, angle_step=1, value_threshold=26, min_line_votes=90)
        super_imposed = Filter._superimpose(
            img, lines_binary, color=edge_color)

        return super_imposed

    @staticmethod
    def hough_line(img, angle_step=1, value_threshold=26, min_line_votes=90):
        width, height = img.shape[0], img.shape[1]
        thetas = np.deg2rad(np.arange(-90.0, 90.0, angle_step))
        diag_len = int(round(math.sqrt(width ** 2 + height ** 2)))
        rhos = np.linspace(-diag_len, diag_len, diag_len * 2)
        cos_t = np.cos(thetas)
        sin_t = np.sin(thetas)
        num_thetas = len(thetas)

        # Hough accumulator array of theta(rows) , rho(columns)
        accumulator = np.zeros((2 * diag_len, num_thetas), dtype=np.uint8)
        # (row, col) indexes to edges
        are_edges = img > value_threshold
        y_idxs, x_idxs = np.nonzero(are_edges)

        # Vote in the hough accumulator
        for i in range(len(x_idxs)):
            x = x_idxs[i]
            y = y_idxs[i]

            for t_idx in range(num_thetas):
                # Calculate rho. diag_len is added for a positive index
                rho = diag_len + \
                    int(round(x * cos_t[t_idx] + y * sin_t[t_idx]))
                accumulator[rho, t_idx] += 1

        satisfying_lines = accumulator >= min_line_votes
        x, y = np.meshgrid(thetas, rhos)
        lines = np.dstack((x, y))[satisfying_lines]
        if len(lines) == 0:
            print("max votes at lines accumulator: ", np.max(accumulator))
            raise ValueError(
                "No Lines found, try to decrease the min_line_votes_param")
        for rho, theta in lines:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a*rho
            y0 = b*rho
            x1 = int(x0 + 1000*(-b))
            y1 = int(y0 + 1000*(a))
            x2 = int(x0 - 1000*(-b))
            y2 = int(y0 - 1000*(a))
            import cv2
            lines_img = cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 4)
        return lines_img

    @staticmethod
    def hough_circles(img, pixel_step=1, minRadius=5, maxRadius=50, min_circle_votes=120, lowEdges_pixel_value=26):
        height, width = img.shape[0], img.shape[1]
        a = np.arange(0, width, 1)
        b = np.arange(0, height, 1)
        diagonal = int(round(math.sqrt(height ** 2 + width ** 2)/2))
        print(diagonal)
        r = np.arange(0, diagonal, pixel_step)
        # Hough accumulator array
        accumulator = np.zeros((len(a), len(b), len(r)), dtype=np.uint16)
        # (row, col) indexes to edges
        are_edges = img >= lowEdges_pixel_value
        y_idxs, x_idxs = np.nonzero(are_edges)
        print("edge pixels: ", len(y_idxs))
        # Vote in the hough accumulator
        for i in range(len(x_idxs)):
            x = x_idxs[i]
            y = y_idxs[i]
            for xi in range(len(a)):
                for yi in range(len(b)):
                    radius = int(((x-xi)**2 + (y-yi)**2)**0.5)
                    if minRadius <= radius <= maxRadius:
                        # print(xi, yi, radius)
                        try:
                            accumulator[xi, yi, radius] += 1
                        except:
                            pass

        # highly_voted_circles = np.sort(
        #     accumulator, axis=None, kind="mergesort")[::-1][:1]
        highly_voted_circles = np.max(
            accumulator, axis=2)
        highly_voted_circles = np.sort(
            highly_voted_circles, axis=None, kind="mergesort")[::-1][:5]

        # satisfying_lines =( accumulator >= min_circle_votes)
        satisfying_lines = (accumulator >= highly_voted_circles[-1]) & (
            accumulator <= highly_voted_circles[0])
        # x, y, radius = np.meshgrid(a, b, r)
        # circles = np.dstack((x, y, radius))[satisfying_lines]
        circles = np.argwhere(satisfying_lines)
        print("number of detected circels:  ", circles.shape)
        try:
            print(circles[0:3])
        except:
            pass
        if len(circles) == 0:
            print("max votes at circle accumulator: ", np.max(accumulator))
            raise ValueError(
                "No Lines found, try to decrease the min_circle_votes")
        img = np.zeros_like(img)
        for (x, y, r) in circles:
            # draw the circle in the output image
            import cv2
            circles_binary = cv2.circle(img, (x, y), r, 255, 1)
        return circles_binary

    @staticmethod
    def circles_superImpose(img, pixel_step=1, minRadius=5, maxRadius=50, canny_low=40, canny_high=150, edge_color="red") -> np.ndarray:
        edges = Filter.canny(img, min_value=canny_low,
                             max_value=canny_high)
        lines_binary = Filter.hough_circles(
            edges,  pixel_step=pixel_step, minRadius=minRadius, maxRadius=maxRadius)
        super_imposed = Filter._superimpose(
            img, lines_binary, color=edge_color)

        return super_imposed

    @staticmethod
    def low_pass_frequency(img: np.ndarray, cut_off_x=40, cut_off_y=40) -> np.ndarray:
        """
        low_pass_frequency [summary]

        Parameters
        ----------
        img : np.ndarray
            [description]
        cut_off_x : int, optional
            [description], by default 40
        cut_off_y : int, optional
            [description], by default 40

        Returns
        -------
        np.ndarray
            [description]
        """

        ncols, nrows = img.shape[0], img.shape[1]
        gmask = Kernel.gaussian_frequency_mask(
            shape=(ncols, nrows), mode='low_pass', cut_off_x=cut_off_x, cut_off_y=cut_off_y, plot=False)
        filtered_image = Filter._frequency_convolution(img, gmask)
        return filtered_image

    @classmethod
    def _frequency_convolution(cls, img: np.ndarray, filter: np.ndarray) -> np.ndarray:
        """
        _frequency_convolution [summary]

        Parameters
        ----------
        img : np.ndarray
            [description]
        filter : np.ndarray
            [description]

        Returns
        -------
        np.ndarray
            [description]
        """
        ftimage = np.fft.fft2(img)
        ftimage = np.fft.fftshift(ftimage)
        ftimagep = ftimage * filter.T  # product instead of convolution
        # take the inverse transform and return the absolute of the filtered image
        imagep = np.abs(np.fft.ifft2(ftimagep))

        return imagep

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
        filtered_image = Filter._frequency_convolution(img, gmask)
        return filtered_image

    @classmethod
    def _non_max_suppression(cls, img: np.ndarray, grad_direction: np.ndarray) -> np.ndarray:
        """
        _non_max_suppression [summary]

        Parameters
        ----------
        img : np.ndarray
            [description]
        grad_direction : np.ndarray
            [description]

        Returns
        -------
        np.ndarray
            [description]
        """
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
    def _threshold(cls, img: np.ndarray, lowThresholdRatio=0.05, highThresholdRatio=0.09, min_edge_thresh=100, max_edge_thresh=220) -> np.ndarray:
        """
        _threshold [summary]

        Parameters
        ----------
        img : np.ndarray
            [description]
        lowThresholdRatio : float, optional
            [description], by default 0.05
        highThresholdRatio : float, optional
            [description], by default 0.09
        min_edge_thresh : int, optional
            [description], by default 40
        max_edge_thresh : int, optional
            [description], by default 70

        Returns
        -------
        np.ndarray
            [description]
        """
        M, N = img.shape[0], img.shape[1]
        res = np.zeros((M, N), dtype=np.int32)

        weak_pixel_val = np.int32(25)
        strong_pixel_val = np.int32(255)

        strong_i, strong_j = np.where(img >= min_edge_thresh)
        weak_i, weak_j = np.where(
            (img <= min_edge_thresh) & (img >= max_edge_thresh))

        res[strong_i, strong_j] = strong_pixel_val
        res[weak_i, weak_j] = weak_pixel_val

        return (res, weak_pixel_val, strong_pixel_val)

    @classmethod
    def _hysteresis(cls, image: np.ndarray, weak=25, strong=255) -> np.ndarray:
        """
        _hysteresis [summary]

        Parameters
        ----------
        image : np.ndarray
            [description]
        weak : int, optional
            [description], by default 25
        strong : int, optional
            [description], by default 255

        Returns
        -------
        np.ndarray
            [description]
        """
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
    """
    Collection of methods that implements differnt spatial kernels and frequency domain Masks
    """

    @staticmethod
    def average(kernel_size=3, plot=False) -> np.ndarray:
        """
        average [summary]

        Parameters
        ----------
        kernel_size : int, optional
            [description], by default 3
        plot : bool, optional
            [description], by default False

        Returns
        -------
        np.ndarray
            [description]
        """
        avg_kernel = np.ones((kernel_size, kernel_size))
        avg_kernel = (1/avg_kernel.size) * avg_kernel
        if plot:
            Kernel._plot(avg_kernel)
        return avg_kernel

    @staticmethod
    def gaussian(kernel_size=3, std=1, plot=False) -> np.ndarray:
        """
        gaussian [summary]

        Parameters
        ----------
        kernel_size : int, optional
            [description], by default 3
        std : int, optional
            [description], by default 1
        plot : bool, optional
            [description], by default False

        Returns
        -------
        np.ndarray
            [description]
        """
        kernel_size = kernel_size//2
        x = np.arange(-kernel_size, kernel_size+1, 1)
        y = np.arange(-kernel_size, kernel_size+1, 1)
        x, y = np.meshgrid(x, y)
        # gauss_kernel = (1/(2*np.pi*std**2))*np.exp(-((x**2+y**2)/(2*std**2)))
        gauss_kernel = np.exp(-((x**2+y**2)/(2*std**2)))
        gauss_kernel = gauss_kernel/np.sum(gauss_kernel)
        if plot:
            Kernel._plot(gauss_kernel, mode="3d", x=x, y=y)
        return gauss_kernel

    @staticmethod
    def sobel(direction="x", kernel_size=3, plot=False) -> np.ndarray:
        """
        sobel [summary]

        Parameters
        ----------
        direction : str, optional
            [description], by default "x"
        kernel_size : int, optional
            [description], by default 3
        plot : bool, optional
            [description], by default False

        Returns
        -------
        np.ndarray
            [description]

        Raises
        ------
        ValueError
            [description]
        """
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
    def prewitt(kernel_size=3, direction="x", plot=False) -> np.ndarray:
        """
        prewitt [summary]

        Parameters
        ----------
        kernel_size : int, optional
            [description], by default 3
        direction : str, optional
            [description], by default "x"
        plot : bool, optional
            [description], by default False

        Returns
        -------
        np.ndarray
            [description]

        Raises
        ------
        ValueError
            [description]
        """
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
    def gaussian_frequency_mask(shape: tuple, mode="low_pass", cut_off_x=40, cut_off_y=40, plot=False) -> np.ndarray:
        """
        gaussian_frequency_mask [summary]

        Parameters
        ----------
        shape : tuple
            [description]
        mode : str, optional
            [description], by default "low_pass"
        cut_off_x : int, optional
            [description], by default 40
        cut_off_y : int, optional
            [description], by default 40
        plot : bool, optional
            [description], by default False

        Returns
        -------
        np.ndarray
            [description]

        Raises
        ------
        ValueError
            [description]
        """
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

    def circular_frequency_mask(shape: tuple, mode="low_pass", cut_off_x=40, cut_off_y=40, plot=False) -> np.ndarray:
        """
        circular_frequency_mask [summary]

        Parameters
        ----------
        shape : tuple
            [description]
        mode : str, optional
            [description], by default "low_pass"
        cut_off_x : int, optional
            [description], by default 40
        cut_off_y : int, optional
            [description], by default 40
        plot : bool, optional
            [description], by default False

        Returns
        -------
        np.ndarray
            [description]
        """
        ncols, nrows = shape[0], shape[1]
        centerY, centerX = nrows//2, ncols//2
        x = np.linspace(0, ncols, ncols)  # horizontal
        y = np.linspace(0, nrows, nrows)  # vertical
        X, Y = np.meshgrid(x, y)
        mask = np.zeros((shape))
        area = cut_off_x**2+cut_off_y**2
        if mode.lower() == "low_pass":
            mask_area = ((X-centerX))**2 + ((Y-centerY))**2 <= area
        else:  # high_pass
            mask_area = ((X-centerX))**2 + ((Y-centerY))**2 >= area
        if plot:
            Kernel._plot(mask, mode="3d", x=X, y=Y)
        mask[mask_area.T] = 1
        return mask.T

    @classmethod
    def _plot(cls, kernel: np.ndarray, mode="2d", **kwargs):
        """
        _plot [summary]

        Parameters
        ----------
        kernel : np.ndarray
            [description]
        mode : str, optional
            [description], by default "2d"
        """
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

    img1 = mpimg.imread("manyCoins.jpg")

    print(img1.ndim)
    img = gray(img1)
    print(img.shape)
    canny = Filter.canny(img, min_value=35, max_value=155)
    f, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 6))
    circles = Filter.circles_superImpose(img1)
    ax[0].imshow(img1, cmap="gray")
    ax[0].set_title("Original Image")
    ax[0].axis("off")
    ax[1].set_title("Hough Circles Superimposed Image")
    ax[1].imshow(circles, cmap="gray")
    plt.axis("off")

    plt.show()

    # print(circles)
