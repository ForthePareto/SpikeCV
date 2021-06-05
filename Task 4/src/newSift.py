import numpy as np
import cv2 as cv
from harrisOperator import find_key_points, harris
import math
import matplotlib.pyplot as plt
from matplotlib.patches import ConnectionPatch


def valid(i, j, n, m):
    return (i >= 0 and i < n and j >= 0 and j < m)


def get_gradient(frame, i, j):
    di = int(frame[i + 1, j] - frame[i - 1, j])
    dj = int(frame[i, i + 1] - frame[i, j - 1])

    magnitude = np.sqrt(di ** 2 + dj ** 2)
    theta = np.degrees(np.arctan2([di], [dj]))[0]

    if np.isnan(theta):
        theta = 90

    while theta < 0:
        theta += 360

    while theta > 360:
        theta -= 360

    if theta == 360:
        theta -= 1

    return magnitude, int(theta)


def orientation(frame, key_points):
    BINS_NUMBER = 36
    BIN_WIDTH = int(360 / BINS_NUMBER)

    KERNAL_SIZE = (16, 16)
    HALF_KERNAL_SIZE = int(KERNAL_SIZE[0] / 2)

    SIGMA = 1
    MEAN = 0

    gaussian_kernal = np.random.normal(MEAN, SIGMA, KERNAL_SIZE)

    histogram = np.zeros(BINS_NUMBER, dtype=int)
    new_key_points = []

    for p in key_points:

        x = p[0]
        y = p[1]

        for i in range(-HALF_KERNAL_SIZE, HALF_KERNAL_SIZE):
            for j in range(-HALF_KERNAL_SIZE, HALF_KERNAL_SIZE):
                wx = x + i
                wy = y + j

                maganitude, theta = get_gradient(frame, wx, wy)

                maganitude *= gaussian_kernal[i +
                                              HALF_KERNAL_SIZE, j + HALF_KERNAL_SIZE]

                _bin = int(theta / BIN_WIDTH)

                histogram[_bin] += maganitude

        max_bin = (np.argmax(histogram) + 1) * BIN_WIDTH
        new_key_points.append([x, y, max_bin])

    return new_key_points


def local_descriptors(frame, key_points):
    new_key_points = []

    BINS_NUMBER = 8

    BIN_WIDTH = int(360 / BINS_NUMBER)

    KERNAL_SIZE = (16, 16)
    HALF_KERNAL_SIZE = int(KERNAL_SIZE[0] / 2)

    SIGMA = 1
    MEAN = 0
    guasian_kernal = np.random.normal(MEAN, SIGMA, KERNAL_SIZE)

    for p in key_points:
        x = p[0]
        y = p[1]
        oriantation = p[2]

        window = frame[x - HALF_KERNAL_SIZE:x + HALF_KERNAL_SIZE,
                       y - HALF_KERNAL_SIZE:y + HALF_KERNAL_SIZE]

        window_gradients = np.zeros(KERNAL_SIZE)
        window_thetas = np.zeros(KERNAL_SIZE)

        for i in range(-HALF_KERNAL_SIZE, HALF_KERNAL_SIZE):
            for j in range(-HALF_KERNAL_SIZE, HALF_KERNAL_SIZE):
                wx = x + i
                wy = y + j

                magnitude, theta = get_gradient(frame, wx, wy)

                magnitude *= guasian_kernal[i +
                                            HALF_KERNAL_SIZE, j + HALF_KERNAL_SIZE]

                theta = np.abs(theta - oriantation)
                window_gradients[i + HALF_KERNAL_SIZE,
                                 j + HALF_KERNAL_SIZE] = magnitude
                window_thetas[i + HALF_KERNAL_SIZE,
                              j + HALF_KERNAL_SIZE] = theta

        window_sub_regions = []
        window_sub_gradients = []
        window_sub_thetas = []
        for i in range(0, 16, 4):
            for j in range(0, 16, 4):
                window_sub_regions.append(window[i: i + 4, j: j + 4])
                window_sub_gradients.append(
                    window_gradients[i: i + 4, j: j + 4])
                window_sub_thetas.append(window_thetas[i: i + 4, j: j + 4])

        descriptor = []

        for region_idx in range(16):
            hist = [0]*BINS_NUMBER
            for i in range(4):
                for j in range(4):
                    theta_p = window_sub_thetas[region_idx][i, j]
                    magnitude_p = window_sub_gradients[region_idx][i, j]
                    if theta_p >= 360:
                        theta_p -= 360
                    bin = int(theta_p/BIN_WIDTH)
                    hist[bin] += magnitude_p
            descriptor += hist

        descriptor_sum = sum(descriptor)
        if descriptor_sum > 0:
            for d in range(128):
                descriptor[d] /= descriptor_sum
                if descriptor[d] > .2:
                    descriptor[d] = .2

        descriptor_sum = sum(descriptor)
        if descriptor_sum > 0:
            for d in range(128):
                descriptor[d] /= descriptor_sum

        new_key_points.append(
            [x, y, oriantation, np.asarray(descriptor)])

    return new_key_points


def normalized_match(des1, des2, kp1, kp2):
    sort_list = []
    matches = [[] for i in range(2)]
    for idx, ele2 in enumerate(des2):
        points_dis = []
        for ele1 in des1:
            nnc = np.mean(np.multiply(
                (ele1[3]-np.mean(ele1[3])), (ele2[3]-np.mean(ele2[3]))))/(np.std(ele1[3])*np.std(ele2[3]))
            points_dis.append(nnc)
        min_value = max(points_dis)
        index = points_dis.index(min_value)
        sort_list.append((kp1[index], kp2[idx], min_value))
    sorted_list = sorted(sort_list, key=lambda x: x[2])
    for element in sorted_list:
        matches[0].append(element[0])
        matches[1].append(element[1])
    return matches


def main():
    filename = 'cat.jpg'
    frame1 = cv.imread(filename)
    frame1 = cv.cvtColor(frame1, cv.COLOR_BGR2RGB)
    grey1 = cv.cvtColor(frame1, cv.COLOR_RGB2GRAY)
    key_points1 = find_key_points(grey1)
    new_key_points = orientation(grey1, key_points1)
    new_key_points = local_descriptors(grey1, new_key_points)
    result1 = np.array(new_key_points)

    frame2 = cv.imread("cat22.jpg")

    rows, cols, a = frame2.shape

    # M = cv.getRotationMatrix2D((cols/2, rows/2), 90, 1)
    # frame2 = cv.warpAffine(frame2, M, (cols, rows))
    frame2 = cv.cvtColor(frame2, cv.COLOR_BGR2RGB)
    grey2 = cv.cvtColor(frame2, cv.COLOR_RGB2GRAY)

    key_points2 = find_key_points(grey2)
    new_key_points2 = orientation(grey2, key_points2)
    new_key_points2 = local_descriptors(grey2, new_key_points2)
    result2 = np.array(new_key_points2)

    matches = normalized_match(
        result1, result2, key_points1, key_points2)

    fig = plt.figure(figsize=(10, 5))
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)

    ax1.imshow(frame1)
    ax2.imshow(frame2)

    colors = ["red", "blue", "green", "black",
              "orange", "white", "cyan", "magenta"]

    for i in range(0, 50):
        con = ConnectionPatch(xyA=(matches[0][i][0], matches[0][i][1]), xyB=(matches[1][i][0], matches[1][i][1]), coordsA="data",
                              axesA=ax1, axesB=ax2, color=colors[i % 8])
        ax2.add_artist(con)
    plt.show()

    img = cv.imread(filename)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


if __name__ == "__main__":
    main()
