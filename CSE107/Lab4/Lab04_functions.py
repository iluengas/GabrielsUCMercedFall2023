import numpy as np

def spatial_filter( simple_image_pixels, impulse_filter_pixels):
    m, n = simple_image_pixels.shape

    filtered_image = np.zeros(shape=(m, n))

    for row in range(m-1):
        for column in range(n-1):
            temp = simple_image_pixels[row-1][column-1] * impulse_filter_pixels[0][0] +\
                    simple_image_pixels[row-1][column] * impulse_filter_pixels[0][1] +\
                    simple_image_pixels[row-1][column+1] * impulse_filter_pixels[0][2] +\
                    simple_image_pixels[row][column-1] * impulse_filter_pixels[1][0] +\
                    simple_image_pixels[row][column] * impulse_filter_pixels[1][1] +\
                    simple_image_pixels[row][column+1] * impulse_filter_pixels[1][2] +\
                    simple_image_pixels[row+1][column-1] * impulse_filter_pixels[2][0] +\
                    simple_image_pixels[row+1][column] * impulse_filter_pixels[2][1] +\
                    simple_image_pixels[row+1][column+1] * impulse_filter_pixels[2][2]
            
            print ('CHECK VAL'+ str(simple_image_pixels[row+1][column+1]))
            
            filtered_image[row][column] = temp

    return filtered_image