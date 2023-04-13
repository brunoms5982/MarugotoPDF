# importing modules

import cv2

import pytesseract

# reading image using opencv

image = cv2.imread("Page_1.jpg")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

threshold_img = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
#cv2.imshow("threshold image", threshold_img)
cv2.imwrite("t.jpg", threshold_img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

custom_config = r'--oem 3 --psm 6'


details = pytesseract.image_to_data(threshold_img ,config=custom_config, lang="eng+jpn")
print(details)