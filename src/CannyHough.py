import numpy as np
import math
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from src.Filters import Filter, rgba2rgb,gray


class BoundaryDetector:

    @staticmethod
    def canny_superImpose(img: np.ndarray, min_value=40, max_value=220, edge_color="blue") -> np.ndarray:
        """
         detect edges and superimpose them on the original image
        """
        if img.shape[-1] == 4:
            img = rgba2rgb(img)
        edges = Filter.canny(img, min_value=min_value, max_value=max_value)
        super_imposed = BoundaryDetector._superimpose(
            img, edges, color=edge_color)

        return super_imposed

    @staticmethod
    def circles_superImpose(img, pixel_step=1, minRadius=5, maxRadius=50, canny_low=40, canny_high=150, edge_color="red") -> np.ndarray:
        """
        detect cricles and superimpose them on the original image
        """
        edges = Filter.canny(img, min_value=canny_low,
                             max_value=canny_high)
        lines_binary = BoundaryDetector.hough_circles(
            edges,  pixel_step=pixel_step, minRadius=minRadius, maxRadius=maxRadius)
        super_imposed = BoundaryDetector._superimpose(
            img, lines_binary, color=edge_color)

        return super_imposed

    @staticmethod
    def lines_superImpose(img: np.ndarray, histress_low=40, histress_high=220, angle_step=1, value_threshold=26, min_line_votes=90, edge_color="red") -> np.ndarray:
        """
         detect lines and superimpose them on the original image
        """
        edges = Filter.canny(img, min_value=histress_low,
                             max_value=histress_high)
        lines_binary = BoundaryDetector.hough_line(
            edges, angle_step=1, value_threshold=26, min_line_votes=90)
        super_imposed = BoundaryDetector._superimpose(
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
    def hough_circles(img, pixel_step=1, n_circles=10, minRadius=5, maxRadius=50, min_circle_votes=120, lowEdges_pixel_value=26):
        height, width = img.shape[0], img.shape[1]
        a = np.arange(0, width, 1)
        b = np.arange(0, height, 1)
        diagonal = int(round(math.sqrt(height ** 2 + width ** 2)/2))
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
        highly_voted_circles = np.max(
            accumulator, axis=2)
        highly_voted_circles = np.sort(
            highly_voted_circles, axis=None, kind="mergesort")[::-1][:n_circles]

        # satisfying_lines =( accumulator >= min_circle_votes)
        satisfying_lines = (accumulator >= highly_voted_circles[-1]) & (
            accumulator <= highly_voted_circles[0])

        circles = np.argwhere(satisfying_lines)
        print("number of detected circels:  ", circles.shape[0])
        # try:
        #     print(circles[0:3])
        # except:
        # pass
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

    @classmethod
    def _superimpose(cls, img: np.ndarray, binary: np.ndarray, color="blue") -> np.ndarray:

        colors = {"red": (255, 0, 0),
                  "green": (0, 255, 0),
                  "blue": (0, 0, 255),
                  "yellow": (255, 255, 0)}

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

if __name__ == "__main__":

    img1 = mpimg.imread("imgs/2coins.png")

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
