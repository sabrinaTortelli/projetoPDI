import cv2
from PIL.ImageQt import rgb


class GrayPonder:
    def gray_pixel_manipulation(pixel):
        pixel[2] = pixel[2] * 0.2989  # r
        pixel[1] = pixel[1] * 0.5870  # g
        pixel[0] = pixel[1] * 0.1140  # b
        return [pixel[2], pixel[1], pixel[0]]


class GrayScale(object):
    def __init__(self, image):
        self.image = image
        self.row = self.image.shape[0]
        self.col = self.image.shape[1]

    def gray_convert_simple(self):
        for i in range(self.row):
            for j in range(self.col):
                self.image[i, j] = sum(self.image[i, j]) * 0.33
        cv2.imshow('Simple Grayscale Image', self.image)
        cv2.waitKey(0)
        return self.image

    def gray_convert_ponder(self):
        for i in range(self.row):
            for j in range(self.col):
                self.image[i, j] = sum(GrayPonder.gray_pixel_manipulation(self.image[i, j]))
        cv2.imshow('Ponder Grayscale Image', self.image)
        cv2.waitKey(0)
        return self.image
