import numpy as np

from morphology.dilate import Dilate as DL
from arithmetic_operations.arithmetic_operations_images import ArithmeticOperationsImages as AOI
from space import show_images_by_side


# Diferença entre a dilatação e a imagem original
class OuterLimit(object):

    def __init__(self, image, kernel):
        # recebe a imagem
        self.image = image
        self.kernel = kernel
        # cria a imagem de saída
        self.outer_image = np.zeros((self.image.shape[0], self.image.shape[1]), np.uint8)

    # Operação de limite externo: Diferença entre a imagem dilatada e imagem original
    # Retorna a imagem resultante da operação
    def outer_limit(self):
        # Operação de dilatação
        dilate = DL(self.image, self.kernel)
        dilate_image = dilate.dilate()
        # Operação de subtração das imagens
        sub_operation = AOI(dilate_image, self.image)
        self.outer_image = sub_operation.sub_operation()
        # Mostra a imagem original e a resultante lado a lado
        show_images_by_side("Outer Limit Image", self.image, self.outer_image)
        return self.outer_image

