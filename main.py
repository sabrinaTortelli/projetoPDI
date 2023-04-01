import cv2
import numpy as np

from image_io.image_processor import ImageProcessor as IP
from value.gray_scale import GrayScale as GS
from value.rgb_channels import Extractor as EX
from value.histogram import Histogram as Hs
from value.negative_image import NegativeImage as NI
from space.convolution import Convolution as CVLT
from image_io.save_image import SaveImage as SI
from space.segmentation import Segmentation as SG
from morphology.erode import Erode as ER
from morphology.dilate import Dilate as DL
from morphology.opening import Opening as OP
from morphology.closure import Closure as CL
from morphology.outer_limit import OuterLimit as OL
from morphology.inner_limit import InnerLimit as IL
from arithmetic_operations.arithmetic_operations_images import ArithmeticOperationsImages as AOI
from arithmetic_operations.arithmetic_operations_value import ArithmeticOperationsValue as AOV


def test_gray_simple_convert():
    img = IP("joker.jpg", 1)
    gray_img = GS(img.return_image_object())
    img_save = SI(gray_img.gray_convert_simple())
    img_save.save_image("gray_simple_test_joker")


def test_gray_ponder_convert():
    img = IP("joker.jpg", 1)
    gray_img = GS(img.return_image_object())
    img_save = SI(gray_img.gray_convert_ponder())
    img_save.save_image("gray_ponder_test_joker")


def test_blue_channel():
    img = IP("joker.jpg", 1)
    chan_img = EX(img.return_image_object())
    img_save = SI(chan_img.blue_channel())
    img_save.save_image("blue_channel_test_joker")


def test_red_channel():
    img = IP("joker.jpg", 1)
    chan_img = EX(img.return_image_object())
    img_save = SI(chan_img.red_channel())
    img_save.save_image("red_channel_test_joker")


def test_green_channel():
    img = IP("joker.jpg", 1)
    chan_img = EX(img.return_image_object())
    img_save = SI(chan_img.green_channel())
    img_save.save_image("green_channel_test_joker")


def test_histogram():
    img = IP("gray_image_tree.jpg", 1)
    Hs(img.return_image_object()).plot_hist()


def test_threshold():
    img = IP("joker.jpg", 1)
    gray_img = GS(img.return_image_object())
    gray_img.gray_convert_ponder()
    img_save = SI(gray_img.threshold(200))
    img_save.save_image("threshold_test_joker")


def test_negative_image():
    img = IP("joker.jpg", 1)
    negative_image = NI(img.return_image_object())
    list_img = SI(negative_image.negative_image())
    list_img.save_image("test_negative_image")
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
    # teste - outra forma de criar um kernel
    element_np = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
    # testando meu resultado com a implementação do opencv
    con_opencv = cv2.filter2D(src=img.return_image_object(), ddepth=-1, kernel=element_np)
    cv2.imshow("Teste OpenCV Convolucao", con_opencv)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


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
    # teste - outra forma de criar um kernel
    element_np = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
    # testando meu resultado com a implementação do opencv
    con_opencv = cv2.filter2D(src=img.return_image_object(), ddepth=-1, kernel=element_np)
    cv2.imshow("Teste OpenCV Convolucao", con_opencv)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


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
    # teste com imagem em tons de cinza 2 canais
    img = IP("gray_simple_test_joker.jpg", 0)
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


def test_gray_segmentation_robinson():
    img = IP("joker.jpg", 0)
    robinson_image = SG(img.return_image_object())
    transformed_img = robinson_image.robinson()
    img_save = SI(transformed_img)
    img_save.save_image("gray_segmentation_robinson_test_joker")


def test_rgb_segmentation_roberts():
    # teste com imagem em tons de cinza
    img = IP("gray_simple_test_joker.jpg", 1)
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
    transformed_img = result_image.sub_operation()
    img_save = SI(transformed_img)
    img_save.save_image("sub_operation_test_aberta_fechada")


def test_value_subtraction():
    img = IP("aberta.jpg", 1)
    value = 100
    result_image = AOV(img.return_image_object(), value)
    transformed_img = result_image.sub_operation()
    img_save = SI(transformed_img)
    img_save.save_image("sub_operation_value_test_aberta")


def test_addition():
    img = IP("aberta.jpg", 1)
    imgS = IP("fechada.jpg", 1)
    width = int(img.return_image_object().shape[1])
    height = int(img.return_image_object().shape[0])
    dim = (width, height)
    resized = cv2.resize(imgS.return_image_object(), dim)
    result_image = AOI(img.return_image_object(), resized)
    transformed_img = result_image.add_operation()
    img_save = SI(transformed_img)
    img_save.save_image("add_operation_test_aberta_fechada")


def test_value_addition():
    img = IP("aberta.jpg", 1)
    value = 80
    result_image = AOV(img.return_image_object(), value)
    transformed_img = result_image.add_operation()
    img_save = SI(transformed_img)
    img_save.save_image("add_operation_value_test_aberta")


def test_multiplication():
    img = IP("aberta.jpg", 1)
    imgS = IP("fechada.jpg", 1)
    width = int(img.return_image_object().shape[1])
    height = int(img.return_image_object().shape[0])
    dim = (width, height)
    resized = cv2.resize(imgS.return_image_object(), dim)
    result_image = AOI(img.return_image_object(), resized)
    transformed_img = result_image.mult_operation()
    img_save = SI(transformed_img)
    img_save.save_image("mult_operation_test_aberta_fechada")


def test_value_multiplication():
    img = IP("aberta.jpg", 1)
    value = 5
    result_image = AOV(img.return_image_object(), value)
    transformed_img = result_image.mult_operation()
    img_save = SI(transformed_img)
    img_save.save_image("mult_operation_value_test_aberta")


def test_division():
    img = IP("aberta.jpg", 1)
    imgS = IP("fechada.jpg", 1)
    width = int(img.return_image_object().shape[1])
    height = int(img.return_image_object().shape[0])
    dim = (width, height)
    resized = cv2.resize(imgS.return_image_object(), dim)
    result_image = AOI(img.return_image_object(), resized)
    transformed_img = result_image.div_operation()
    img_save = SI(transformed_img)
    img_save.save_image("div_operation_test_aberta_fechada")


def test_value_division():
    img = IP("aberta.jpg", 1)
    value = 5
    result_image = AOV(img.return_image_object(), value)
    transformed_img = result_image.div_operation()
    img_save = SI(transformed_img)
    img_save.save_image("div_operation_value_test_aberta")


def test_value_division_error():
    img = IP("aberta.jpg", 1)
    value = 0
    result_image = AOV(img.return_image_object(), value)
    result_image.div_operation()


def test_rgb_segmentation_robinson():
    img = IP("joker.jpg", 1)
    robinson_image = SG(img.return_image_object())
    transformed_img = robinson_image.robinson()
    img_save = SI(transformed_img)
    img_save.save_image("rgb_segmentation_robinson_test_joker")


def test_erode():
    # imagens em 1 canal
    img = IP("j.png", 0)
    kernel_5x5 = np.ones((5, 5), np.uint8)
    kernel_3x3 = np.ones((3, 3), np.uint8)
    erode = ER(img.return_image_object(), kernel_5x5)
    erode_image1 = erode.erode()
    erode = ER(img.return_image_object(), kernel_3x3)
    erode_image2 = erode.erode()
    result_erode = cv2.hconcat([img.return_image_object(), erode_image1, erode_image2])
    img_save = SI(erode_image1)
    img_save.save_image("erode_test_j_kernel_5x5")
    img_save = SI(erode_image2)
    img_save.save_image("erode_test_j_kernel_3x3")
    cv2.imshow('Erosion: Original - Result 5x5 - Result 3x3', result_erode)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def test_dilate():
    # imagens em 1 canal
    img = IP("j.png", 0)
    kernel_5x5 = np.ones((5, 5), np.uint8)
    kernel_3x3 = np.ones((3, 3), np.uint8)
    dilate = DL(img.return_image_object(), kernel_5x5)
    dilate_image1 = dilate.dilate()
    dilate = DL(img.return_image_object(), kernel_3x3)
    dilate_image2 = dilate.dilate()
    result_dilate = cv2.hconcat([img.return_image_object(), dilate_image1, dilate_image2])
    img_save = SI(dilate_image1)
    img_save.save_image("dilate_test_j_kernel_5x5")
    img_save = SI(dilate_image2)
    img_save.save_image("dilate_test_j_kernel_3x3")
    cv2.imshow('Dilate: Original - Result 5x5 - Result 3x3', result_dilate)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def test_opening():
    img = IP("j.png", 0)
    kernel_5x5 = np.ones((5, 5), np.uint8)
    open_image = OP(img.return_image_object(), kernel_5x5)
    result_image = open_image.opening()
    img_save = SI(result_image)
    img_save.save_image("opening_test_j_kernel_5x5")
    opening_cv = cv2.morphologyEx(img.return_image_object(), cv2.MORPH_OPEN, kernel_5x5)
    result_opening = cv2.hconcat([img.return_image_object(), result_image, opening_cv])
    cv2.imshow('Opening: Original - Our code - CV Code', result_opening)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def test_closing():
    img = IP("j.png", 0)
    kernel_5x5 = np.ones((5, 5), np.uint8)
    closure_image = CL(img.return_image_object(), kernel_5x5)
    result_image = closure_image.closure()
    img_save = SI(result_image)
    img_save.save_image("closure_test_j_kernel_5x5")
    closure_cv = cv2.morphologyEx(img.return_image_object(), cv2.MORPH_CLOSE, kernel_5x5)
    result_opening = cv2.hconcat([img.return_image_object(), result_image, closure_cv])
    cv2.imshow('Closure: Original - Our code - CV Code', result_opening)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def test_outer_limit():
    img = IP("j.png", 0)
    kernel_5x5 = np.ones((5, 5), np.uint8)
    outer_image = OL(img.return_image_object(), kernel_5x5)
    result_image = outer_image.outer_limit()
    img_save = SI(result_image)
    img_save.save_image("outer_limit_test_j_kernel_5x5")


def test_inner_limit():
    img = IP("j.png", 0)
    kernel_5x5 = np.ones((5, 5), np.uint8)
    inner_image = IL(img.return_image_object(), kernel_5x5)
    result_image = inner_image.inner_limit()
    img_save = SI(result_image)
    img_save.save_image("inner_limit_test_j_kernel_5x5")


if __name__ == '__main__':
    ## Testes de aritmética
    ### Imagem com imagem
    # test_subtraction()
    # test_addition()
    # test_multiplication()
    # test_division()
    ### Imagem com valor
    # test_value_subtraction()
    # test_value_addition()
    # test_value_multiplication()
    # test_value_division()
    # test_value_division_error()

    ##Testes de valor
    # test_gray_simple_convert()
    # test_gray_ponder_convert()
    # test_red_channel()
    # test_green_channel()
    # test_blue_channel()
    # test_histogram()
    # test_threshold()
    # test_negative_image()

    ## Testes de espaço

    ### Teste morfologia matemática
    # test_erode()
    # test_dilate()
    # test_opening()
    # test_closing()
    # test_outer_limit()
    # test_inner_limit()

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
    # test_gray_segmentation_roberts()
    # test_gray_segmentation_sobel()
    # test_gray_segmentation_robinson()
    ### Teste segmentação imagens rgb
    # test_rgb_segmentation_roberts()
    # test_rgb_segmentation_sobel()
    # test_rgb_segmentation_robinson()

    print("Fim Operacoes")
