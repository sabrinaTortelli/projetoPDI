import math

import cv2
import numpy as np

from space.convolution import Convolution as CVLT
from arithmetic_operations.arithmetic_operations_images import ArithmeticOperationsImages as AOI
from space import fit_1_value, fit_value, show_images_by_side


class Segmentation(object):

    def __init__(self, image):
        self.image = image
        self.image1 = image
        self.image2 = image
        self.rows = self.image1.shape[0]
        self.cols = self.image1.shape[1]
        self.image_result = None
        self.conv_image1 = None
        self.conv_image2 = None

    def __initMatrix(self):
        if len(self.image.shape) == 2:
            # cria uma matriz (imagem) zerada sem os canais rgb
            self.conv_image1 = np.zeros((self.rows, self.cols), np.uint8)
            self.conv_image2 = np.zeros((self.rows, self.cols), np.uint8)
        else:
            # cria uma matriz (imagem) zerada com os canais rgb
            self.conv_image1 = np.zeros((self.rows, self.cols, 3), np.uint8)
            self.conv_image2 = np.zeros((self.rows, self.cols, 3), np.uint8)

    def sobel(self):
        print("Operação de Sobel")
        self.__initMatrix()
        return self.__sobel()

    def roberts(self):
        print("Operação de Roberts")
        self.__initMatrix()
        return self.__roberts()

    def __sobel(self):
        # Máscaras de Sobel
        mask_hor = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
        mask_ver = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
        # Convolução da primeira imagem
        print("Convolucao imagem com mascara horizontal")
        convolution_img_hor = CVLT(self.image1, mask_hor)
        self.conv_image1 = convolution_img_hor.convolution()
        # Convolução da segunda imagem
        print("Convolucao imagem com mascara vertical")
        convolution_img_ver = CVLT(self.image2, mask_ver)
        self.conv_image2 = convolution_img_ver.convolution()
        # Adição das imagens
        result_image = AOI(self.conv_image1, self.conv_image2)
        self.image_result = result_image.add_operation()
        # Mostra a imagem original e a imagem transformada lado a lado
        show_images_by_side("Sobel", self.image, self.image_result)
        return self.image_result

    def __roberts(self):
        # Máscaras de Roberts
        mask_hor = [[0, 1], [-1, 0]]
        mask_ver = [[1, 0], [0, -1]]
        # Convolução da primeira imagem
        print("Convolucao imagem e mascara horizontal")
        convolution_img_hor = CVLT(self.image1, mask_hor)
        self.conv_image1 = convolution_img_hor.convolution()
        # Convolução da segunda imagem
        print("Convolucao imagem com mascara vertical")
        convolution_img_ver = CVLT(self.image2, mask_ver)
        self.conv_image2 = convolution_img_ver.convolution()
        # Operação final com as imagens resultantes da convolução
        self.__operation_roberts()
        # Mostra a imagem original e a imagem transformada lado a lado
        show_images_by_side("Roberts", self.image, self.image_result)
        return self.image_result

    def __operation_roberts(self):
        if len(self.conv_image1.shape) == 2:
            # cria uma matriz (imagem) zerada sem os canais rgb
            self.image_result = np.zeros((self.rows, self.cols), np.uint8)
            for row in range(self.conv_image1.shape[0]):  # lines
                for col in range(self.conv_image1.shape[1]):  # columns
                    pixel1 = self.conv_image1.item(row, col)
                    pixel2 = self.conv_image2.item(row, col)
                    result = math.sqrt((pixel1 ** 2) + (pixel2 ** 2))
                    # atribui o resultado à imagem resultante
                    self.image_result.itemset((row, col), result)
        else:
            # cria uma matriz (imagem) zerada com os canais rgb
            self.image_result = np.zeros((self.rows, self.cols, 3), np.uint8)
            for row in range(self.conv_image1.shape[0]):  # lines
                for col in range(self.conv_image1.shape[1]):  # columns
                    # atribui cada pixel da imagem 1 a um canal
                    r_img1 = self.conv_image1.item(row, col, 0)
                    g_img1 = self.conv_image1.item(row, col, 1)
                    b_img1 = self.conv_image1.item(row, col, 2)
                    # atribui cada pixel da imagem 2 a um canal
                    r_img2 = self.conv_image2.item(row, col, 0)
                    g_img2 = self.conv_image2.item(row, col, 1)
                    b_img2 = self.conv_image2.item(row, col, 2)

                    r_result = math.sqrt((r_img1 ** 2) + (r_img2 ** 2))
                    g_result = math.sqrt((g_img1 ** 2) + (g_img2 ** 2))
                    b_result = math.sqrt((b_img1 ** 2) + (b_img2 ** 2))
                    # faz ajuste para não estourar os valores
                    values = fit_value([r_result, g_result, b_result])
                    # atribui o pixel final de cada canal à imagem resultante
                    self.image_result.itemset((row, col, 0), values[0])
                    self.image_result.itemset((row, col, 1), values[1])
                    self.image_result.itemset((row, col, 2), values[2])

    def robinson(self):
        print("Operação de Robinson")
        # Máscaras de Robinson
        south = [[1, 0, -1], [2, 0, -2], [1, 0, -1]]
        south_east = [[0, -1, -2], [1, 0, -1], [2, 1, 0]]
        east = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
        north_east = [[-2, -1, 0], [-1, 0, 1], [0, 1, 2]]
        north = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
        north_west = [[0, 1, 2], [-1, 0, 1], [-2, -1, 0]]
        west = [[1, 2, 1], [0, 0, 0], [-1, -2, -1]]
        south_west = [[2, 1, 0], [1, 0, -1], [0, -1, -2]]

        # Convolução de south
        print("Convolucao south")
        conv = CVLT(self.image, south)
        img_south = conv.convolution()
        # Convolução de south east
        print("Convolucao south east")
        conv = CVLT(self.image, south_east)
        img_south_east = conv.convolution()
        # Convolução de east
        print("Convolucao east")
        conv = CVLT(self.image, east)
        img_east = conv.convolution()
        # Convolução de north east
        print("Convolucao north east")
        conv = CVLT(self.image, north_east)
        img_north_east = conv.convolution()
        # Convolução de north
        print("Convolucao north east")
        conv = CVLT(self.image, north)
        img_north = conv.convolution()
        # Convolução de north west
        print("Convolucao north west")
        conv = CVLT(self.image, north_west)
        img_north_west = conv.convolution()
        # Convolução de west
        print("Convolucao west")
        conv = CVLT(self.image, west)
        img_west = conv.convolution()
        # Convolução de south_west
        print("Convolucao south wast")
        conv = CVLT(self.image, south_west)
        img_south_west = conv.convolution()

        # Compara os pixels
        if len(self.image.shape) == 2:
            # cria uma matriz (imagem) zerada sem os canais rgb
            self.image_result = np.zeros((self.rows, self.cols), np.uint8)
            for row in range(self.rows):  # lines
                for col in range(self.cols):  # columns
                    # Coloca os pixels das 8 imagens resultantes em uma lista
                    pixels = [img_south.item(row, col), img_south_east.item(row, col),
                              img_east.item(row, col), img_north_east.item(row, col),
                              img_north.item(row, col), img_north_west.item(row, col),
                              img_west.item(row, col), img_south_west.item(row, col)]
                    # acha o valor máximo do pixel e insere na função para evitar estouro de pixel
                    result = fit_1_value(max(pixels))
                    # atribui o valor máximo a imagem resultante
                    self.image_result.itemset((row, col), result)
        else:
            # cria uma matriz (imagem) zerada com os canais rgb
            self.image_result = np.zeros((self.rows, self.cols, 3), np.uint8)
            for row in range(self.rows):  # lines
                for col in range(self.cols):  # columns
                    # Coloca os pixels das 8 imagens resultantes em uma lista de cada canal
                    pixels_r = [img_south.item(row, col, 0), img_south_east.item(row, col, 0),
                                img_east.item(row, col, 0), img_north_east.item(row, col, 0),
                                img_north.item(row, col, 0), img_north_west.item(row, col, 0),
                                img_west.item(row, col, 0), img_south_west.item(row, col, 0)]

                    pixels_g = [img_south.item(row, col, 1), img_south_east.item(row, col, 1),
                                img_east.item(row, col, 1), img_north_east.item(row, col, 1),
                                img_north.item(row, col, 1), img_north_west.item(row, col, 1),
                                img_west.item(row, col, 1), img_south_west.item(row, col, 1)]

                    pixels_b = [img_south.item(row, col, 2), img_south_east.item(row, col, 2),
                                img_east.item(row, col, 2), img_north_east.item(row, col, 2),
                                img_north.item(row, col, 2), img_north_west.item(row, col, 2),
                                img_west.item(row, col, 2), img_south_west.item(row, col, 2)]
                    # acha o valor máximo do pixel de cada canal e insere na função para evitar estouro de pixel
                    values = fit_value([max(pixels_r), max(pixels_g), max(pixels_b)])
                    # atribui o valor máximo do pixel de cada canal a cada pixel de cada canal da imagem resultante
                    self.image_result.itemset((row, col, 0), values[0])
                    self.image_result.itemset((row, col, 1), values[1])
                    self.image_result.itemset((row, col, 2), values[2])

        # Mostra a imagem original e a imagem transformada lado a lado
        show_images_by_side("Robinson", self.image, self.image_result)
        return self.image_result
