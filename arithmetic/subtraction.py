import cv2
import numpy as np
class Subtraction(object):
    def subtraction(img1, img2):
        image1 = img1.return_image_object()
        image2 = img2.return_image_object()
        rows = image1.shape[0]
        cols = image1.shape[1]
        shape_ = image1.shape

        image_diff = ''  # to return

        if (len(shape_) == 3):
            image_diff = np.zeros((rows, cols, 3), np.uint8)

            for row in range(0, rows):
                for col in range(0, cols):
                    r_img1 = image1.item(row, col, 0)
                    g_img1 = image1.item(row, col, 1)
                    b_img1 = image1.item(row, col, 2)

                    r_img2 = image2.item(row, col, 0)
                    g_img2 = image2.item(row, col, 1)
                    b_img2 = image2.item(row, col, 2)

                    r_result = abs(r_img1 - r_img2)
                    g_result = abs(g_img1 - g_img2)
                    b_result = abs(b_img1 - b_img2)

                    image_diff.itemset((row, col, 0), r_result)
                    image_diff.itemset((row, col, 1), g_result)
                    image_diff.itemset((row, col, 2), b_result)
        else:
            image_diff = np.zeros((rows, cols, 1), np.uint8)  # criação
            for row in range(0, rows):
                for col in range(0, cols):
                    pixel1 = image1.item(row, col)
                    pixel2 = image2.item(row, col)

                    result = abs(pixel1 - pixel2)

                    image_diff.itemset((row, col, 0), result)

        cv2.imshow('Subtraction', image_diff)
        cv2.waitKey(0)
        return image_diff