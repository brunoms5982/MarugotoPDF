from pdf2image import convert_from_path
from split_image import split_image
from PIL import Image
import cv2
import pytesseract
import numpy as np
import os
directory = 'second_crop'
pdfs = r"teste.pdf"
pages = convert_from_path(pdfs, 350)
array = []
anki = {}
i = 1
for page in pages:
    if i==3:
        break
    image_name = "pages/Page_" + str(i) + ".jpg"  
    page.save(image_name, "JPEG")
    image = cv2.imread(f"pages/Page_{i}.jpg")
    print(f"Page_{i}.jpg")
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    t_img = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    if i == 1:
        cropImg = t_img[500:t_img.shape[0]-155, 0:t_img.shape[1]] #para 1 página
        cv2.imwrite(f"first_crop/t{i}.jpg", cropImg)
        split_image(f"first_crop/t{i}.jpg", 11, 2, False, False, True, "second_crop")
    else:
        cropImg = t_img[80:t_img.shape[0]-155, 0:t_img.shape[1]] #para outras
        cv2.imwrite(f"first_crop/t{i}.jpg", cropImg)
        split_image(f"first_crop/t{i}.jpg", 12, 2, False, False, True, "second_crop")
    i = i+1

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        details = pytesseract.image_to_string(Image.open(f), lang="eng+jpn")
        array.append(details)

for i in range (int(len(array))/2):
    anki[array[i]] = array[i+1]
    