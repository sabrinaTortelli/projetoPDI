import cv2


def open_image(address):
    return cv2.imread("../imagens/" + address, 1)


def show_image(window_name, image):
    cv2.imshow(window_name, image)
    k = cv2.waitKey(0)
    if k == 27 or k == ord('q'):
        cv2.destroyAllWindows()


def save_image(name_image, image):
    cv2.imwrite("../imagensGeradas/" + name_image + ".jpg", image)