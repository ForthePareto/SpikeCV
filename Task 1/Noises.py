import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt


class Noise:

    @staticmethod
    def uniform(image: np.ndarray, amount=0.2) -> np.ndarray:
        noise = amount*np.random.uniform(0, 255, size=image.shape)
        output = (noise + image).astype(np.uint8)
        return output

    @staticmethod
    def gaussian(image: np.ndarray, mean=0, variance=0.1,amount=0.2) -> np.ndarray:
        sigma = variance**0.5
        gauss = np.random.normal(mean, sigma, (image.shape))*np.max(image)*amount
        noisy = image + gauss
        return noisy

    @staticmethod
    def salt_pepper(image: np.ndarray, salt_ratio=0.5, amount=0.01) -> np.ndarray:
        output = np.copy(image)
        # Salt mode
        num_salt = np.ceil(amount * image.size * salt_ratio)
        coords = [np.random.randint(0, i - 1, int(num_salt))
                  for i in image.shape]
        output[tuple(coords)] = 255

        # Pepper mode
        num_pepper = np.ceil(amount * image.size * (1. - salt_ratio))
        coords = [np.random.randint(0, i - 1, int(num_pepper))
                  for i in image.shape]
        output[tuple(coords)] = 0
        return output


if __name__ == '__main__':
    img = mpimg.imread("emHn_NO-.jpg",)
    # noisy = Noise.uniform(img)
    # noisy = Noise.gaussian(img)
    noisy = Noise.salt_pepper(img)
    plt.imshow(noisy, cmap="gray")
    plt.show()
