from pathlib import Path

import cv2
import pkg_resources


class ImageProcessor(object):
    def __init__(self, selected_image):
        self.image = cv2.imread(pkg_resources.resource_filename('images', 'SampleImages/' + selected_image), 1)

    def show_image(self, window_name):
        cv2.imshow(window_name, self.image)
        k = cv2.waitKey(0)
        if k == 10 or k == ord('q'):
            cv2.destroyAllWindows()

    def save_image(self, image_name):
        file_name = image_name + ".jpg"
        path = str(Path("images/ResultImages/")/file_name)
        cv2.imwrite(path, self.image)
