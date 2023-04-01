import cv2
import numpy as np

from morphology.erode import Erode as ER
from morphology.dilate import Dilate as DL
from space import show_images_by_side


# Classe de operação de fechamento
class Closure(object):

    # Recebe uma imagem e a máscara (kernel)
    def __init__(self, image, kernel):
        # recebe a imagem
        self.image = image
        # recebe a máscara (kernel)
        self.kernel = kernel
        # cria a imagem de saída
        self.closure_image = np.zeros((self.image.shape[0], self.image.shape[1]), np.uint8)

    # Operação de dilatação seguida de uma erosão utilizando o mesmo kernel
    # Retorna a imagem resultante da operação
    def closure(self):
        # dilatação da imagem
        dilate = DL(self.image, self.kernel)
        dilate_image = dilate.dilate()
        # erosão da imagem dilatada
        erode = ER(dilate_image, self.kernel)
        self.closure_image = erode.erode()
        # Mostra a imagem de entrada e a resultante lado a lado
        show_images_by_side("Closure Image", self.image, self.closure_image)
        return self.closure_image
