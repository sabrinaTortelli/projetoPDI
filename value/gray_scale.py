import cv2


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

    def gray_convert_simple(self):
        #recebe uma matriz imagem e percorre todas as linhas e colunas
        #somando os pixels RGB de cada posicão e faz a média simples
        #deixando a imgem com tons de cinza
        for i in range(self.row):
            for j in range(self.col):
                self.image[i, j] = sum(self.image[i, j]) * 0.33
        cv2.imshow('Simple Grayscale Image', self.image)
        cv2.waitKey(0)
        return self.image

    def gray_convert_ponder(self):
        # recebe uma matriz imagem e percorre todas as linhas e colunas
        # chamando o metodo gray_manipulation para realizar a média ponderada dos pixels
        # deixando a imgem com tons de cinza
        for i in range(self.row):
            for j in range(self.col):
                self.image[i, j] = sum(GrayPonder.gray_pixel_manipulation(self.image[i, j]))
        cv2.imshow('Ponder Grayscale Image', self.image)
        cv2.waitKey(0)
        return self.image
