import numpy as np
import cv2
import random
import sys


def get_euclidean_distance(current_mean_arr, pixel):
    euclidean_dist = 0
    for i in range(5):
        euclidean_dist += (current_mean_arr[i] - pixel[i]) ** 2

    euclidean_dist = euclidean_dist ** 0.5

    return euclidean_dist


def get_below_threshold(current_mean_arr, feature_space, threshold):
    below_threshold_arr = []
    for i in range(len(feature_space)):
        # current_color_total = 0
        # new_color_total = 0
        euclidean_dist = get_euclidean_distance(
            current_mean_arr[0], feature_space[i])

        if euclidean_dist < threshold:
            below_threshold_arr.append(i)

    return below_threshold_arr


def get_feature_space(frame):
    row = frame.shape[0]
    col = frame.shape[1]
    feature_space = np.zeros((row * col, 5))
    arr = np.array((1, 3))
    cnt = 0

    for i in range(row):
        for j in range(col):
            arr = frame[i][j]

            for k in range(5):
                if (k >= 0) & (k <= 2):
                    feature_space[cnt][k] = arr[k]
                else:
                    if(k == 3):
                        feature_space[cnt][k] = i
                    else:
                        feature_space[cnt][k] = j
            cnt += 1

    return feature_space


def mean_shift(frame):
    row = frame.shape[0]
    col = frame.shape[1]

    num_of_pixels = row * col
    size = row, col, 3
    result_frame = np.zeros(size, dtype=np.uint8)

    iter = 1.0

    threshold = 30
    current_mean_random = True
    current_mean_arr = np.zeros((1, 5))
    below_threshold_arr = []

    feature_space = get_feature_space(frame)

    while len(feature_space) > 0:
        print(len(feature_space))

        if current_mean_random:
            current_mean = random.randint(0, len(feature_space) - 1)

            for i in range(5):
                current_mean_arr[0][i] = feature_space[current_mean][i]

        below_threshold_arr = get_below_threshold(
            current_mean_arr, feature_space, threshold)

        mean_R = 0
        mean_G = 0
        mean_B = 0
        mean_i = 0
        mean_j = 0
        current_mean = 0
        mean_col = 0

        for i in range(len(below_threshold_arr)):
            mean_R += feature_space[below_threshold_arr[i]][0]
            mean_G += feature_space[below_threshold_arr[i]][1]
            mean_B += feature_space[below_threshold_arr[i]][2]
            mean_i += feature_space[below_threshold_arr[i]][3]
            mean_j += feature_space[below_threshold_arr[i]][4]

        mean_R = mean_R / len(below_threshold_arr)
        mean_G = mean_G / len(below_threshold_arr)
        mean_B = mean_B / len(below_threshold_arr)
        mean_i = mean_i / len(below_threshold_arr)
        mean_j = mean_j / len(below_threshold_arr)

        mean_e_distance = ((mean_R - current_mean_arr[0][0])**2 + (mean_G - current_mean_arr[0][1])**2 + (
            mean_B - current_mean_arr[0][2])**2 + (mean_i - current_mean_arr[0][3])**2 + (mean_j - current_mean_arr[0][4])**2)
        mean_e_distance = mean_e_distance**0.5

        nearest_i = 0
        min_e_dist = 0
        cnt_threshold = 0

        if mean_e_distance < iter:
            new_arr = np.zeros((1, 3))
            new_arr[0][0] = mean_R
            new_arr[0][1] = mean_G
            new_arr[0][2] = mean_B

            for i in range(len(below_threshold_arr)):
                result_frame[int(feature_space[below_threshold_arr[i]][3])][int(
                    feature_space[below_threshold_arr[i]][4])] = new_arr
                feature_space[below_threshold_arr[i]][0] = -1

            current_mean_random = True
            new_feature_space = np.zeros((len(feature_space), 5))
            counter_i = 0

            for i in range(len(feature_space)):
                if feature_space[i][0] != -1:
                    new_feature_space[counter_i] = feature_space[i]
                    counter_i += 1

            feature_space = np.zeros((counter_i, 5))

            for i in range(counter_i):
                feature_space[i] = new_feature_space[i]

        else:
            current_mean_random = False

            current_mean_arr[0][0] = mean_R
            current_mean_arr[0][1] = mean_G
            current_mean_arr[0][2] = mean_B
            current_mean_arr[0][3] = mean_i
            current_mean_arr[0][4] = mean_j

    return result_frame


def main():
    frame = cv2.imread('cat.jpg')

    result_frame = mean_shift(frame)

    cv2.imshow('final', result_frame)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()
