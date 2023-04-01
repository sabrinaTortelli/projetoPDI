import cv2
import numpy as np

def fit_value(values):
    matrix = [0, 0, 0]
    for p in range(len(values)):
        if values[p] < 0:
            matrix[p] = 0
        elif values[p] > 255:
            matrix[p] = 255
        else:
            matrix[p] = values[p]
    return matrix

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
        else:
            print("Deu erro. Imagens com tamanhos diferentes")

    def __add_3_shapes(self):
        for row in range(self.rows):
            for col in range(self.cols):

                r_img1 = self.image1.item(row, col, 0)
                g_img1 = self.image1.item(row, col, 1)
                b_img1 = self.image1.item(row, col, 2)

                r_img2 = self.image2.item(row, col, 0)
                g_img2 = self.image2.item(row, col, 1)
                b_img2 = self.image2.item(row, col, 2)

                r_result = abs(r_img1 + r_img2)
                g_result = abs(g_img1 + g_img2)
                b_result = abs(b_img1 + b_img2)

                self.image_result.itemset((row, col, 0), r_result)
                self.image_result.itemset((row, col, 1), g_result)
                self.image_result.itemset((row, col, 2), b_result)
        self.show_images_by_side("Adicao RGB")
        return self.image_result

    def __add_2_shapes(self):
        for row in range(self.rows):
            for col in range(self.cols):
                pixel1 = self.image1.item(row, col)
                pixel2 = self.image2.item(row, col)
                result = abs(pixel1 + pixel2)
                self.image_result.itemset((row, col), result)
        self.show_images_by_side("Adicao")
        return self.image_result

    def sub_operation(self):
        equal_size = self.__verify_shapes()
        if equal_size:
            if len(self.shape) == 2:
                self.image_result = np.zeros((self.rows, self.cols), np.uint8)
                return self.__sub_2_shapes()
            else:
                print("Shape 3")
                self.image_result = np.zeros((self.rows, self.cols, 3), np.uint8)
                return self.__sub_3_shapes()

    def __sub_3_shapes(self):
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

                values = fit_value([r_result, g_result, b_result])

                self.image_result.itemset((row, col, 0), values[0])
                self.image_result.itemset((row, col, 1), values[1])
                self.image_result.itemset((row, col, 2), values[2])
        self.show_images_by_side("Subtracao RGB")
        return self.image_result

    def __sub_2_shapes(self):
        for row in range(self.rows):
            for col in range(self.cols):
                pixel1 = self.image1.item(row, col)
                pixel2 = self.image2.item(row, col)
                result = abs(pixel1 - pixel2)
                self.image_result.itemset((row, col), result)
        self.show_images_by_side("Subtracao")
        return self.image_result

    def mult_operation(self):
        equal_size = self.__verify_shapes()
        if equal_size:
            if len(self.shape) == 2:
                self.image_result = np.zeros((self.rows, self.cols), np.uint8)
                return self.__mult_2_shapes()
            else:
                print("Shape 3")
                self.image_result = np.zeros((self.rows, self.cols, 3), np.uint8)
                return self.__mult_3_shapes()

    def __mult_3_shapes(self):
        for row in range(self.rows):
            for col in range(self.cols):

                r_img1 = self.image1.item(row, col, 0)
                g_img1 = self.image1.item(row, col, 1)
                b_img1 = self.image1.item(row, col, 2)

                r_img2 = self.image2.item(row, col, 0)
                g_img2 = self.image2.item(row, col, 1)
                b_img2 = self.image2.item(row, col, 2)

                r_result = abs(r_img1 * r_img2)
                g_result = abs(g_img1 * g_img2)
                b_result = abs(b_img1 * b_img2)

                values = fit_value([r_result, g_result, b_result])

                self.image_result.itemset((row, col, 0), values[0])
                self.image_result.itemset((row, col, 1), values[1])
                self.image_result.itemset((row, col, 2), values[2])
        self.show_images_by_side("Multiplicacao RGB")
        return self.image_result

    def __mult_2_shapes(self):
        for row in range(self.rows):
            for col in range(self.cols):
                pixel1 = self.image1.item(row, col)
                pixel2 = self.image2.item(row, col)
                result = abs(pixel1 * pixel2)
                self.image_result.itemset((row, col), result)
        self.show_images_by_side("Multiplicacao")
        return self.image_result

    def div_operation(self):
        equal_size = self.__verify_shapes()
        if equal_size:
            if len(self.shape) == 2:
                self.image_result = np.zeros((self.rows, self.cols), np.uint8)
                return self.__div_2_shapes()
            else:
                print("Shape 3")
                self.image_result = np.zeros((self.rows, self.cols, 3), np.uint8)
                return self.__div_3_shapes()

    def __check_value_den(self, value):
        if(value <= 0):
            value = 1
        else:
            return value
        return value

    def __div_3_shapes(self):
        for row in range(self.rows):
            for col in range(self.cols):

                r_img1 = self.image1.item(row, col, 0)
                g_img1 = self.image1.item(row, col, 1)
                b_img1 = self.image1.item(row, col, 2)

                r_img2 = self.image2.item(row, col, 0)
                g_img2 = self.image2.item(row, col, 1)
                b_img2 = self.image2.item(row, col, 2)

                newValue_rImg2 = self.__check_value_den(r_img2)
                newValue_gImg2 = self.__check_value_den(g_img2)
                newValue_bImg2 = self.__check_value_den(b_img2)

                r_result = abs(r_img1 / newValue_rImg2)
                g_result = abs(g_img1 / newValue_gImg2)
                b_result = abs(b_img1 / newValue_bImg2)

                values = fit_value([r_result, g_result, b_result])

                self.image_result.itemset((row, col, 0), values[0])
                self.image_result.itemset((row, col, 1), values[1])
                self.image_result.itemset((row, col, 2), values[2])
        self.show_images_by_side("Divisao RGB")
        return self.image_result

    def __div_2_shapes(self):
        for row in range(self.rows):
            for col in range(self.cols):
                pixel1 = self.image1.item(row, col)
                pixel2 = self.image2.item(row, col)
                if(pixel2 <= 0):
                    newValue_pixel2 = 1
                else:
                    newValue_pixel2 = pixel2
                result = abs(pixel1 / newValue_pixel2)
                self.image_result.itemset((row, col), result)
        self.show_images_by_side("Divisao")
        return self.image_result

    def show_images_by_side(self, name_operation):
        horizontal = np.concatenate((self.image1, self.image_result), axis=1)
        cv2.imshow(name_operation, horizontal)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
