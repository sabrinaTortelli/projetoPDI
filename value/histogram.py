import matplotlib.pyplot as plt
import numpy as np


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
        values = [0 for i in range(256)]
        list = [self.image[i][j][c] for i in range(self.row) for j in range(self.col) for c in range(3)]

        for i in list:
            value = i
            values[value] += 1
            print(i)

        #return para plot_hist2
        #return list

        # return para plot_hist
        return values

    def plot_hist(self):
        # chama o método pixel_counter e imprime um gráfico com os valores obtidos

        x = np.array(range(256))
        y = np.array(self.pixel_counter())

        plt.title("Image line Graph")
        plt.xlabel("Intensity")
        plt.ylabel("Number")
        plt.plot(x, y, color="red")
        plt.show()

    def plot_hist2(self):
        # chama o método pixel_counter e imprime um gráfico com os valores obtidos
        plt.xlabel("Intensity")
        plt.ylabel("Number")
        plt.hist(self.pixel_counter())
        plt.show()
