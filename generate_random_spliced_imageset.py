#This script creates random corresponding spliced images from a given set of authetic images.
#The spliced region is strip (either vertical or horizontal) located at a random position
#The width of the spliced region varies between 20 and 34

import os
from skimage import io
from random import seed
from random import randint
import csv

#This file stores the spliced to region to determine the metric values (TP,FP etc)
spliced_region_file = open(os.getcwd() + '/Dataset/spliced_area.csv','w') 

#We are using an input of 180 Authentic images to create their corresponding spliced image
#The files names are 1.bmp, 2.bmp, etc
for i in range(1,181):

    PATH_TO_AUTHENTIC_IMG = os.getcwd() + '/Dataset/Authentic/' +  str(i) + '.bmp'
    authentic_img = io.imread(PATH_TO_AUTHENTIC_IMG);

    img_height = authentic_img.shape[0]
    img_width = authentic_img.shape[1]

    #The orientation of the spliced region is determined randomly
    is_horizontal_splicing = randint(1,100) > 50

    #The width of the spliced region is determined randomly
    splice_strip_width = randint(20,35)

    #This variable defines the initial row or column in the authentic image which need to be cut
    splice_strip_begin = randint(0, 
                                    (img_width - splice_strip_width) if (is_horizontal_splicing == False) else (img_width - splice_strip_width)
                                )

    #This variable defines the initial row or column in the spliced image where the cut portion would be pasted.
    #For this we ensure this value is at a distance from splice_strip_begin such that spliced of strip of width
    #splice_strip_width can be accomodated
    splice_strip_end = splice_strip_begin
    while( abs(splice_strip_end - splice_strip_begin) <= splice_strip_width):
        splice_strip_end = randint(0, 
                                    (img_width - splice_strip_width) if (is_horizontal_splicing == False) else (img_width - splice_strip_width)
                                )

    #here the splicing takes place based on the value of randomly derived values above 
    spliced_img = authentic_img
    if (is_horizontal_splicing == False):
        spliced_img[0:img_height, splice_strip_end:(splice_strip_end + splice_strip_width)] = authentic_img[0:img_height, splice_strip_begin:(splice_strip_begin + splice_strip_width)]
    else:
        spliced_img[splice_strip_end : splice_strip_end + splice_strip_width,0:img_width] = authentic_img[splice_strip_begin : splice_strip_begin + splice_strip_width,0:img_width]


    #These four varibles refer to 4 lines which act as a bounding box for spliced region. They are stored in a csv file
    if (is_horizontal_splicing == False):
        spliced_row_begin = 0
        spliced_row_end = img_height-1
        spliced_col_begin = splice_strip_end
        spliced_col_end = (splice_strip_end + splice_strip_width) - 1
    else:
        spliced_row_begin = splice_strip_end
        spliced_row_end = splice_strip_end + splice_strip_width - 1
        spliced_col_begin = 0
        spliced_col_end = img_width-1

    
    spliced_region_file.write(str(i) + ',' +
                              str(spliced_row_begin) + ',' + 
                              str(spliced_row_end) + ',' + 
                              str(spliced_col_begin) + ',' + 
                              str(spliced_col_end) + '\n')

    #The spliced image is saved with convention <Original_Filename>_S.bmp
    pos1 = PATH_TO_AUTHENTIC_IMG.rindex("/")
    pos2 = PATH_TO_AUTHENTIC_IMG.rindex(".")
    base_file_name = PATH_TO_AUTHENTIC_IMG[pos1:pos2]
    io.imsave(os.getcwd() + '/Dataset/Spliced/' + base_file_name + '_S.bmp',spliced_img)