from pathlib import Path

import cv2
import pkg_resources


class ImageProcessor(object):
    def __init__(self, selected_image):
        # imread leva 2 params: image path e flag. Flag 1 le a imagem colorida, 0 ou -1 le a imagem em tons de cinza
        # pkg_resources.resource_filename leva o nome do package e o path dentro do package para ler arquivos
        self.image = cv2.imread(pkg_resources.resource_filename('images', 'SampleImages/' + selected_image), 1)

    def show_image(self, window_name):
        # mostra a imagem. waitKey 0 mantem a imagem aberta, 0 é um valor em milisec e pode ser ajustado
        # apertar key 27(ESC) ou q fecha a janela e permite que o programa volte a rodar
        cv2.imshow(window_name, self.image)
        k = cv2.waitKey(0)
        if k == 27 or k == ord('q'):
            cv2.destroyAllWindows()

    def save_image(self, image_name):
        # recebe um nome para a imagem, concatena a terminção e salva a imagem no path indicado
        # o Path especifica o path no fomato / forward slash e resolve o caminho no SO que está rodando
        file_name = image_name + ".jpg"
        path = str(Path("images/ResultImages/") / file_name)
        cv2.imwrite(path, self.image)

    def return_image_object(self):
        #retorna a matriz de pixels
        return self.image
