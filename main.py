from image_io.image_processor import ImageProcessor as IP
from value.gray_scale import GrayScale as GS
from value.rgb_channels import Extractor as EX
from value.histogram import Histogram as Hs
from value.negative_image import NegativeImage as NI


if __name__ == '__main__':
    img = IP("joker.jpg")
    #img = IP("dog.jpg")
    #img.show_image("Teste")
    #img.save_image("Test014")
    #gray_img = GS(img.return_image_object())
    #gray_img.gray_convert_simple()
    #gray_img.gray_convert_ponder()


    #chan_img = EX(img.return_image_object())
    #chan_img.blue_channel()
    #Hs(img.return_image_object()).plot_hist()
    #gray_img.threshold(200)
    negative_image = NI(img.return_image_object())
    negative_image.negative_image()

    print("YO")












