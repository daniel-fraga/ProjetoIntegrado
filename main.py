import cv2
import numpy as np
import pytesseract


def image_treatment(image):
    '''
    Receive a image and returns a treated image to use in Tesseract's OCR.
    :param: image
    :return:
    '''
    _, treated_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

    return treated_image


def main():
    # read a image, flag 0 is a gray scale image
    img = cv2.imread("./img4.jpeg", 0)
    treated_image = image_treatment(img)

    cv2.imshow("Image", treated_image)

    print(pytesseract.image_to_string(treated_image))

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == main():
    main()
