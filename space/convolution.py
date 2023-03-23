import cv2


class Convolution(object):

    def __init__(self, image, size):
        self.image = image
        # self.row = self.image.shape[0]
        # self.col = self.image.shape[1]
        # self.mask = self.make_mask()
        self.size = size
        # print(self.mask)

    def make_mask(self):
        line = [0] * self.size
        mask = [line] * self.size
        num = 0
        for l in range(self.size):
            line = []
            for c in range(self.size):
                num = num + 1
                line.append(num)
            mask[l] = line
        print(mask)
        return mask

    def convolution_operator(self):
        print(self.row)
        print(self.col)
        # for i in range(self.row):
        #     for j in range(self.col):
        #         self.image[i, j] = sum(GrayPonder.gray_pixel_manipulation(self.image[i, j]))
        # cv2.imshow('Ponder Grayscale Image', self.image)
        # cv2.waitKey(0)
        # return self.image
