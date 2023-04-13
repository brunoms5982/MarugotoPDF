# import the necessary packages
from pytesseract import Output
import pytesseract
import argparse
from split_image import split_image
import cv2
import numpy as np
# construct the argument parser and parse the arguments
split_image(f"t1.jpg", 1, 2, False, False, True)
image1 = cv2.imread("t1_0.jpg")
image = image1.resize((image1.size[0] * 5, image1.size[1] * 5))
rgb1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
rgb2 = cv2.threshold(rgb1,0,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)[1]
kernel = np.ones((5, 5), np.uint8)
rgb = cv2.medianBlur(rgb2, 5)
results = pytesseract.image_to_data(rgb, output_type=Output.DICT, lang="eng+jpn")

# loop over each of the individual text localizations
for i in range(0, len(results["text"])):
	# extract the bounding box coordinates of the text region from
	# the current result
	x = results["left"][i]
	y = results["top"][i]
	w = results["width"][i]
	h = results["height"][i]
	# extract the OCR text itself along with the confidence of the
	# text localization
	text = results["text"][i]
	conf = int(results["conf"][i])
    # filter out weak confidence text localizations
	if conf > 50:
		# display the confidence and text to our terminal
		print("Confidence: {}".format(conf))
		print("Text: {}".format(text))
		print("")
		# strip out non-ASCII text so we can draw the text on the image
		# using OpenCV, then draw a bounding box around the text along
		# with the text itself
		text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
		cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
		cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,1.2, (0, 0, 255), 3)
# show the output image

cv2.imwrite(f"image.jpg", image)
