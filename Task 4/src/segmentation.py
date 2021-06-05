import numpy as np
import cv2 as cv

from src.kmeans import KMeans
from src.agglomerative import segment_frame
from src.meanshift import mean_shift
from src.rGrowing import RGWrapper

class Segmenation:
    """
    Segmentation algorthms APIs: kmeans, agglomerative, regiongrowing and mean shift segmentation
    """

    @staticmethod
    def kmeans(img: np.ndarray, k: int) -> np.ndarray:
        """
        unsupervised kmeans segmenation
        """
        # convert to RGB
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

        # reshape image to points
        pixel_values = img.reshape((-1, 3))
        pixel_values = np.float32(pixel_values)

        max_iter=10

        # run clusters_num-means algorithm
        model = KMeans(K=k, max_iters=max_iter)
        y_pred = model.predict(pixel_values)

        centers = np.uint8(model.cent())
        y_pred = y_pred.astype(int)

        # flatten labels and get segmented image
        labels = y_pred.flatten()
        segmented_image = centers[labels.flatten()]
        segmented_image = segmented_image.reshape(img.shape)

        return segmented_image

    @staticmethod
    def agglomerative(img: np.ndarray, n_clusters=5) -> np.ndarray:
        """
        agglomerative segmenation
        """
        return segment_frame(img, n_clusters)

    @staticmethod
    def region_growing(img: np.ndarray,threshold=15) -> np.ndarray:
        """
        region_growing segmenation
        """
        return RGWrapper(img, threshold)

    @staticmethod
    def mean_shift(img: np.ndarray, **params: dict) -> np.ndarray:
        """
        mean shift segmenation
        """
        return mean_shift(img)
