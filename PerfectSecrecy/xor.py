import numpy as np
import cv2

img1 = cv2.imread("flag.png")
img2 = cv2.imread("universe.png")


print(img1.shape)
print(img2.shape)
new_img = np.zeros((1079, 1920, 3))


pixel = 0

for i in range(1079):
    for j in range(1920):
        for k in range(3):
            pixel = img1[i, j, k] ^ img2[i, j, k]
            new_img[i, j, k] = pixel

cv2.imwrite("xor.png", new_img)

