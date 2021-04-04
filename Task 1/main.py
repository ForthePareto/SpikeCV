import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


def normalize(frame: np.ndarray, newMin: float, newMax: float):
    newFrame = np.copy(frame)
    mini = frame.min()
    maxi = frame.max()
    newFrame = (newFrame - mini) * ((newMax - newMin) / (maxi - mini)) + newMin

    return newFrame.astype(np.uint8)


def rgb2gray(frame):
    greyFrame = np.copy(frame)
    return np.dot(frame[..., :3], [0.2989, 0.5870, 0.1140]).astype(np.uint8)


def distrubutionCurve(frame):
    fig, ax = plt.subplots(2)
    histogram, bin_edges = np.histogram(
        frame[..., 0], bins=256, range=(frame[..., 0].min(), frame[..., 0].max()))
    ax[0].plot(bin_edges[0:-1], histogram, label='R', color='red')
    histogram, bin_edges = np.histogram(
        frame[..., 1], bins=256, range=(frame[..., 1].min(), frame[..., 1].max()))
    ax[0].plot(bin_edges[0:-1], histogram, label='G', color='green')
    histogram, bin_edges = np.histogram(
        frame[..., 2], bins=256, range=(frame[..., 2].min(), frame[..., 2].max()))
    ax[0].plot(bin_edges[0:-1], histogram, label='B', color='blue')
    ax[0].legend()
    ax[1].hist(frame.flatten(), bins=frame.max() - frame.min() + 1)
    plt.show()
    pass


def main():
    frame = cv.imread('test2.jpg')
    distrubutionCurve(frame)
    # # print('original frame: ', frame)
    # normalizedFrame = normalize(frame, 0, 255)
    # # print('normalized frame: ', type(normalizedFrame[0][0][0]))
    # cv.imshow('image', frame)
    # greyFrame = rgb2gray(frame)
    # cv.imshow('normalizedImage', greyFrame)
    # # cv.waitKey(0)
    # frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # histogram, bin_edges = np.histogram(
    #     frame, bins=256, range=(frame.min(), frame.max()))
    # # print(histogram)
    # plt.figure()

    # plt.title("Grayscale Histogram")
    # plt.xlabel("grayscale value")
    # plt.ylabel("pixels")
    # # plt.xlim([frame.min(), frame.max()])  # <- named arguments do not work here

    # # plt.plot(bin_edges[0:-1], histogram)  # <- or here
    # plt.hist(frame.flatten(), bins=256)

    # plt.show()
    pass


if __name__ == '__main__':
    main()
