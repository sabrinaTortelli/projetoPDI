import cv2


class RGBChannelExtractor:

    def red_pixel_extractor(pixel):
        # recebe um pixel e zera o seu valor para verde e azul
        pixel[1] = 0  # green
        pixel[2] = 0  # blue
        return [pixel[2], pixel[1], pixel[0]]

    def green_pixel_extractor(pixel):
        # recebe um pixel e zera o seu valor para vermelho e azul
        pixel[2] = 0  # blue
        pixel[0] = 0  # red
        return [pixel[2], pixel[1], pixel[0]]

    def blue_pixel_extractor(pixel):
        # recebe um pixel e zera o seu valor para verde e vermelho
        pixel[0] = 0  # red
        pixel[1] = 0  # green
        return [pixel[2], pixel[1], pixel[0]]


class Extractor(object):
    # recebe um objeto imagem e armazena o numero de colunas e linhas da matriz imagem

    def __init__(self, image):
        self.image = image
        self.row = self.image.shape[0]
        self.col = self.image.shape[1]

    def red_channel(self):
        # recebe uma matriz imagem e percorre todas as linhas e colunas
        # chamando o extrator de pixels vermelho
        # deixando a imgem com tons de vermelho
        for i in range(self.row):
            for j in range(self.col):
                self.image[i, j] = RGBChannelExtractor.red_pixel_extractor(self.image[i, j])
        cv2.imshow('Red Channel', self.image)
        cv2.waitKey(0)
        return self.image

    def green_channel(self):
        # recebe uma matriz imagem e percorre todas as linhas e colunas
        # chamando o extrator de pixels verde
        # deixando a imgem com tons de verde
        for i in range(self.row):
            for j in range(self.col):
                self.image[i, j] = RGBChannelExtractor.green_pixel_extractor(self.image[i, j])
        cv2.imshow('Green Channel', self.image)
        cv2.waitKey(0)
        return self.image

    def blue_channel(self):
        # recebe uma matriz imagem e percorre todas as linhas e colunas
        # chamando o extrator de pixels azul
        # deixando a imgem com tons de azul
        for i in range(self.row):
            for j in range(self.col):
                self.image[i, j] = RGBChannelExtractor.blue_pixel_extractor(self.image[i, j])
        cv2.imshow('Blue Channel', self.image)
        cv2.waitKey(0)
        return self.image
