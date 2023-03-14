import image_process.image_process as io
import cv2
def colorToGrayAuto(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


if __name__ == '__main__':
    address = "coringa.jpg"
    img = io.open_image(address)
    # img = image_process.open_image(address)
    io.show_image("Teste", img)
    # image_process.show_image("Teste", img)
    # img_transform = colorToGrayAuto(img)
    # image_process.show_image("Teste 2", img_transform)
    # image_process.save_image("teste1", img_transform)

