import cv2

from image_io.image_processor import ImageProcessor as IP
from value.gray_scale import GrayScale as GS
from value.rgb_channels import Extractor as EX
from value.histogram import Histogram as Hs
from value.negative_image import NegativeImage as NI
from space.convolution import Convolution as CVLT
from image_io.save_image import SaveImage as SI
from space.segmentation import Segmentation as SG

from arithmetic_operations.arithmetic_operations_images import ArithmeticOperationsImages as AOI


def test_gray_simple_convert():
    img = IP("joker.jpg", 1)
    gray_img = GS(img.return_image_object())
    transformed_img = gray_img.gray_convert_simple()
    img_save = SI(transformed_img)
    img_save.save_image("gray_simple_test_joker")


def test_gray_ponder_convert():
    img = IP("joker.jpg", 1)
    gray_img = GS(img.return_image_object())
    transformed_img = gray_img.gray_convert_ponder()
    img_save = SI(transformed_img)
    img_save.save_image("gray_ponder_test_joker")


def test_blue_channel():
    img = IP("joker.jpg", 1)
    chan_img = EX(img.return_image_object())
    transformed_img = chan_img.blue_channel()
    img_save = SI(transformed_img)
    img_save.save_image("blue_channel_test_joker")


def test_red_channel():
    img = IP("joker.jpg", 1)
    chan_img = EX(img.return_image_object())
    transformed_img = chan_img.red_channel()
    img_save = SI(transformed_img)
    img_save.save_image("red_channel_test_joker")


def test_green_channel():
    img = IP("joker.jpg", 1)
    chan_img = EX(img.return_image_object())
    transformed_img = chan_img.green_channel()
    img_save = SI(transformed_img)
    img_save.save_image("green_channel_test_joker")


def test_histogram():
    img = IP("joker.jpg", 1)
    Hs(img.return_image_object()).plot_hist()


def test_threshold():
    img = IP("joker.jpg", 1)
    gray_img = GS(img.return_image_object())
    gray_img.gray_convert_ponder()
    transformed_img = gray_img.threshold(200)
    img_save = SI(transformed_img)
    img_save.save_image("threshold_test_joker")


def test_negative_image():
    img = IP("joker.jpg", 1)
    negative_image = NI(img.return_image_object())
    list_img = negative_image.negative_image()
    s = SI(list_img)
    s.save_image("test_negative_image")
    print(list_img)


def test_save_image(image):
    # teste para salvar a imagem que foi processada
    image_teste = SI(image)
    image_teste.save_image("dog-gray")


def test_gray_convolution_mask():
    mask = [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]
    img = IP("joker.jpg", 0)
    convolution_img = CVLT(img.return_image_object(), mask)
    transformed_img = convolution_img.convolution()
    img_save = SI(transformed_img)
    img_save.save_image("gray_convolution_test_joker")


def test_gray_convolution_mask_laplace():
    mask = [[0, -1, 0], [-1, 4, -1], [0, -1, 0]]
    img = IP("joker.jpg", 0)
    convolution_img = CVLT(img.return_image_object(), mask)
    transformed_img = convolution_img.convolution()
    img_save = SI(transformed_img)
    img_save.save_image("gray_convolution_laplace_test_joker")


def test_gray_convolution_mask_agucar():
    mask = [[0, 0, 0, 0, 0], [0, 0, -1, 0, 0], [0, -1, 5, -1, 0], [0, 0, -1, 0, 0], [0, 0, 0, 0, 0]]
    img = IP("joker.jpg", 0)
    convolution_img = CVLT(img.return_image_object(), mask)
    transformed_img = convolution_img.convolution()
    img_save = SI(transformed_img)
    img_save.save_image("gray_convolution_agucar_test_joker")


def test_gray_convolution_mask_desfocar():
    mask = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    img = IP("joker.jpg", 0)
    convolution_img = CVLT(img.return_image_object(), mask)
    transformed_img = convolution_img.convolution()
    img_save = SI(transformed_img)
    img_save.save_image("gray_convolution_desfocar_test_joker")


def test_gray_convolution_mask_realcar_bordas():
    mask = [[0, 0, 0], [-1, 1, 0], [0, 0, 0]]
    img = IP("joker.jpg", 0)
    convolution_img = CVLT(img.return_image_object(), mask)
    transformed_img = convolution_img.convolution()
    img_save = SI(transformed_img)
    img_save.save_image("gray_convolution_realcar_bordas_test_joker")


def test_gray_convolution_mask_detectar_bordas():
    mask = [[0, 1, 0], [1, -4, 1], [0, 1, 0]]
    img = IP("joker.jpg", 0)
    convolution_img = CVLT(img.return_image_object(), mask)
    transformed_img = convolution_img.convolution()
    img_save = SI(transformed_img)
    img_save.save_image("gray_convolution_detectar_bordas_test_joker")


def test_gray_convolution_mask_detectar_relevos():
    mask = [[-2, -1, 0], [-1, 1, 1], [0, 1, 2]]
    img = IP("joker.jpg", 0)
    convolution_img = CVLT(img.return_image_object(), mask)
    transformed_img = convolution_img.convolution()
    img_save = SI(transformed_img)
    img_save.save_image("gray_convolution_detectar_relevos_test_joker")


def test_rgb_convolution_mask():
    mask = [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]
    img = IP("simpsons.jpg", 1)
    half = cv2.resize(img.return_image_object(), (0, 0), fx=0.5, fy=0.5)
    convolution_img = CVLT(half, mask)
    transformed_img = convolution_img.convolution()
    img_save = SI(transformed_img)
    img_save.save_image("rgb_convolution_test_simpsons")


def test_rgb_convolution_mask_laplace():
    mask = [[0, -1, 0], [-1, 4, -1], [0, -1, 0]]
    img = IP("joker.jpg", 1)
    convolution_img = CVLT(img.return_image_object(), mask)
    transformed_img = convolution_img.convolution()
    img_save = SI(transformed_img)
    img_save.save_image("rgb_convolution_laplace_test_joker")


def test_rgb_convolution_mask_agucar():
    mask = [[0, 0, 0, 0, 0], [0, 0, -1, 0, 0], [0, -1, 5, -1, 0], [0, 0, -1, 0, 0], [0, 0, 0, 0, 0]]
    img = IP("simpsons.jpg", 1)
    half = cv2.resize(img.return_image_object(), (0, 0), fx=0.5, fy=0.5)
    convolution_img = CVLT(half, mask)
    transformed_img = convolution_img.convolution()
    img_save = SI(transformed_img)
    img_save.save_image("rgb_convolution_agucar_test_simpsons")


def test_rgb_convolution_mask_desfocar():
    mask = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    img = IP("joker.jpg", 1)
    convolution_img = CVLT(img.return_image_object(), mask)
    transformed_img = convolution_img.convolution()
    img_save = SI(transformed_img)
    img_save.save_image("rgb_convolution_realcar_bordas_test_joker")


def test_rgb_convolution_mask_realcar_bordas():
    mask = [[0, 0, 0], [-1, 1, 0], [0, 0, 0]]
    img = IP("simpsons.jpg", 1)
    half = cv2.resize(img.return_image_object(), (0, 0), fx=0.5, fy=0.5)
    convolution_img = CVLT(half, mask)
    transformed_img = convolution_img.convolution()
    img_save = SI(transformed_img)
    img_save.save_image("rgb_convolution_realcar_bordas_test_simpsons")


def test_rgb_convolution_mask_detectar_bordas():
    mask = [[0, 1, 0], [1, -4, 1], [0, 1, 0]]
    img = IP("joker.jpg", 1)
    convolution_img = CVLT(img.return_image_object(), mask)
    transformed_img = convolution_img.convolution()
    img_save = SI(transformed_img)
    img_save.save_image("rgb_convolution_detectar_bordas_test_joker")


def test_rgb_convolution_mask_detectar_relevos():
    mask = [[-2, -1, 0], [-1, 1, 1], [0, 1, 2]]
    img = IP("simpsons.jpg", 1)
    half = cv2.resize(img.return_image_object(), (0, 0), fx=0.5, fy=0.5)
    convolution_img = CVLT(half, mask)
    transformed_img = convolution_img.convolution()
    img_save = SI(transformed_img)
    img_save.save_image("rgb_convolution_detectar_relevos_test_simpsons")


def test_gray_segmentation_roberts():
    img = IP("joker.jpg", 0)
    roberts_image = SG(img.return_image_object())
    transformed_img = roberts_image.roberts()
    img_save = SI(transformed_img)
    img_save.save_image("gray_segmentation_roberts_test_joker")


def test_gray_segmentation_sobel():
    img = IP("joker.jpg", 0)
    sobel_image = SG(img.return_image_object())
    transformed_img = sobel_image.sobel()
    img_save = SI(transformed_img)
    img_save.save_image("gray_segmentation_sobel_test_joker")


def test_rgb_segmentation_roberts():
    img = IP("joker.jpg", 1)
    roberts_image = SG(img.return_image_object())
    transformed_img = roberts_image.roberts()
    img_save = SI(transformed_img)
    img_save.save_image("rgb_segmentation_roberts_test_joker")


def test_rgb_segmentation_sobel():
    img = IP("joker.jpg", 1)
    sobel_image = SG(img.return_image_object())
    transformed_img = sobel_image.sobel()
    img_save = SI(transformed_img)
    img_save.save_image("rgb_segmentation_sobel_test_joker")

def test_subtraction():
    img = IP("aberta.jpg", 1)
    imgS = IP("fechada.jpg", 1)
    width = int(img.return_image_object().shape[1])
    height = int(img.return_image_object().shape[0])
    dim = (width, height)
    resized = cv2.resize(imgS.return_image_object(), dim)
    result_image = AOI(img.return_image_object(), resized)
    result_image.sub_operation()

def test_addition():
    img = IP("aberta.jpg", 1)
    imgS = IP("fechada.jpg", 1)
    width = int(img.return_image_object().shape[1])
    height = int(img.return_image_object().shape[0])
    dim = (width, height)
    resized = cv2.resize(imgS.return_image_object(), dim)
    result_image = AOI(img.return_image_object(), resized)
    result_image.add_operation()

def test_multiplication():
    img = IP("aberta.jpg", 1)
    imgS = IP("fechada.jpg", 1)
    width = int(img.return_image_object().shape[1])
    height = int(img.return_image_object().shape[0])
    dim = (width, height)
    resized = cv2.resize(imgS.return_image_object(), dim)
    result_image = AOI(img.return_image_object(), resized)
    result_image.mult_operation()

def test_division():
    img = IP("aberta.jpg", 1)
    imgS = IP("fechada.jpg", 1)
    width = int(img.return_image_object().shape[1])
    height = int(img.return_image_object().shape[0])
    dim = (width, height)
    resized = cv2.resize(imgS.return_image_object(), dim)
    result_image = AOI(img.return_image_object(), resized)
    result_image.div_operation()

if __name__ == '__main__':
    ### Testes de aritmética
    # test_subtraction()
    # test_addition()
    # test_multiplication()
    # test_division()

    ##Testes de valor
    # test_gray_simple_convert()
    # test_gray_ponder_convert()
    # test_red_channel()
    # test_green_channel()
    # test_blue_channel()
    # test_histogram()
    # test_threshold()
    test_negative_image()

    ## Testes de espaço

    ### Teste convolução imagens tons de cinza
    # test_gray_convolution_mask()
    # test_gray_convolution_mask_laplace()
    # test_gray_convolution_mask_agucar()
    # test_gray_convolution_mask_desfocar()
    # test_gray_convolution_mask_realcar_bordas()
    # test_gray_convolution_mask_detectar_bordas()
    # test_gray_convolution_mask_detectar_relevos()

    ### Teste convolução imagens rgb
    # test_rgb_convolution_mask()
    # test_rgb_convolution_mask_laplace()
    # test_rgb_convolution_mask_agucar()
    # test_rgb_convolution_mask_desfocar()
    # test_rgb_convolution_mask_realcar_bordas()
    # test_rgb_convolution_mask_detectar_bordas()
    # test_rgb_convolution_mask_detectar_relevos()

    ### Teste segmentação imagens gray
    #test_gray_segmentation_roberts()
    # test_gray_segmentation_sobel()
    # test_rgb_segmentation_roberts()
    # test_rgb_segmentation_sobel()

    print("YO")
