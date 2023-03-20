import matplotlib.pyplot as plt


class Histogram(object):
    # recebe um objeto imagem e armazena o numero de colunas e linhas da matriz imagem
    # chama o método pixel counter para armazenar em uma lista os valores de todos os pixels de uma imagem
    def __init__(self, image):
        self.image = image
        self.row = self.image.shape[0]
        self.col = self.image.shape[1]
        self.pixel_counter = self.pixel_counter

    # def pixel_counter(self):
    #    [pixel for pixel in self.row ]
    #    pixel_counter = []
    #    for i in range(self.row):
    #        for j in range(self.col):
    #            pixel_counter.append(self.image[i, j][0])
    #            pixel_counter.append(self.image[i, j][1])
    #            pixel_counter.append(self.image[i, j][2])
    #    return pixel_counter

    def pixel_counter(self):
        # percorre tudas as colunas e linhas da imagem recebida no init
        # e extraindo os valores RGB e retorna em uma lista
        pixel_counter = [self.image[i][j][c] for i in range(self.row) for j in range(self.col) for c in range(3)]
        return pixel_counter

    def plot_hist(self):
        #chama o método pixel_counter e imprime um gráfico com os valores obtidos
        plt.xlabel("Intensity")
        plt.ylabel("Number")
        plt.hist(self.pixel_counter())
        plt.show()
