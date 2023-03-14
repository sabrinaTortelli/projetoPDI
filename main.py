from image_io.image_processor import ImageProcessor as IP


if __name__ == '__main__':
    img = IP("joker.jpg")
    img.show_image("Teste")
    img.save_image("Test014")






