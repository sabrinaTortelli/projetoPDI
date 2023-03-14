import cv2


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    img = cv2.imread("D:/Pictures/DISW4155.JPG", 1)
    cv2.imshow('Teste Imagem', img)
    k = cv2.waitKey(0)
    if k == 27 or k == ord('q'):
        cv2.destroyAllWindows()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('Comida.jpg', gray)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
