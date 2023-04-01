import numpy as np

from arithmetic_operations import check_value_den
from space import show_images_by_side, fit_value, fit_1_value


# Classe de operações matemática entre duas imagens
class ArithmeticOperationsValue(object):

    # Recebe duas imagens
    def __init__(self, image, value):
        self.image = image
        self.value = value
        self.rows = self.image.shape[0]
        self.cols = self.image.shape[1]
        self.shape = self.image.shape
        self.image_result = None

    # Operação de adição
    # Retorna imagem resultante
    def add_operation(self):
        # Verifica canais da imagem e escolhe operação adequada para cada imagem
        if len(self.shape) == 2:
            self.image_result = np.zeros((self.rows, self.cols), np.uint8)
            return self.__add_2_shapes()
        else:
            self.image_result = np.zeros((self.rows, self.cols, 3), np.uint8)
            return self.__add_3_shapes()

    # Operação de adição com 3 canais rgb
    # Retorna imagem resultante
    def __add_3_shapes(self):
        for row in range(self.rows):
            for col in range(self.cols):
                # Atribui os pixels de cada canal da imagem
                r_img1 = self.image.item(row, col, 0)
                g_img1 = self.image.item(row, col, 1)
                b_img1 = self.image.item(row, col, 2)

                # Realiza a operação de adição dos pixels de cada canal e ajusta o resultado
                r_result = abs(r_img1 + self.value)
                g_result = abs(g_img1 + self.value)
                b_result = abs(b_img1 + self.value)

                values = fit_value([r_result, g_result, b_result])

                # Atribui o resultado aos pixels da imagem resultante
                self.image_result.itemset((row, col, 0), values[0])
                self.image_result.itemset((row, col, 1), values[1])
                self.image_result.itemset((row, col, 2), values[2])
        # Mostra a imagem original e a imagem resultante lado a lado
        show_images_by_side("Adicao Valor RGB", self.image, self.image_result)
        return self.image_result

    # Operação de adição sem canal rgb
    # Retorna imagem resultante
    def __add_2_shapes(self):
        for row in range(self.rows):
            for col in range(self.cols):
                # Atribui os pixels da imagem
                pixel1 = self.image.item(row, col)
                # Realiza a operação de adição e ajusta o resultado
                result = fit_1_value(abs(pixel1 + self.value))
                # Atribui o resultado aos pixels da imagem resultante
                self.image_result.itemset((row, col), result)
        # Mostra a imagem original e a imagem resultante lado a lado
        show_images_by_side("Adicao Valor", self.image, self.image_result)
        return self.image_result

    # Operação de subtração
    # Retorna imagem resultante
    def sub_operation(self):
        # Verifica canais da imagem e escolhe operação adequada para cada imagem
        if len(self.shape) == 2:
            self.image_result = np.zeros((self.rows, self.cols), np.uint8)
            return self.__sub_2_shapes()
        else:
            self.image_result = np.zeros((self.rows, self.cols, 3), np.uint8)
            return self.__sub_3_shapes()

    # Operação de subtração com 3 canais rgb
    # Retorna imagem resultante
    def __sub_3_shapes(self):
        for row in range(self.rows):
            for col in range(self.cols):
                # Atribui os pixels de cada canal da imagem
                r_img1 = self.image.item(row, col, 0)
                g_img1 = self.image.item(row, col, 1)
                b_img1 = self.image.item(row, col, 2)

                # Realiza a operação de subtração e ajusta o resultado
                r_result = abs(r_img1 - self.value)
                g_result = abs(g_img1 - self.value)
                b_result = abs(b_img1 - self.value)

                values = fit_value([r_result, g_result, b_result])
                # Atribui o resultado aos pixels da imagem resultante
                self.image_result.itemset((row, col, 0), values[0])
                self.image_result.itemset((row, col, 1), values[1])
                self.image_result.itemset((row, col, 2), values[2])
        # Mostra a imagem original e a imagem resultante lado a lado
        show_images_by_side("Subtracao Valor RGB", self.image, self.image_result)
        return self.image_result

    # Operação de subtração sem canal rgb
    # Retorna imagem resultante
    def __sub_2_shapes(self):
        for row in range(self.rows):
            for col in range(self.cols):
                pixel1 = self.image.item(row, col)
                # Realiza a operação de subtração e ajusta o resultado
                result = fit_1_value(abs(pixel1 - self.value))
                # Atribui o resultado aos pixels da imagem resultante
                self.image_result.itemset((row, col), result)
        # Mostra a imagem original e a imagem resultante lado a lado
        show_images_by_side("Subtracao Valor", self.image, self.image_result)
        return self.image_result

    # Operação de multiplicação
    # Retorna imagem resultante
    def mult_operation(self):
        # Verifica canais da imagem e escolhe operação adequada para cada imagem
        if len(self.shape) == 2:
            self.image_result = np.zeros((self.rows, self.cols), np.uint8)
            return self.__mult_2_shapes()
        else:
            self.image_result = np.zeros((self.rows, self.cols, 3), np.uint8)
            return self.__mult_3_shapes()

    # Operação de multiplicação com 3 canais rgb
    # Retorna imagem resultante
    def __mult_3_shapes(self):
        for row in range(self.rows):
            for col in range(self.cols):
                # Atribui os pixels de cada canal da imagem
                r_img1 = self.image.item(row, col, 0)
                g_img1 = self.image.item(row, col, 1)
                b_img1 = self.image.item(row, col, 2)

                # Realiza a operação de multiplicação e ajusta o resultado
                r_result = abs(r_img1 * self.value)
                g_result = abs(g_img1 * self.value)
                b_result = abs(b_img1 * self.value)

                values = fit_value([r_result, g_result, b_result])
                # Atribui o resultado aos pixels da imagem resultante
                self.image_result.itemset((row, col, 0), values[0])
                self.image_result.itemset((row, col, 1), values[1])
                self.image_result.itemset((row, col, 2), values[2])
        # Mostra a imagem original e a imagem resultante lado a lado
        show_images_by_side("Multiplicacao Valor RGB", self.image, self.image_result)
        return self.image_result

    # Operação de multiplicação sem canal rgb
    # Retorna imagem resultante
    def __mult_2_shapes(self):
        for row in range(self.rows):
            for col in range(self.cols):
                pixel1 = self.image.item(row, col)
                # Realiza a operação de multiplicação e ajusta o resultado
                result = fit_1_value(abs(pixel1 * self.value))
                # Atribui o resultado aos pixels da imagem resultante
                self.image_result.itemset((row, col), result)
        # Mostra a imagem original e a imagem resultante lado a lado
        show_images_by_side("Multiplicacao Valor", self.image, self.image_result)
        return self.image_result

    # Operação de divisão
    # Retorna imagem resultante
    def div_operation(self):
        # Verifica se o valor é diferente de zero
        # Mostra mensagem de erro caso o valor seja igual a 0
        if self.value != 0:
            # Verifica canais da imagem e escolhe operação adequada para cada imagem
            if len(self.shape) == 2:
                self.image_result = np.zeros((self.rows, self.cols), np.uint8)
                return self.__div_2_shapes()
            else:
                self.image_result = np.zeros((self.rows, self.cols, 3), np.uint8)
                return self.__div_3_shapes()
        else:
            print("Não é possível fazer divisão por 0")

    # Operação de divisão com 3 canais rgb
    # Retorna imagem resultante
    def __div_3_shapes(self):
        for row in range(self.rows):
            for col in range(self.cols):
                # Atribui os pixels de cada canal das imagens
                r_img1 = self.image.item(row, col, 0)
                g_img1 = self.image.item(row, col, 1)
                b_img1 = self.image.item(row, col, 2)

                # Realiza a operação de divisão
                r_result = abs(r_img1 / self.value)
                g_result = abs(g_img1 / self.value)
                b_result = abs(b_img1 / self.value)
                # Ajusta o valor do pixel para não estourar
                values = fit_value([r_result, g_result, b_result])
                # Atribui o resultado aos pixels da imagem resultante
                self.image_result.itemset((row, col, 0), values[0])
                self.image_result.itemset((row, col, 1), values[1])
                self.image_result.itemset((row, col, 2), values[2])
        # Mostra a imagem original e a imagem resultante lado a lado
        show_images_by_side("Divisao Valor RGB", self.image, self.image_result)
        return self.image_result

    # Operação de divisão sem canal rgb
    # Retorna imagem resultante
    def __div_2_shapes(self):
        for row in range(self.rows):
            for col in range(self.cols):
                # Atribui os pixels das imagens
                pixel1 = self.image.item(row, col)
                # Realiza a operação de divisão e ajusta o valor do pixel
                result = fit_1_value(abs(pixel1 / self.value))
                # Atribui o resultado aos pixels da imagem resultante
                self.image_result.itemset((row, col), result)
        # Mostra a imagem original e a imagem resultante lado a lado
        show_images_by_side("Divisao", self.image1, self.image_result)
        return self.image_result
