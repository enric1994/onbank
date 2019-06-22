import numpy as np
import cv2


def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]
    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))
    resized = cv2.resize(image, dim, interpolation = inter)
    return resized

def generate():
    image = cv2.imread('/code/src/static/img/face.png')
    # output = image_resize(image, width = 400)

    id_layout = cv2.imread('/code/src/static/img/id_layout.jpg')
    id_layout = cv2.resize(id_layout, (1000,800))

    s_img = image
    l_img = id_layout
    x_offset,y_offset=300, 120
    l_img[y_offset:y_offset+480, x_offset:x_offset+640] = s_img
    cv2.imwrite("id.png", l_img)