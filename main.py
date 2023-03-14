from image_io.image_processor import ImageProcessor as IP
from value.gray_scale import GrayScale as GS
from value.rgb_channels import Extractor as EX


if __name__ == '__main__':
    img = IP("joker.jpg")
    #img.show_image("Teste")
    #img.save_image("Test014")
    #gray_img = GS(img.return_image_object())
    #gray_img.gray_convert_simple()
    #gray_img.gray_convert_ponder()
    chan_img = EX(img.return_image_object())
    chan_img.blue_channel()












