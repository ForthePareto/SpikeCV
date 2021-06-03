import os
import sys
from itertools import product

import cv2 as cv
import matplotlib.cm as cm
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import filters
from src.Filters import Filter as filt

alpha = 100
beta = 200
_W_LINE = 250
_W_EDGE = 30
_MIN_DISTANCE = 10
_NUM_NEIGHBORS = 9

class greedySnake:
    @staticmethod
    def gray(rgb):
        if not (rgb.ndim == 3):
            raise ValueError("input must be 3-dimensional")
        return np.dot(rgb[..., :3], [0.299, 0.587, 0.114])

    @staticmethod
    def _display(image, snaxels=None):
        """
        Display a grayscale image with pylab, and draw the contour if there is any.
        """
        plt.clf()
        if snaxels is not None:
            for s in snaxels:
                plt.plot(s[0],s[1],'g.',markersize=10.0)
        
        plt.imshow(image, cmap=cm.Greys_r)
        plt.pause(0.01)
        plt.draw()
        
        return

    @staticmethod
    def normalize(array, newMin, newMax):
        minArr=array.min()
        maxArr=array.max()
        return ((array-minArr)/(maxArr-minArr))*(newMax-newMin)+newMin

    @staticmethod
    def _gradientImage(image):
        """
        Obtain a gradient image (in both x and y directions)
        """
        gradx = filt.sobel(image,direction="x",kernel_size=5,magnitude=True) 
        #cv.Sobel(image,cv.CV_64F,1,0,ksize=5)
        grady = filt.sobel(image,direction="x",kernel_size=5,magnitude=True)
        #cv.Sobel(image,cv.CV_64F,0,1,ksize=5)
        gradient = np.hypot(gradx, grady)
        gradient = greedySnake.normalize(gradient,0,1)

        return gradient 

    @staticmethod
    def _inBounds(image, point):
        """
        Is the point within the bounds of the image?
        """
        return np.all(point < np.shape(image)) and np.all(point > 0)

    @staticmethod
    def _externalEnergy(image, smooth_image, point):
        """
        The external energy of the point, a combination of line and edge 
        """
        pixel = 255 * image[point[1]][point[0]]
        smooth_pixel = 255 * smooth_image[point[1]][point[0]]
        external_energy = (_W_LINE * pixel) - (_W_EDGE * (smooth_pixel**2))
        return external_energy

    @staticmethod
    def _energy(image, smooth_image, current_point, next_point, previous_point=None):
        """
        Total energy (internal and external).
        Internal energy measures the shape of the contour
        """
        d_squared = np.linalg.norm(next_point -current_point)**2
        
        if previous_point is None:
            e =  alpha * d_squared + greedySnake._externalEnergy(image, smooth_image, current_point)
            return e 
        else:
            deriv = np.sum((next_point - 2 * current_point + previous_point)**2)
            e = 0.5 * (alpha * d_squared + beta * deriv + greedySnake._externalEnergy(image, smooth_image, current_point))
            return e

    @staticmethod
    def _pointsOnCircle(center, radius, num_points=12):
        points = np.zeros((num_points, 2), dtype=np.int32)
        for i in range(num_points):
            theta = float(i)/num_points * (2 * np.pi)
            x = center[0] + radius * np.cos(theta)
            y = center[1] + radius * np.sin(theta)
            p = [x, y]
            points[i] = p
            
        return points

    @staticmethod
    def _iterateContour(image, smooth_image, snaxels, energy_matrix, position_matrix, neighbors):
        """
        Compute the minimum energy locations for all the snaxels in the contour
        """
        snaxels_added = len(snaxels)
        for curr_idx in range(snaxels_added - 1, 0, -1):
            energy_matrix[curr_idx][:][:] = float("inf")
            prev_idx = (curr_idx - 1) % snaxels_added
            next_idx = (curr_idx + 1) % snaxels_added
            
            for j, next_neighbor in enumerate(neighbors):
                next_node = snaxels[next_idx] + next_neighbor
                
                if not greedySnake._inBounds(image, next_node):
                    continue
                
                min_energy = float("inf")
                for k, curr_neighbor in enumerate(neighbors):
                    curr_node = snaxels[curr_idx] + curr_neighbor
                    distance = np.linalg.norm(next_node - curr_node)
                    
                    if not greedySnake._inBounds(image, curr_node) or (distance < _MIN_DISTANCE):
                        continue
                    
                    min_energy = float("inf")
                    for l, prev_neighbor in enumerate(neighbors):
                        prev_node = snaxels[prev_idx] + prev_neighbor
                            
                        if not greedySnake._inBounds(image, prev_node):
                            continue
                            
                        energy = energy_matrix[prev_idx][k][l] + greedySnake._energy(image, smooth_image, curr_node, next_node, prev_node)
                        
                        if energy < min_energy:
                            min_energy = energy
                            min_position_k = k
                            min_position_l = l
                    
                    energy_matrix[curr_idx][j][k] = min_energy
                    position_matrix[curr_idx][j][k][0] = min_position_k
                    position_matrix[curr_idx][j][k][1] = min_position_l
        
        min_final_energy = float("inf")
        min_final_position_j = 0
        min_final_position_k = 0

        for j in range(_NUM_NEIGHBORS):
            for k in range(_NUM_NEIGHBORS):
                if energy_matrix[snaxels_added - 2][j][k] < min_final_energy:
                    min_final_energy = energy_matrix[snaxels_added - 2][j][k]
                    min_final_position_j = j
                    min_final_position_k = k

        pos_j = min_final_position_j
        pos_k = min_final_position_k
        
        for i in range(snaxels_added - 1, -1, -1):
            snaxels[i] = snaxels[i] + neighbors[pos_j]
            if i > 0:
                pos_j = position_matrix[i - 1][pos_j][pos_k][0]
                pos_k = position_matrix[i - 1][pos_j][pos_k][1]
                
        return min_final_energy


