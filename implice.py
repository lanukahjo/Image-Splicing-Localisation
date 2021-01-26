import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import os
import math
from skimage import data
from skimage import filters
from skimage import io
from skimage.feature import greycomatrix

from utilities import *

#The function reduces the image to 8 gray levels
#Assumption : 0-255 color levels grayscale image available
def reduce_gray_level(matrix):
    return (matrix/32).astype(int)

def localise_spliced_area(PATH_TO_AUTHENTIC_IMG,PATH_TO_SPLICED_IMG,THRESHOLD=0.2,BLOCK_SIZE = 4,STEP_SIZE = 2,MINKOWSKI_DISTANCE_ORDER = 4):
    authentic_img = io.imread(PATH_TO_AUTHENTIC_IMG);
    spliced_img = io.imread(PATH_TO_SPLICED_IMG); 

    output_img_euclidean_dist = spliced_img;
    output_img_hellinger_dist = spliced_img;
    output_img_minkowski_dist = spliced_img;

    authentic_img_grey_reduced = reduce_gray_level(authentic_img)
    spliced_img_grey_reduced = reduce_gray_level(spliced_img)

    img_height = authentic_img.shape[0]
    img_width = authentic_img.shape[1]

    # We shall store the different distances because we need to normalise the diatances too.

    #total number of blocks in a column
    dist_mat_height = (int)((img_height - BLOCK_SIZE)/STEP_SIZE + 1); 


    #total number of blocks in a row
    dist_mat_width = (int)((img_width - BLOCK_SIZE)/STEP_SIZE + 1); 


    #create empty arrays to store the different distances used

    euc_dist_mat = np.zeros((dist_mat_height, dist_mat_width), dtype = float) 
    hell_dist_mat = np.zeros((dist_mat_height, dist_mat_width), dtype = float) 
    minkowski_dist_mat = np.zeros((dist_mat_height, dist_mat_width), dtype = float) 

    # row and col are used to index into the distance matrices

    row = 0; 
    col = 0; 
    
    for i in range(BLOCK_SIZE - 1, img_height, STEP_SIZE):
        col = 0;
        
        for j in range(BLOCK_SIZE - 1, img_width, STEP_SIZE):

            #Index into the blocks
            authentic_block = authentic_img_grey_reduced[i + 1 - BLOCK_SIZE : i + 1,
                                                        j + 1 - BLOCK_SIZE : j + 1];                                          
            spliced_block = spliced_img_grey_reduced[i + 1 - BLOCK_SIZE : i + 1,
                                                    j + 1 - BLOCK_SIZE : j + 1]
            
            #Calculate the normalised GLCM for Authentic image
            glcm_matrix_auth = greycomatrix(authentic_block,
                                            distances = [1],
                                            angles = [0],
                                            levels = 8,
                                            normed = True);
            glcm_matrix_auth = glcm_matrix_auth[:,:,0,0];

            #Calculate the normalised GLCM for Spliced image
            glcm_matrix_spl = greycomatrix(spliced_block,
                                        distances = [1],
                                        angles = [0],
                                        levels = 8,
                                        normed = True);
            glcm_matrix_spl = glcm_matrix_spl[:,:,0,0]
        
            #glcm_matrix_auth = softmax(glcm_matrix_auth)
            #glcm_matrix_spl = softmax(glcm_matrix_spl)
            #Calculate different distances
            hellinger_distance = getHellingerDistance(glcm_matrix_auth, glcm_matrix_spl);
            euclidean_distance = getEuclideanDistance(glcm_matrix_auth, glcm_matrix_spl);
            minkowski_distance = getMinkowskiDistance(glcm_matrix_auth, glcm_matrix_spl,
                                                    MINKOWSKI_DISTANCE_ORDER);

            #Store the distance between blocks at (row,col) index in distance matrices
            hell_dist_mat[row,col] = hellinger_distance
            euc_dist_mat[row,col] = euclidean_distance
            minkowski_dist_mat[row,col] = minkowski_distance;

            col = col + 1
        row = row + 1

    #Normalise the distance matrices

    euc_dist_mat = euc_dist_mat / np.max(euc_dist_mat)
    hell_dist_mat = hell_dist_mat / np.max(hell_dist_mat)
    minkowski_dist_mat = minkowski_dist_mat / np.max(minkowski_dist_mat);



    #changing the datatype from default uint8 to allow marking the spliced region with value 300
    output_img_euclidean_dist = np.uint16(output_img_euclidean_dist)
    output_img_hellinger_dist = np.uint16(output_img_hellinger_dist)
    output_img_minkowski_dist = np.uint16(output_img_minkowski_dist)

    #The blocks for which the textural difference is greater than threshold is painted white

    for i in range(0, dist_mat_height):
        for j in range(0, dist_mat_width):
        
            if (euc_dist_mat[i,j] > THRESHOLD):
                output_img_euclidean_dist[i * STEP_SIZE : i * STEP_SIZE + BLOCK_SIZE, 
                                        j * STEP_SIZE : j * STEP_SIZE + BLOCK_SIZE] = 300 * np.ones((BLOCK_SIZE, BLOCK_SIZE))
            if (hell_dist_mat[i,j] > THRESHOLD):
                output_img_hellinger_dist[i * STEP_SIZE : i * STEP_SIZE + BLOCK_SIZE,
                                        j * STEP_SIZE : j * STEP_SIZE + BLOCK_SIZE] = 300 * np.ones((BLOCK_SIZE, BLOCK_SIZE))
            if (minkowski_dist_mat[i,j] > THRESHOLD):
                output_img_minkowski_dist[i * STEP_SIZE : i * STEP_SIZE + BLOCK_SIZE,
                                        j * STEP_SIZE : j * STEP_SIZE + BLOCK_SIZE] = 300*np.ones((BLOCK_SIZE, BLOCK_SIZE))
    
    return (output_img_euclidean_dist,output_img_hellinger_dist,output_img_minkowski_dist)

#paints the localised area with white pixels
def paint_in_white(matrix):
    height = matrix.shape[0]
    width = matrix.shape[1]

    for i in range(0,height):
        for j in range(0,width):
            if (matrix[i,j] == 300):
                matrix[i,j] = 255

    return matrix