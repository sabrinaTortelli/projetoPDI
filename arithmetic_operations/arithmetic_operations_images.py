import numpy as np


class ArithmeticOperationsImages(object):

    def __init__(self, image1, image2):
        self.image1 = image1
        self.image2 = image2
        self.rows = self.image1.shape[0]
        self.cols = self.image1.shape[1]
        self.shape = self.image1.shape
        self.image_result = None

    def __verify_shapes(self):
        if self.image1.shape[0] == self.image2.shape[0] and self.image1.shape[1] == self.image2.shape[1]:
            return True
        else:
            return False

    def add_operation(self):
        equal_size = self.__verify_shapes()
        if equal_size:
            if len(self.shape) == 2:
                self.image_result = np.zeros((self.rows, self.cols), np.uint8)
                return self.__add_2_shapes()
            else:
                print("Shape 3")
                self.image_result = np.zeros((self.rows, self.cols, 3), np.uint8)
                return self.__add_3_shapes()

    def __add_3_shapes(self):
        for row in range(self.rows):
            for col in range(self.cols):

                r_img1 = self.image1.item(row, col, 0)
                g_img1 = self.image1.item(row, col, 1)
                b_img1 = self.image1.item(row, col, 2)

                r_img2 = self.image2.item(row, col, 0)
                g_img2 = self.image2.item(row, col, 1)
                b_img2 = self.image2.item(row, col, 2)

                r_result = abs(r_img1 - r_img2)
                g_result = abs(g_img1 - g_img2)
                b_result = abs(b_img1 - b_img2)

                self.image_result.itemset((row, col, 0), r_result)
                self.image_result.itemset((row, col, 1), g_result)
                self.image_result.itemset((row, col, 2), b_result)
        return self.image_result

    def __add_2_shapes(self):
        for row in range(self.rows):
            for col in range(self.cols):
                pixel1 = self.image1.item(row, col)
                pixel2 = self.image2.item(row, col)
                result = abs(pixel1 + pixel2)
                self.image_result.itemset((row, col), result)
        return self.image_result
