import cv2
import numpy as np

from space import fit_1_value, fit_value, show_images_by_side


# Convolução de imagens
class Convolution(object):

    def __init__(self, image, mask):
        # recebe a imagem
        self.convolution_image = None
        self.image = image
        self.row = self.image.shape[0]
        self.col = self.image.shape[1]
        # recebe a máscara de convolução
        self.mask = mask
        self.row_mask = len(self.mask)
        self.col_mask = len(self.mask[0])
        # Divisão inteira do tamanho da máscara para determinar as partes que ficarão de fora da convolução
        self.start = len(self.mask) // 2

    def convolution(self):
        print("Entrou na convolucao")
        # verifica se a imagem tem os 3 canais rgb ou não e encaminha para a função adequada para a imagem
        if len(self.image.shape) == 2:
            # cria uma matriz (imagem) zerada sem os canais rgb
            self.convolution_image = np.zeros((self.row, self.col), np.uint8)
            return self.__gray_convolution_operator()
        else:
            # cria uma matriz (imagem) zerada com os canais rgb
            self.convolution_image = np.zeros((self.row, self.col, 3), np.uint8)
            return self.__rgb_convolution_operator()

    # Convolução de imagens sem canal
    def __gray_convolution_operator(self):
        for i in range(self.start, self.row - self.start):
            for j in range(self.start, self.col - self.start):
                start_row = i - self.start
                end_row = i + self.start + 1
                start_col = j - self.start
                end_col = j + self.start + 1
                # iguala o tamanho da imagem original à máscara
                temp_image = self.image[start_row:end_row, start_col:end_col]
                # faz a operação de convolução e ajusta o valor resultante
                value = fit_1_value(self.__gray_convolution_operator_(temp_image))
                # atribui o valor à imagem resultante
                self.convolution_image.itemset((i, j), value)
        show_images_by_side("Gray Convolution", self.image, self.convolution_image)
        return self.convolution_image

    # Operação de convolução
    def __gray_convolution_operator_(self, temp_image):
        value = 0
        for i in range(self.row_mask):
            for j in range(self.col_mask):
                value += temp_image.item(i, j) * self.mask[i][j]
        return value

    # Convolução de imagens com 3 canais rgb
    def __rgb_convolution_operator(self):
        for i in range(self.start, self.row - self.start):
            for j in range(self.start, self.col - self.start):
                start_row = i - self.start
                end_row = i + self.start + 1
                start_col = j - self.start
                end_col = j + self.start + 1
                # iguala o tamanho da imagem original à máscara
                temp_image = self.image[start_row:end_row, start_col:end_col]
                # faz a operação de convolução
                values = self.__rgb_convolution_operator_(temp_image)
                # ajusta os valores resultantes
                values_fit = fit_value(values)
                # atribui os valores à imagem resultante
                self.convolution_image.itemset((i, j, 0), values_fit[0])
                self.convolution_image.itemset((i, j, 1), values_fit[1])
                self.convolution_image.itemset((i, j, 2), values_fit[2])
        # Mostra as imagens lado a lado
        show_images_by_side("RGB Convolution", self.image, self.convolution_image)
        return self.convolution_image

    # Operação de convolução de imagens com 3 canais
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
