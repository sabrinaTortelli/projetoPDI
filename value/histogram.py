import matplotlib.pyplot as plt
import numpy as np


class Histogram(object):
    # recebe um objeto imagem e armazena o numero de colunas e linhas da matriz imagem
    # chama o método pixel counter para armazenar em uma lista os valores de todos os pixels de uma imagem
    def __init__(self, image):
        self.image = image
        self.row = self.image.shape[0]
        self.col = self.image.shape[1]
        self.pixels = self.pixel_counter

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
        # retorna pixel counter [ azul, verde, vermelho]
        # é uma lista de 3 listas de 256 posições
        # cada lista corresponde ao BGR da imagem e guarda a soma de cada intensidade do mesmo
        # o metodo percorre o self image para popular a lista pixel counter
        pixel_counter = [[0 for i in range(256)], [0 for i in range(256)], [0 for i in range(256)]]
        for i in range(self.row):
            for j in range(self.col):
                pixel_counter[0][self.image[i, j][0]] += 1
                pixel_counter[1][self.image[i, j][1]] += 1
                pixel_counter[2][self.image[i, j][2]] += 1
        # print ("YO")
        return pixel_counter

    def plot_hist(self):
        # chama o método pixel_counter e imprime um gráfico com os valores obtidos
        pixels = self.pixel_counter()

        x = np.array(range(256))
        blue = np.array(pixels[0])
        green = np.array(pixels[1])
        red = np.array(pixels[2])

        plt.title("Image line Graph")
        plt.xlabel("Intensity")
        plt.ylabel("Number")
        plt.plot(x, blue, color="blue")
        plt.plot(x, green, color="green")
        plt.plot(x, red, color="red")
        plt.show()

    def plot_hist2(self):
        # chama o método pixel_counter e imprime um gráfico com os valores obtidos
        plt.xlabel("Intensity")
        plt.ylabel("Number")
        plt.hist(self.pixel_counter())
        plt.show()
