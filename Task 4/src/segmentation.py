import numpy as np


class Segmenation:

    @staticmethod
    def kmeans(img: np.ndarray, k: int) -> np.ndarray:
        """
        unsupervised kmeans segmenation
        """
        pass

    @staticmethod
    def region_growing(img: np.ndarray, **params: dict) -> np.ndarray:
        """
        region_growing segmenation
        """
        pass

    @staticmethod
    def agglomerative(img: np.ndarray, **params: dict) -> np.ndarray:
        """
        agglomerative segmenation
        """
        pass

    @staticmethod
    def mean_shift(img: np.ndarray, **params: dict) -> np.ndarray:
        """
        agglomerative segmenation
        """
        pass
