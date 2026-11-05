from pathlib import Path

import cv2
import numpy as np


def var_of_picture(image_path: str, convolution_kernel: list):
    assert Path(image_path).exists(), "Path does not exist"
    assert isinstance(convolution_kernel, list) and len(convolution_kernel) == 3  

    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    result = cv2.filter2D(
    gray, cv2.CV_64F, np.array(convolution_kernel))

    return result.var()


if __name__ == "__main__":
    # aproximation of blur detection filter
    convolution_kernel = [
        [0,  1, 0],
        [1, -4, 1],
        [0,  1, 0]
    ]

    path_blurry = "data/test_images/blurry.jpg"
    path_normal = "data/test_images/normal.jpg"

    print(var_of_picture(path_blurry, convolution_kernel))
    print(var_of_picture(path_normal, convolution_kernel))


