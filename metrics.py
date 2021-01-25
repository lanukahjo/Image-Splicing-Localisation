#this method returns the metrics true_positive, true_negative, false_positive, false_negative
def getMetric(output_matrix, spliced_region_data, img_number):
    height = output_matrix.shape[0]
    width = output_matrix.shape[1]

    row_begin = int(spliced_region_data[img_number-1][1])
    row_end = int(spliced_region_data[img_number-1][2])
    col_begin = int(spliced_region_data[img_number-1][3])
    col_end = int(spliced_region_data[img_number-1][4])

    tp = 0
    tn = 0
    fp = 0
    fn = 0

    for i in range(0,height):
        for j in range(0,width):
            if (output_matrix[i,j] == -1):
                if (i > row_begin and i < row_end) and (j > col_begin and j < col_end):
                    tp=tp+1
                else:
                    fp=fp+1
            else:
                if (i > row_begin and i < row_end) and (j > col_begin and j < col_end):
                    fn=fn+1
                else:
                    tn=tn+1
    
    return (tp,tn,fp,fn)

