import os
import glob
from sklearn import preprocessing
import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
from ..Filters import gray


def plot_image(images, titles, h, w, n_row, n_col):
    plt.figure(figsize=(2.2*n_col, 2.2*n_row))
    plt.subplots_adjust(bottom=0, left=.01, right=.99, top=.90, hspace=.20)
    for i in range(n_row*n_col):
        plt.subplot(n_row, n_col, i+1)
        plt.imshow(images[i].reshape((h, w)), cmap=plt.cm.gray)
        plt.title(titles[i])
        plt.xticks(())
        plt.yticks(())
    plt.show()


class FaceRecognition():

    def __init__(self, dataSetPath: str):
        self.dataSetPath = dataSetPath
        self.N_IMGS = 0
        self.class_name = None
        self.countImgs()
        self.loadDataSet()
        self.meanImgs()
        self.eigenVectors()
        self.eigenFaces()

    def countImgs(self):
        # Loop through all the images in the folder
        for images in glob.glob(self.dataSetPath + '/**', recursive=True):
            if images[-3:] == 'pgm' or images[-3:] == 'jpg':
                self.N_IMGS += 1
        print(self.N_IMGS)

    def loadDataSet(self):
        # height of the image is 112 and width is 92
        self.shape = (112, 92)
        # Creating 0 matrix with 112 rows and 92 columns of zeros for 400 images
        self.all_img = np.zeros(
            (self.N_IMGS, self.shape[0], self.shape[1]), dtype='float64')
        self.names = list()
        i = 0
        # Loop through folders
        for folder in glob.glob(self.dataSetPath + '/*'):
            for _ in range(10):
                self.names.append(folder[-3:].replace('/', ''))
            # Loop through images
            for image in glob.glob(folder + '/*'):
                read_image = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
                # cv2.resize resizes an image into (# column x # height)
                resized_image = cv2.resize(
                    read_image, (self.shape[1], self.shape[0]))
                self.all_img[i] = np.array(resized_image)
                i += 1

        # plot_image(self.all_img,self.names,112,92,2,10)

    def meanImgs(self):
        # Creating a matrix of n^2 x m
        A = np.resize(self.all_img, (self.N_IMGS, self.shape[0]*self.shape[1]))
        self.mean_vector = np.sum(A, axis=0, dtype='float64')/self.N_IMGS
        # Calculating mean for all the 400 images
        self.mean_matrix = np.tile(self.mean_vector, (self.N_IMGS, 1))
        # Matrix A - the mean value of all the images
        self.A_tilde = A - self.mean_matrix

        # plt.imshow(np.resize(self.mean_vector,(self.shape[0],self.shape[1])),cmap='gray')#display the mean image vector
        # plt.title('Mean Image')
        # plt.show()
        # plot_image(self.A_tilde,self.names,112,92,2,10)

    def eigenVectors(self):
        # Creating a m x m symmetric matrix
        L = (self.A_tilde.dot(self.A_tilde.T))/self.N_IMGS
        # Calculating the eigenvalues and eigenvectors
        eigenvalues, eigenvectors = np.linalg.eig(L)
        # sort eigenvalues in descending order
        idx = eigenvalues.argsort()[::-1]
        eigenvalues = eigenvalues[idx]
        # Sort the eigenvectors according to the highest eigenvalues
        eigenvectors = eigenvectors[:, idx]
        # print(eigenvectors)

        # perform linear combination with Matrix A_tilde
        self.eigenvector_C = self.A_tilde.T @ eigenvectors
        # Each column is an eigenvector
        # print(self.eigenvector_C.shape)

    def eigenFaces(self):
        # Normalize the vector
        self.eigenfaces = preprocessing.normalize(self.eigenvector_C.T)
        # List of images
        eigenface_labels = [x for x in range(self.eigenfaces.shape[0])]
        # Display image using eigenvectors for each image
        # plot_image(self.eigenfaces,eigenface_labels,112,92,2,10)

    def classifyImg(self, input: np.ndarray):
        # test_img = cv2.imread(inputPath, cv2.IMREAD_GRAYSCALE)
        # input = np.resize(input,(self.N_IMGS,self.shape[0]*self.shape[1]))
        # Subtract test image with the mean value
        mean_sub_testimg = np.reshape(
            input, (input.shape[0]*input.shape[1])) - self.mean_vector

        # 350 eigenvectors is chosen
        self.q = 350
        # Projecting the test image into the face space
        self.E = self.eigenfaces[:self.q].dot(mean_sub_testimg)
        # print(self.E.shape)
        # Reconstruct the test image using eigenvectors
        reconstruction = self.eigenfaces[:self.q].T.dot(self.E)
        reconstruction.shape

        return(self.recognizeFace())

    def recognizeFace(self) -> np.ndarray:
        # Classify the image belongs to which class
        thres_2 = 3000
        # to keep track of the smallest value
        smallest_value = None
        # to keep track of the class that produces the smallest value
        index = None
        # Loop through all the image vectors
        for z in range(self.N_IMGS):
            # Calculate and represent the vectors of the image in the dataset
            E_z = self.eigenfaces[:self.q].dot(self.A_tilde[z])
            diff = self.E - E_z
            epsilon_z = math.sqrt(diff.dot(diff))
            if smallest_value == None:
                smallest_value = epsilon_z
                index = z
            if smallest_value > epsilon_z:
                smallest_value = epsilon_z
                index = z
        if smallest_value < thres_2:
            self.class_name =  self.names[index]
            print("input image belongs to class: ", self.names[index])
            # display the first-img in the matching database-dir
            # plt.imshow(self.all_img[index],cmap='gray')
            # plt.title('Busted')
            # plt.show()
            return(self.all_img[index])
        else:
            print("unknown Face")
            test_img = cv2.imread("../../imgs/404.png", cv2.IMREAD_GRAYSCALE)
            return(test_img)


def FaceRecognitionWrapper(input: np.ndarray, dataSetPath="src/recognizeFaces/archive/"):
    FaceRecognizer = FaceRecognition(dataSetPath)
    gray_img = gray(input)
    print(input.shape)
    class_name = FaceRecognizer.class_name
    try:
        result = FaceRecognizer.classifyImg(gray_img)
    except:
        print("not found")
        result = cv2.imread('../testImgs/404.png', cv2.IMREAD_GRAYSCALE)

    plt.imshow(result, cmap='gray')
    plt.title('Busted')
    plt.show()
    return result,class_name


if __name__ == '__main__':

    test = cv2.imread('src/testImgs/export1.png', cv2.IMREAD_GRAYSCALE)
    FaceRecognitionWrapper(test)
