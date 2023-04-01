import numpy as np

from arithmetic_operations import check_value_den
from space import show_images_by_side, fit_value, fit_1_value


# Classe de operações matemática entre duas imagens
class ArithmeticOperationsImages(object):

    # Recebe duas imagens
    def __init__(self, image1, image2):
        self.image1 = image1
        self.image2 = image2
        self.rows = self.image1.shape[0]
        self.cols = self.image1.shape[1]
        self.shape = self.image1.shape
        self.image_result = None

    # Verifica se as duas imagens tem os mesmos tamanhos
    # Caso tenha retorna true e pode prosseguir com as operações
    # Caso não tenha retorna false e não pode prosseguir com as operações
    def __verify_shapes(self):
        if self.image1.shape[0] == self.image2.shape[0] and self.image1.shape[1] == self.image2.shape[1]:
            return True
        else:
            return False

    # Operação de adição
    # Retorna imagem resultante
    def add_operation(self):
        equal_size = self.__verify_shapes()
        # Verifica tamanhos das imagens e prossegue caso tenham tamanhos iguais
        # Mostra mensagem de erro caso tenham tamanhos diferentes
        if equal_size:
            # Verifica canais da imagem e escolhe operação adequada para cada imagem
            if len(self.shape) == 2:
                self.image_result = np.zeros((self.rows, self.cols), np.uint8)
                return self.__add_2_shapes()
            else:
                self.image_result = np.zeros((self.rows, self.cols, 3), np.uint8)
                return self.__add_3_shapes()
        else:
            print("Erro. Imagens com tamanhos diferentes")

    # Operação de adição com 3 canais rgb
    # Retorna imagem resultante
    def __add_3_shapes(self):
        for row in range(self.rows):
            for col in range(self.cols):
                # Atribui os pixels de cada canal das imagens
                r_img1 = self.image1.item(row, col, 0)
                g_img1 = self.image1.item(row, col, 1)
                b_img1 = self.image1.item(row, col, 2)

                r_img2 = self.image2.item(row, col, 0)
                g_img2 = self.image2.item(row, col, 1)
                b_img2 = self.image2.item(row, col, 2)

                # Realiza a operação de adição dos pixels de cada canal e ajusta o resultado
                r_result = abs(r_img1 + r_img2)
                g_result = abs(g_img1 + g_img2)
                b_result = abs(b_img1 + b_img2)

                values = fit_value([r_result, g_result, b_result])

                # Atribui o resultado aos pixels da imagem resultante
                self.image_result.itemset((row, col, 0), values[0])
                self.image_result.itemset((row, col, 1), values[1])
                self.image_result.itemset((row, col, 2), values[2])
        # Mostra a imagem original e a imagem resultante lado a lado
        show_images_by_side("Adicao RGB", self.image1, self.image_result)
        return self.image_result

    # Operação de adição sem canal rgb
    # Retorna imagem resultante
    def __add_2_shapes(self):
        for row in range(self.rows):
            for col in range(self.cols):
                # Atribui os pixels das imagens
                pixel1 = self.image1.item(row, col)
                pixel2 = self.image2.item(row, col)
                # Realiza a operação de adição e ajusta o resultado
                result = fit_1_value(abs(pixel1 + pixel2))
                # Atribui o resultado aos pixels da imagem resultante
                self.image_result.itemset((row, col), result)
        # Mostra a imagem original e a imagem resultante lado a lado
        show_images_by_side("Adicao", self.image1, self.image_result)
        return self.image_result

    # Operação de subtração
    # Retorna imagem resultante
    def sub_operation(self):
        equal_size = self.__verify_shapes()
        # Verifica tamanhos das imagens e prossegue caso tenham tamanhos iguais
        # Mostra mensagem de erro caso tenham tamanhos diferentes
        if equal_size:
            # Verifica canais da imagem e escolhe operação adequada para cada imagem
            if len(self.shape) == 2:
                self.image_result = np.zeros((self.rows, self.cols), np.uint8)
                return self.__sub_2_shapes()
            else:
                self.image_result = np.zeros((self.rows, self.cols, 3), np.uint8)
                return self.__sub_3_shapes()
        else:
            print("Erro. Imagens com tamanhos diferentes")

    # Operação de subtração com 3 canais rgb
    # Retorna imagem resultante
    def __sub_3_shapes(self):
        for row in range(self.rows):
            for col in range(self.cols):
                # Atribui os pixels de cada canal das imagens
                r_img1 = self.image1.item(row, col, 0)
                g_img1 = self.image1.item(row, col, 1)
                b_img1 = self.image1.item(row, col, 2)

                r_img2 = self.image2.item(row, col, 0)
                g_img2 = self.image2.item(row, col, 1)
                b_img2 = self.image2.item(row, col, 2)
                # Realiza a operação de subtração e ajusta o resultado
                r_result = abs(r_img1 - r_img2)
                g_result = abs(g_img1 - g_img2)
                b_result = abs(b_img1 - b_img2)

                values = fit_value([r_result, g_result, b_result])
                # Atribui o resultado aos pixels da imagem resultante
                self.image_result.itemset((row, col, 0), values[0])
                self.image_result.itemset((row, col, 1), values[1])
                self.image_result.itemset((row, col, 2), values[2])
        # Mostra a imagem original e a imagem resultante lado a lado
        show_images_by_side("Subtracao RGB", self.image1, self.image_result)
        return self.image_result

    # Operação de subtração sem canal rgb
    # Retorna imagem resultante
    def __sub_2_shapes(self):
        for row in range(self.rows):
            for col in range(self.cols):
                pixel1 = self.image1.item(row, col)
                pixel2 = self.image2.item(row, col)
                # Realiza a operação de subtração e ajusta o resultado
                result = fit_1_value(abs(pixel1 - pixel2))
                # Atribui o resultado aos pixels da imagem resultante
                self.image_result.itemset((row, col), result)
        # Mostra a imagem original e a imagem resultante lado a lado
        show_images_by_side("Subtracao", self.image1, self.image_result)
        return self.image_result

    # Operação de multiplicação
    # Retorna imagem resultante
    def mult_operation(self):
        # Verifica tamanhos das imagens e prossegue caso tenham tamanhos iguais
        # Mostra mensagem de erro caso tenham tamanhos diferentes
        equal_size = self.__verify_shapes()
        if equal_size:
            # Verifica canais da imagem e escolhe operação adequada para cada imagem
            if len(self.shape) == 2:
                self.image_result = np.zeros((self.rows, self.cols), np.uint8)
                return self.__mult_2_shapes()
            else:
                self.image_result = np.zeros((self.rows, self.cols, 3), np.uint8)
                return self.__mult_3_shapes()
        else:
            print("Erro. Imagens com tamanhos diferentes")

    # Operação de multiplicação com 3 canais rgb
    # Retorna imagem resultante
    def __mult_3_shapes(self):
        for row in range(self.rows):
            for col in range(self.cols):
                # Atribui os pixels de cada canal das imagens
                r_img1 = self.image1.item(row, col, 0)
                g_img1 = self.image1.item(row, col, 1)
                b_img1 = self.image1.item(row, col, 2)

                r_img2 = self.image2.item(row, col, 0)
                g_img2 = self.image2.item(row, col, 1)
                b_img2 = self.image2.item(row, col, 2)
                # Realiza a operação de multiplicação e ajusta o resultado
                r_result = abs(r_img1 * r_img2)
                g_result = abs(g_img1 * g_img2)
                b_result = abs(b_img1 * b_img2)

                values = fit_value([r_result, g_result, b_result])
                # Atribui o resultado aos pixels da imagem resultante
                self.image_result.itemset((row, col, 0), values[0])
                self.image_result.itemset((row, col, 1), values[1])
                self.image_result.itemset((row, col, 2), values[2])
        # Mostra a imagem original e a imagem resultante lado a lado
        show_images_by_side("Multiplicacao RGB", self.image1, self.image_result)
        return self.image_result

    # Operação de multiplicação sem canal rgb
    # Retorna imagem resultante
    def __mult_2_shapes(self):
        for row in range(self.rows):
            for col in range(self.cols):
                pixel1 = self.image1.item(row, col)
                pixel2 = self.image2.item(row, col)
                # Realiza a operação de multiplicação e ajusta o resultado
                result = fit_1_value(abs(pixel1 * pixel2))
                # Atribui o resultado aos pixels da imagem resultante
                self.image_result.itemset((row, col), result)
        # Mostra a imagem original e a imagem resultante lado a lado
        show_images_by_side("Multiplicacao", self.image1, self.image_result)
        return self.image_result

    # Operação de divisão
    # Retorna imagem resultante
    def div_operation(self):
        # Verifica tamanhos das imagens e prossegue caso tenham tamanhos iguais
        # Mostra mensagem de erro caso tenham tamanhos diferentes
        equal_size = self.__verify_shapes()
        if equal_size:
            # Verifica canais da imagem e escolhe operação adequada para cada imagem
            if len(self.shape) == 2:
                self.image_result = np.zeros((self.rows, self.cols), np.uint8)
                return self.__div_2_shapes()
            else:
                self.image_result = np.zeros((self.rows, self.cols, 3), np.uint8)
                return self.__div_3_shapes()
        else:
            print("Erro. Imagens com tamanhos diferentes")

    # Operação de divisão com 3 canais rgb
    # Retorna imagem resultante
    def __div_3_shapes(self):
        for row in range(self.rows):
            for col in range(self.cols):
                # Atribui os pixels de cada canal das imagens
                r_img1 = self.image1.item(row, col, 0)
                g_img1 = self.image1.item(row, col, 1)
                b_img1 = self.image1.item(row, col, 2)

                r_img2 = self.image2.item(row, col, 0)
                g_img2 = self.image2.item(row, col, 1)
                b_img2 = self.image2.item(row, col, 2)
                # Ajusta o divisor caso menor ou igual a 0
                newValue_rImg2 = check_value_den(r_img2)
                newValue_gImg2 = check_value_den(g_img2)
                newValue_bImg2 = check_value_den(b_img2)
                # Realiza a operação de divisão
                r_result = abs(r_img1 / newValue_rImg2)
                g_result = abs(g_img1 / newValue_gImg2)
                b_result = abs(b_img1 / newValue_bImg2)
                # Ajusta o valor do pixel para não estourar
                values = fit_value([r_result, g_result, b_result])
                # Atribui o resultado aos pixels da imagem resultante
                self.image_result.itemset((row, col, 0), values[0])
                self.image_result.itemset((row, col, 1), values[1])
                self.image_result.itemset((row, col, 2), values[2])
        # Mostra a imagem original e a imagem resultante lado a lado
        show_images_by_side("Divisao RGB", self.image1, self.image_result)
        return self.image_result

    # Operação de divisão sem canal rgb
    # Retorna imagem resultante
    def __div_2_shapes(self):
        for row in range(self.rows):
            for col in range(self.cols):
                # Atribui os pixels das imagens
                pixel1 = self.image1.item(row, col)
                pixel2 = self.image2.item(row, col)
                # Ajusta o divisor caso menor ou igual a 0
                newValue_pixel2 = check_value_den(pixel2)
                # Realiza a operação de divisão e ajusta o valor do pixel
                result = fit_1_value(abs(pixel1 / newValue_pixel2))
                # Atribui o resultado aos pixels da imagem resultante
                self.image_result.itemset((row, col), result)
        # Mostra a imagem original e a imagem resultante lado a lado
        show_images_by_side("Divisao", self.image1, self.image_result)
        return self.image_result
