import cv2
import numpy as np


class GrayPonder:
    # recebe um pixel a multiplica os valores RGB para calcular a média ponderada
    def gray_pixel_manipulation(pixel):
        pixel[2] = pixel[2] * 0.1140  # blue
        pixel[1] = pixel[1] * 0.5870  # green
        pixel[0] = pixel[0] * 0.2989  # red
        return [pixel[0], pixel[1], pixel[2]]


class GrayScale(object):
    # recebe um objeto imagem e armazena o numero de colunas e linhas da matriz imagem
    def __init__(self, image):
        self.image = image
        self.row = self.image.shape[0]
        self.col = self.image.shape[1]
        self.extracted_grayscale_image = np.zeros((self.row, self.col, self.image.shape[2]), np.uint8)
        self.extracted_binary_image = np.zeros((self.row, self.col, self.image.shape[2]), np.uint8)

    def gray_convert_simple(self):
        #recebe uma matriz imagem e percorre todas as linhas e colunas
        #somando os pixels RGB de cada posicão e faz a média simples
        #deixando a imgem com tons de cinza
        for i in range(self.row):
            for j in range(self.col):
                self.extracted_grayscale_image[i, j] = sum(self.image[i, j]) * 0.33
        cv2.imshow('Simple Grayscale Image', self.extracted_grayscale_image)
        cv2.waitKey(0)
        return self.extracted_grayscale_image

    def gray_convert_ponder(self):
        # recebe uma matriz imagem e percorre todas as linhas e colunas
        # chamando o metodo gray_manipulation para realizar a média ponderada dos pixels
        # deixando a imgem com tons de cinza
        for i in range(self.row):
            for j in range(self.col):
                self.extracted_grayscale_image[i, j] = sum(GrayPonder.gray_pixel_manipulation(self.image[i, j]))
        cv2.imshow('Ponder Grayscale Image', self.extracted_grayscale_image)
        cv2.waitKey(0)
        return self.extracted_grayscale_image

    def threshold(self, pixel_intensity):
        #recebe uma matriz imagem cinza e percorre todas as linhas e colunas
        #somando os pixels RGB de cada posicão e faz a média simples
        #se a soma for mair que o pixel intesity ele é convertido para branco 255
        #se a soma for menor que o pixel intesity ele é convertido para preto 0
        for i in range(self.row):
            for j in range(self.col):
                if sum(self.extracted_grayscale_image[i, j]) > pixel_intensity:
                    self.extracted_binary_image[i, j] = 255
                else:
                    self.extracted_binary_image[i, j] = 0
        cv2.imshow('Black and White Image', self.extracted_binary_image)
        cv2.waitKey(0)
        return self.extracted_binary_image
