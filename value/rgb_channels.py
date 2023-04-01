import cv2
import numpy as np


class RGBChannelExtractor:

    def pixel_extractor(pixel, rgb):
        # recebe um pixel e extrai o canal escolhido
        # rgb esta invertido [0] blue, [1] green, [2] red
        isolated_pixel = [0, 0, 0]
        isolated_pixel[rgb] = pixel[rgb]
        return isolated_pixel


class Extractor(object):
    # recebe um objeto imagem e armazena o numero de colunas e linhas da matriz imagem

    def __init__(self, image):
        self.image = image
        self.row = self.image.shape[0]
        self.col = self.image.shape[1]
        self.extracted_isolated_channel_image = np.zeros((self.row, self.col, self.image.shape[2]), np.uint8)
        # self.extracted_isolated_channel_image2 = np.zeros((self.row, self.col, self.image.shape[2]), np.uint8)

    def red_channel(self):
        # recebe uma matriz imagem e percorre todas as linhas e colunas
        # chamando o extrator de pixels com valor 1 para vermelho
        # deixando a imgem com tons de vermelho

        [self.extracted_isolated_channel_image[i, j].__setitem__(k, (
            RGBChannelExtractor.pixel_extractor(self.image[i, j], 2))[k]) for i in range(self.row) for j in
         range(self.col) for k in range(3)]

        cv2.imshow('Red Channel', np.concatenate((self.image, self.extracted_isolated_channel_image), axis=1))
        cv2.waitKey(0)
        return self.extracted_isolated_channel_image

    def green_channel(self):
        # recebe uma matriz imagem e percorre todas as linhas e colunas
        # chamando o extrator de pixels com valor 1 para verde
        # deixando a imgem com tons de verde

        [self.extracted_isolated_channel_image[i, j].__setitem__(k, (
            RGBChannelExtractor.pixel_extractor(self.image[i, j], 1))[k]) for i in range(self.row) for j in
         range(self.col) for k in range(3)]

        cv2.imshow('Green Channel', np.concatenate((self.image, self.extracted_isolated_channel_image), axis=1))
        cv2.waitKey(0)
        return self.extracted_isolated_channel_image

    def blue_channel(self):
        # recebe uma matriz imagem e percorre todas as linhas e colunas
        # chamando o extrator de pixels com valor 0 para azul
        # deixando a imgem com tons de azul

        [self.extracted_isolated_channel_image[i, j].__setitem__(k, (
            RGBChannelExtractor.pixel_extractor(self.image[i, j], 0))[k]) for i in range(self.row) for j in
         range(self.col) for k in range(3)]

        cv2.imshow('Blue Channel', np.concatenate((self.image, self.extracted_isolated_channel_image), axis=1))
        cv2.waitKey(0)
        return self.extracted_isolated_channel_image

# LOOP ORIGINAL
#    def green_channel(self):
#    # recebe uma matriz imagem e percorre todas as linhas e colunas
#    # chamando o extrator de pixels com valor 1 para verde
#    # deixando a imgem com tons de verde
#        for i in range(self.row):
#            for j in range(self.col):
#                self.extracted_isolated_channel_image[i, j] = RGBChannelExtractor.pixel_extractor(self.image[i, j],1)
#        cv2.imshow('Green Channel', self.extracted_isolated_channel_image)
#        cv2.waitKey(0)
#        return self.extracted_isolated_channel_image
