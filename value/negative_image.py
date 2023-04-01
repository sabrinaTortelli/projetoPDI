import cv2
import numpy as np


class NegativeImage(object):
    # recebe um objeto imagem e armazena o numero de colunas e linhas da matriz imagem
    def __init__(self, image):
        self.image = image
        self.row = self.image.shape[0]
        self.col = self.image.shape[1]
        self.extracted_negative_image = np.zeros((self.row, self.col, self.image.shape[2]), np.uint8)

    def negative_image(self):
        # percorre todas as colunas e linhas da imagem recebida no init
        # e extraindo os valores RGB e retorna em uma lista
        [self.extracted_negative_image[i, j].__setitem__(k, 255 - self.image[i, j][k]) for i in range(self.row) for j in
                         range(self.col) for k in range(3)]

        cv2.imshow('Negative Image', np.concatenate((self.image, self.extracted_negative_image), axis=1))
        cv2.waitKey(0)
        return self.extracted_negative_image





