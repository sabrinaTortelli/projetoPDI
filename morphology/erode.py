import numpy as np

from space import show_images_by_side


# Classe de operação de erosão
class Erode(object):

    # Recebe uma imagem e a máscara (kernel)
    def __init__(self, image, kernel):
        # recebe a imagem
        self.image = image
        self.row = self.image.shape[0]
        self.col = self.image.shape[1]
        # cria a imagem de saída
        self.erode_image = np.zeros((self.row, self.col), np.uint8)
        # recebe a máscara (kernel)
        self.kernel = kernel
        self.row_kernel = len(self.kernel)
        self.col_kernel = len(self.kernel[0])
        # Divisão inteira do tamanho da máscara para determinar as partes que ficarão de fora da convolução
        self.start = len(self.kernel) // 2

    # Operação de erosão
    # Retorna a imagem resultante da operação
    def erode(self):
        for row in range(self.start, self.row - self.start):  # lines
            for col in range(self.start, self.col - self.start):  # columns
                start_row = row - self.start  # limite aberto
                end_row = row + self.start + 1  # limite fechado
                start_col = col - self.start
                end_col = col + self.start + 1

                # sub imagem em relação a original, de mesmo tamanho do kernel
                sub_img = self.image[start_row:end_row, start_col:end_col]

                # percorre toda a sub-imagem
                count_kernel = 0
                count_result = 0
                for r in range(self.row_kernel):  # lines
                    for c in range(self.col_kernel):  # colum
                        pixel_img = sub_img.item(r, c)
                        pixel_ker = self.kernel.item(r, c)
                        # contabiliza quantos valores no kernel são não nulos
                        if pixel_ker == 1:
                            count_kernel += 1
                        # contabiliza valores não nulos coincidentes da sub-imagem e kernel
                        if pixel_ker == 1 and pixel_img == 255:
                            count_result += 1

                # se todos os valores coincidirem sera o pixel da imagem com a cor branca
                # se não coincidirem sera o pixel da imagem com a cor preta
                if count_kernel == count_result:
                    self.erode_image.itemset((row, col), 255)
                else:
                    self.erode_image.itemset((row, col), 0)
        # Mostra a imagem original e a resultante lado a lado
        show_images_by_side("Erode Image", self.image, self.erode_image)
        return self.erode_image

