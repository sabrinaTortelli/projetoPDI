import numpy as np

from morphology.erode import Erode as ER
from arithmetic_operations.arithmetic_operations_images import ArithmeticOperationsImages as AOI
from space import show_images_by_side


# Diferença entre a imagem e a erosão da mesma
class InnerLimit(object):

    # Recebe a imagem e o kernel
    def __init__(self, image, kernel):
        # recebe a imagem
        self.image = image
        # recebe o kernel
        self.kernel = kernel
        # cria a imagem de saída
        self.inner_image = np.zeros((self.image.shape[0], self.image.shape[1]), np.uint8)

    # Operação de limite interno: Diferença entre a imagem e a erosão da mesma
    # Retorna a imagem resultante da operação
    def inner_limit(self):
        # Operação de erosão
        erode = ER(self.image, self.kernel)
        erode_image = erode.erode()
        # Operação de subtração das imagens
        sub_operation = AOI(self.image, erode_image)
        self.inner_image = sub_operation.sub_operation()
        # Mostra a imagem original e a resultante lado a lado
        show_images_by_side("Inner Limit Image", self.image, self.inner_image)
        return self.inner_image
