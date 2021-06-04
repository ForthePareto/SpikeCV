import numpy as np
from scipy import signal as sig
from scipy import ndimage as ndi
import matplotlib.pyplot as plt
import cv2 as cv2


def gradient_x(grayImg):
    # Sobel operator kernels.
    kernel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    return sig.convolve2d(grayImg, kernel_x, mode='same')


def gradient_y(grayImg):
    kernel_y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
    return sig.convolve2d(grayImg, kernel_y, mode='same')


def harris(grayImg):
    Ix = gradient_x(grayImg)
    Iy = gradient_y(grayImg)

    Ixx = ndi.gaussian_filter(Ix**2, sigma=1)
    Ixy = ndi.gaussian_filter(Iy*Ix, sigma=1)
    Iyy = ndi.gaussian_filter(Iy**2, sigma=1)

    k = 0.05

    # determinant
    detA = Ixx * Iyy - Ixy ** 2
    # trace
    traceA = Ixx + Iyy

    R = detA - k * traceA ** 2

    dola = np.zeros((grayImg.shape[0], grayImg.shape[1]))
    dola[R > 0.1*R.max()] = True
    x = np.where(dola == True)
    features = np.asarray(x).T.tolist()
    return features


def readImage(filename):
    img = cv2.imread(filename, 0)
    if img is None:
        print('Invalid image:' + filename)
        return None
    else:
        print('Image successfully read...')
        return img


def find_key_points(frame, window_size=5, k=0.04, thresh=100000):
    dy, dx = np.gradient(frame)
    Ixx = dx**2
    Ixy = dy*dx
    Iyy = dy**2
    height = frame.shape[0]
    width = frame.shape[1]

    cornerList = []
    offset = int(window_size/2)

    maxR = 0

    for y in range(20, height-20):
        for x in range(20, width-20):
            windowIxx = Ixx[y-offset:y+offset+1, x-offset:x+offset+1]
            windowIxy = Ixy[y-offset:y+offset+1, x-offset:x+offset+1]
            windowIyy = Iyy[y-offset:y+offset+1, x-offset:x+offset+1]
            Sxx = windowIxx.sum()
            Sxy = windowIxy.sum()
            Syy = windowIyy.sum()

            det = (Sxx * Syy) - (Sxy**2)
            trace = Sxx + Syy
            r = det - k*(trace**2)

            maxR = max(r, maxR)
            cornerList.append([x, y, r])

    key_points = []
    for p in cornerList:
        if p[2] > 0.1 * maxR:
            key_points.append(p)

    return key_points


def main():
    window_size = 5
    k = 0.04
    thresh = 10000
    img_name = 'cat.jpg'

    img = readImage(img_name)
    f, ax = plt.subplots(1, 2)

    ax[0].imshow(img)
    if img is not None:
        if len(img.shape) == 3:
            img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        if len(img.shape) == 4:
            img = cv2.cvtColor(img, cv2.COLOR_RGBA2GRAY)
        print("Shape: " + str(img.shape))
        print("Size: " + str(img.size))
        print("Type: " + str(img.dtype))
        print("Printing Original Image...")
        print(img)
        finalImg, cornerList = find_key_points(
            img, int(window_size), float(k), int(thresh))

        ax[1].imshow(finalImg)
        plt.show()
        if finalImg is not None:
            cv2.imwrite("finalimage.png", finalImg)

        cornerList.sort(key=operator.itemgetter(2))
        outfile = open('corners.txt', 'w')
        for i in range(100):
            outfile.write(str(
                cornerList[i][0]) + ' ' + str(cornerList[i][1]) + ' ' + str(cornerList[i][2]) + '\n')
        outfile.close()


if __name__ == "__main__":
    main()
