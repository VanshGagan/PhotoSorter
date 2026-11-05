import cv2
import numpy as np

blurry_image = cv2.imread("data/test_images/blurry.jpg")
normal_image = cv2.imread("data/test_images/normal.jpg")

# make the picture gray to use convolution
blurry_gray = cv2.cvtColor(blurry_image, cv2.COLOR_BGR2GRAY)
normal_gray = cv2.cvtColor(normal_image, cv2.COLOR_BGR2GRAY)


# aproximation of blur detection filter
convolution_kernel = [
    [0,  1, 0],
    [1, -4, 1],
    [0,  1, 0]
]

result_blurry = cv2.filter2D(
    blurry_gray, cv2.CV_64F, np.array(convolution_kernel)
)

result_normal = cv2.filter2D(
    normal_gray, cv2.CV_64F, np.array(convolution_kernel)
)

print(result_blurry.var())
print(result_normal.var())