import numpy as np

from morphology.erode import Erode as ER
from morphology.dilate import Dilate as DL
from space import show_images_by_side


# Classe de operação de abertura
class Opening(object):

    # Recebe a imagem e o kernel
    def __init__(self, image, kernel):
        # recebe a imagem
        self.image = image
        # recebe o kernel
        self.kernel = kernel
        # cria a imagem de saída
        self.opening_image = np.zeros((self.image.shape[0], self.image.shape[1]), np.uint8)

    # Operação de abertura: erosão seguida de uma dilatação utilizando o mesmo kernel
    # Retorna a imagem resultante da operação
    def opening(self):
        # operação de erosão
        erode = ER(self.image, self.kernel)
        erode_image = erode.erode()
        # operação de dilatação
        dilate = DL(erode_image, self.kernel)
        self.opening_image = dilate.dilate()
        # Mostra a imagem original e a resultante lado a lado
        show_images_by_side("Opening Image", self.image, self.opening_image)
        return self.opening_image

