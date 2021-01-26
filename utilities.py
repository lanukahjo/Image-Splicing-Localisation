import numpy as np
import math

# Get Hellinger Distance between two numpy ndarrays x and y
def getHellingerDistance(x, y):
    hellinger_distance = 1/np.sqrt(2) * np.sqrt(np.sum(np.square(np.sqrt(x) - np.sqrt(y))))
    return hellinger_distance

# Get euclidean distance between two numpy ndarrays x and y
def getEuclideanDistance(x, y):
    euclidean_distance = math.sqrt(np.sum(np.square(x-y)))
    return euclidean_distance;

#Get Minkowski distance of order p between two numpy ndarrays x and y
def getMinkowskiDistance(x, y, p):
    minkowski_distance = (np.sum((x-y)**p))**(1/p);
    return minkowski_distance;

#Get the normalised form of matrix as exponential distribution
def softmax(matrix):
    mu = np.mean(matrix)
    sigma = np.std(matrix)
    return 1/(sigma * np.sqrt(np.pi * 2)) * np.exp(-0.5 * np.square((matrix-mu)/sigma))