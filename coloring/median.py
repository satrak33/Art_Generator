import cv2

img = cv2.imread("../images/yoo.png")

img = cv2.resize(img, (0, 0), fx=2, fy=2)

cv2.imshow("Image", img)
cv2.imwrite("../images/median.png", cv2.medianBlur(img, 21))

cv2.waitKey(0)