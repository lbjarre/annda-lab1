#!/usr/bin/env python3

"""datageneration.py

Module containing methods for generating datasets.
"""

import numpy as np
import numpy.random as rnd
import matplotlib.pyplot as plt

def lin_sep(class_labels, size):
    """Generates two classes of linearly separable data"""

    class1_mean = [1, 1]
    class1_cov = np.diag([0.2, 0.1])
    class1_labels = class_labels[0] * np.ones(size)

    class1_xy = rnd.multivariate_normal(class1_mean, class1_cov, size).T
    class1_xy_labels = np.vstack((class1_xy, class1_labels))

    class2_mean = [-1, -1]
    class2_cov = np.diag([0.1, 0.2])
    class2_labels = class_labels[1] * np.ones(size)

    class2_xy = rnd.multivariate_normal(class2_mean, class2_cov, size).T
    class2_xy_labels = np.vstack((class2_xy, class2_labels))

    xy_labels = np.hstack((class1_xy_labels, class2_xy_labels))
    rnd.shuffle(xy_labels.T)
    xy = xy_labels[0:2, :]
    labels = xy_labels[-1, :]

    return xy, labels

def non_lin_sep(class_labels, size, mean1, mean2):
    class1_cov = np.diag([1, 1])
    class1_labels = class_labels[0] * np.ones(size)

    class1_xy = rnd.multivariate_normal(mean1, class1_cov, size).T
    class1_xy_labels = np.vstack((class1_xy, class1_labels))

    class2_cov = np.diag([1,1])
    class2_labels = class_labels[1] * np.ones(size)

    class2_xy = rnd.multivariate_normal(mean2, class2_cov, size).T
    class2_xy_labels = np.vstack((class2_xy, class2_labels))

    xy_labels = np.hstack((class1_xy_labels, class2_xy_labels))
    rnd.shuffle(xy_labels.T)
    xy = xy_labels[0:2, :]
    labels = xy_labels[-1, :]

    return xy, labels

def sparse_data():

    data = -1 * np.ones((8, 8))
    for i in range(8):
        data[i, i] = 1
    return data

def mackey_glass(x0, length):

    beta = 0.2
    gamma = 0.1
    n = 10
    tau = 25

    x = np.zeros(length)
    x[0] = x0

    for i in range(1, tau+1):
        x[i] = (1 - gamma) * x[i-1]
    for i in range(tau+1, length):
        x[i] = (1 - gamma) * x[i-1] + (beta * x[i-tau])/(1 + x[i-tau]**n)

    return x

if __name__ == '__main__':

    label_color_map = {
        1: 'b',
        -1: 'r'
    }

    data, labels = lin_sep(list(label_color_map.keys()), 100)

    label_colors = list(map(lambda x: label_color_map.get(x), labels))

    plt.scatter(data[0, :], data[1, :], c=label_colors)
    plt.show()
