import cv2

img = cv2.imread('Real Time Face Recognition using KNN\gina.jpg')
gray = cv2.imread('Real Time Face Recognition using KNN\gina.jpg', cv2.IMREAD_GRAYSCALE)

cv2.imshow("Gina", img)
cv2.imshow("Gray Gina", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()