"""
This is a tool for generating a dataset for hand-drawn image classification.

Create a folder called "dataset_python" in your working directory.
You can later combine your images with the drawings from the "dataset_combined" folder.

In the console you will see the animal that you need to draw.
Please draw one entire animal per image.
Do not draw parts only (e.g. the head) and do not draw multiple animals in one image.

Press ENTER to draw the next animal.
Press "q" to quit the application.
Press "b" to clear the image and to restart painting.
Press "c" to skip the current animal and jump to the next one.
"""

import os
import uuid
import numpy as np
import cv2 as cv


dataset_dir = r"dataset_python"
classes = ["cat", "dog", "bird", "turtle", "elephant"]
image_size = 600
stroke_size = 6 # drawing stroke size in pixels

# temp variables for drawing
pressed = False
x_pos, y_pos = 0, 0


def draw_on_image(event, x, y, flags, param):
    global pressed, x_pos, y_pos
    
    if event == cv.EVENT_LBUTTONDOWN:
        pressed = True
        x_pos, y_pos = x, y
    elif event == cv.EVENT_LBUTTONUP:
        pressed = False
    elif event == cv.EVENT_MOUSEMOVE:
        if pressed:
            cv.line(img, (x_pos, y_pos), (x, y), 0, stroke_size, cv.LINE_AA)
            x_pos, y_pos = x, y
            cv.imshow("draw", img)


cv.namedWindow("draw")
cv.setMouseCallback("draw", draw_on_image)

img = np.zeros((image_size, image_size), np.uint8)

current_index = 0
while True:
    print(classes[current_index], "\n")
    img[:] = 255
    cv.imshow("draw", img)
    
    key = cv.waitKey()
    if key == ord("q"):
        cv.destroyAllWindows()
        break
    elif key == ord("b"):
        continue
    elif key == ord("c"):
        current_index = current_index + 1 if current_index < len(classes) - 1 else 0
        continue

    if (img[:] == 255).all():
        continue

    img_name = classes[current_index] + "_team0_" + str(uuid.uuid4())
    cv.imwrite(dataset_dir + os.sep + img_name + ".png", img)
    current_index = current_index + 1 if current_index < len(classes)-1 else 0