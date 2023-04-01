# Operação de ajuste para não estourar o valor do pixel de cada canal
import cv2
import numpy as np


# Operação de ajuste de valores de uma lista de pixels rgb
# param: lista de pixels rgb
# Retorna lista de pixels rgb com valores ajustados
def fit_value(values):
    list_values = [0, 0, 0]
    for p in range(len(values)):
        if values[p] < 0:
            list_values[p] = 0
        elif values[p] > 255:
            list_values[p] = 255
        else:
            list_values[p] = values[p]
    return list_values


# Operação de ajuste de 1 valor de pixel
# param: um valor de pixel
# Retorna o valor do pixel ajustado
def fit_1_value(value):
    if value < 0:
        return 0
    elif value > 255:
        return 255
    else:
        return value


# Mostra a imagem inicial e a resultante da operação lado a lado
def show_images_by_side(name_operation, image_original, image_result):
    horizontal = np.concatenate((image_original, image_result), axis=1)
    cv2.imshow(name_operation, horizontal)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
