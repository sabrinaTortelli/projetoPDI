from image_io.image_processor import ImageProcessor as IP
from value.gray_scale import GrayScale as GS


if __name__ == '__main__':
    img = IP("joker.jpg")
    #img.show_image("Teste")
    #img.save_image("Test014")
    gray_img = GS(img.return_image_object())
    gray_img.gray_convert_simple()
    gray_img.gray_convert_ponder()











