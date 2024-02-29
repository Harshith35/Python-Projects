import cv2
import os

def show(title,image):
    cv2.imshow(title, image)
    cv2.waitKey(0)

image = cv2.imread("./Images/Original/Dog.jpg")
# show("Dog", image)

# Converting original image to grayscale image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# show("New Dog", gray_image)

# Invert the new grayscale image
inverted_image = 255 - gray_image
# show("Inverted", inverted_image)

# Blur the image by using the Gaussian Function
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
# show("Inverted", blurred)

# Final step is to invert the blurred image
inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)

cv2.imshow("Original image",image)
cv2.imshow("Pencil sketch", pencil_sketch)
cv2.waitKey(0)

os.chdir("./Images/Sketch")
cv2.imwrite("Dog-Sketch.jpg",pencil_sketch)