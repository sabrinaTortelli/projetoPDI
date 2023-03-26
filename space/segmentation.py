import cv2
import numpy as np

from space.convolution import Convolution as CVLT
from arithmetic_operations.arithmetic_operations_images import ArithmeticOperationsImages as AOI


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
        print("Entrou no Sobel")
        self.__initMatrix()
        return self.__sobel()

    def roberts(self):
        print("Entrou no Roberts")
        self.__initMatrix()
        return self.__roberts()

    def __sobel(self):
        # Máscaras de Sobel
        mask_hor = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
        mask_ver = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
        # Convolução da primeira imagem
        convolution_img_hor = CVLT(self.image1, mask_hor)
        self.conv_image1 = convolution_img_hor.convolution()
        # Convolução da segunda imagem
        convolution_img_ver = CVLT(self.image2, mask_ver)
        self.conv_image2 = convolution_img_ver.convolution()
        # Adição das imagens
        result_image = AOI(self.conv_image1, self.conv_image2)
        self.image_result = result_image.add_operation()
        # Mostra a imagem original e a imagem transformada lado a lado
        self.show_images_by_side("Sobel")
        return self.image_result

    def __roberts(self):
        # Máscaras de Roberts
        mask_hor = [[0, 0, 0], [0, 1, 0], [0, 0, -1]]
        mask_ver = [[0, 0, 0], [0, -1, 0], [0, 0, 1]]
        # Convolução da primeira imagem
        convolution_img_hor = CVLT(self.image1, mask_hor)
        self.conv_image1 = convolution_img_hor.convolution()
        # Convolução da segunda imagem
        convolution_img_ver = CVLT(self.image2, mask_ver)
        self.conv_image2 = convolution_img_ver.convolution()
        # Adição das imagens
        result_image = AOI(self.conv_image1, self.conv_image2)
        self.image_result = result_image.add_operation()
        # Mostra a imagem original e a imagem transformada lado a lado
        self.show_images_by_side("Roberts")
        return self.image_result

    def show_images_by_side(self, name_operation):
        horizontal = np.concatenate((self.image, self.image_result), axis=1)
        cv2.imshow(name_operation, horizontal)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
