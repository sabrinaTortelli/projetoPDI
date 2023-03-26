from pathlib import Path

import cv2


class SaveImage(object):
    def __init__(self, selected_image):
        self.image = selected_image

    def save_image(self, image_name):
        # recebe um nome para a imagem, concatena a terminação e salva a imagem no path indicado
        # o Path especifica o path no formato / forward slash e resolve o caminho no SO que está rodando
        file_name = image_name + ".jpg"
        path = str(Path("images/ResultImages/") / file_name)
        cv2.imwrite(path, self.image)

    def return_image_object(self):
        # retorna a matriz de pixels
        return self.image