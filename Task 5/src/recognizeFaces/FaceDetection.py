
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
# from .. import Filters
from ..Filters import gray
import cv2
import sys


def detect_faces(img, scaleFactor=1.1, minNeighbors=5, minSize=(25, 25), cascPath="haarcascade_frontalface_default.xml"):
    gray_img = gray(img).astype(np.uint8)
    output = np.copy(img).astype(np.uint8)
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + cascPath)
    faces = faceCascade.detectMultiScale(
        gray_img,
        scaleFactor=scaleFactor,
        minNeighbors=minNeighbors,
        minSize=minSize,
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # print("Found {0} faces!".format(len(faces)))

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(output, (x, y), (x+w, y+h), (0, 255, 0), 2)
    return output


if __name__ == '__main__':
    img = mpimg.imread("src/testImgs/zmlk.jpg")

    f, ax = plt.subplots(nrows=1, ncols=1, figsize=(10, 6))
    faces = detect_faces(img)
    ax.imshow(faces, cmap="gray")
    plt.axis("off")
    plt.show()
