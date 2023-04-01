import numpy as np

from space import show_images_by_side


# Classe de operação de dilatação
class Dilate(object):

    # Recebe uma imagem e a máscara (kernel)
    def __init__(self, image, kernel):
        # recebe a imagem
        self.image = image
        self.row = self.image.shape[0]
        self.col = self.image.shape[1]
        # cria a imagem de saída
        self.dilate_image = np.zeros((self.row, self.col), np.uint8)
        # recebe a máscara (kernel)
        self.kernel = kernel
        self.row_kernel = len(self.kernel)
        self.col_kernel = len(self.kernel[0])
        # Divisão inteira do tamanho da máscara para determinar as partes que ficarão de fora da convolução
        self.start = len(self.kernel) // 2

    # Operação de dilatação
    # Retorna a imagem resultante da operação
    def dilate(self):
        for row in range(self.start, self.row - self.start):  # lines
            for col in range(self.start, self.col - self.start):  # columns
                start_row = row - self.start  # limite aberto
                end_row = row + self.start + 1  # limite fechado
                start_col = col - self.start
                end_col = col + self.start + 1
                # sub imagem em relação a original, de mesmo tamanho do kernel
                sub_img = self.image[start_row:end_row, start_col:end_col]
                sub_img_result = self.dilate_image[start_row:end_row, start_col:end_col]

                # pixel central na sub_imagem
                pixel_img = sub_img.item(self.start, self.start)

                # Se o pixel central da imagem for diferente de 0 verifica se os pixels do
                # kernel são diferentes de 0 e atribui a cor branca para eles
                if pixel_img != 0:
                    for r in range(self.row_kernel):  # lines
                        for c in range(self.col_kernel):  # colum
                            pixel_ker = self.kernel.item(r, c)

                            if pixel_ker != 0:
                                sub_img_result.itemset((r, c), 255)
        # Mostra a imagem original e a resultante lado a lado
        show_images_by_side("Dilate Image", self.image, self.dilate_image)
        return self.dilate_image
