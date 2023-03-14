from pathlib import Path

import cv2
import pkg_resources


class ImageProcessor(object):
    def __init__(self, selected_image):
        # imread takes 2 params: image path and flag. Flag 1 reads image in colors, 0 or -1 reads image in grayscale
        self.image = cv2.imread(pkg_resources.resource_filename('images', 'SampleImages/' + selected_image), 1)

    def show_image(self, window_name):
        cv2.imshow(window_name, self.image)
        # opens image. waitKey 0 keeps image open, 0 is a value in milliseconds and cam be adjusted
        # pressing key 27(ESC) or q closes windows and runs the rest of the code
        k = cv2.waitKey(0)
        if k == 27 or k == ord('q'):
            cv2.destroyAllWindows()

    def save_image(self, image_name):
        file_name = image_name + ".jpg"
        path = str(Path("images/ResultImages/") / file_name)
        cv2.imwrite(path, self.image)

    def return_image_object(self):
        return self.image
