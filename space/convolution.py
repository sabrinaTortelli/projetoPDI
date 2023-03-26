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


class Convolution(object):

    def __init__(self, image, mask):
        # recebe a imagem e o tamanho da máscara de convolução
        self.convolution_image = None
        self.image = image
        self.row = self.image.shape[0]
        self.col = self.image.shape[1]

        self.mask = mask
        self.row_mask = len(self.mask)
        self.col_mask = len(self.mask[0])
        # Divisão inteira do tamanho da máscara para determinar as partes que ficarão de fora da convolução
        self.start = len(self.mask) // 2

    def convolution(self):
        print("Entrou na convolucao")
        # verifica se a imagem tem os 3 canais rgb e escolhe a função adequada para a imagem
        if len(self.image.shape) == 2:
            # cria uma matriz (imagem) zerada sem os canais rgb
            self.convolution_image = np.zeros((self.row, self.col), np.uint8)
            return self.__gray_convolution_operator()
        else:
            # cria uma matriz (imagem) zerada com os canais rgb
            self.convolution_image = np.zeros((self.row, self.col, 3), np.uint8)
            return self.__rgb_convolution_operator()

    def __gray_convolution_operator(self):
        for i in range(self.start, self.row - self.start):
            for j in range(self.start, self.col - self.start):
                start_row = i - self.start
                end_row = i + self.start + 1
                start_col = j - self.start
                end_col = j + self.start + 1
                temp_image = self.image[start_row:end_row, start_col:end_col]
                value = self.__gray_convolution_operator_(temp_image)
                if value < 0:
                    self.convolution_image.itemset((i, j), 0)
                elif value > 255:
                    self.convolution_image.itemset((i, j), 255)
                else:
                    self.convolution_image.itemset((i, j), value)
        self.show_images_by_side("Convolução GRAY")
        return self.convolution_image

    def __gray_convolution_operator_(self, temp_image):
        value = 0
        for i in range(self.row_mask):
            for j in range(self.col_mask):
                value += temp_image.item(i, j) * self.mask[i][j]
        return value

    def __rgb_convolution_operator(self):
        for i in range(self.start, self.row - self.start):
            for j in range(self.start, self.col - self.start):
                start_row = i - self.start
                end_row = i + self.start + 1
                start_col = j - self.start
                end_col = j + self.start + 1
                temp_image = self.image[start_row:end_row, start_col:end_col]
                values = self.__rgb_convolution_operator_(temp_image)
                values_fit = fit_value(values)
                self.convolution_image[i, j][0] = values_fit[0]
                self.convolution_image[i, j][1] = values_fit[1]
                self.convolution_image[i, j][2] = values_fit[2]
        self.show_images_by_side("Convolução RGB")
        return self.convolution_image

    def __rgb_convolution_operator_(self, temp_image):
        pixels_red_value = 0
        pixels_green_value = 0
        pixels_blue_value = 0
        for i in range(self.row_mask):
            for j in range(self.col_mask):
                pixels = temp_image[i, j]
                pixels_red_value += pixels[0] * self.mask[i][j]
                pixels_green_value += pixels[1] * self.mask[i][j]
                pixels_blue_value += pixels[2] * self.mask[i][j]
        return [pixels_red_value, pixels_green_value, pixels_blue_value]

    def show_images_by_side(self, name_operation):
        horizontal = np.concatenate((self.image, self.convolution_image), axis=1)
        cv2.imshow(name_operation, horizontal)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
