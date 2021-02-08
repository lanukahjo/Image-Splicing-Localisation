#this method returns the metrics true_positive, true_negative, false_positive, false_negative
#spliced_region_data contains the spliced region of all images in the dataset
def getMetric(output_matrix, spliced_region_data, img_number):

    #Defines the dimension of input matrix
    height = output_matrix.shape[0] 
    width = output_matrix.shape[1]

    #the bounding box which define the actual spliced area
    row_begin = int(spliced_region_data[img_number-1][1])
    row_end = int(spliced_region_data[img_number-1][2])
    col_begin = int(spliced_region_data[img_number-1][3])
    col_end = int(spliced_region_data[img_number-1][4])


    tp = 0 #true positive
    tn = 0 #true negative
    fp = 0 #false positive
    fn = 0 #false negative

    #if a pixel is marked then it is positive else negative
    for i in range(0,height):
        for j in range(0,width):
            if (output_matrix[i,j] == 300):
                if (i >= row_begin and i <= row_end) and (j >= col_begin and j <= col_end):
                    tp=tp+1
                else:
                    fp=fp+1
            else:
                if (i >= row_begin and i <= row_end) and (j >= col_begin and j <= col_end):
                    fn=fn+1
                else:
                    tn=tn+1
    
    return (tp,tn,fp,fn)

