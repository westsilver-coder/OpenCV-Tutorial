# pylint:disable=no-member

import cv2 as cv
import numpy as np

# ------------------------------------------------------------
# Load the original image
# ------------------------------------------------------------
img = cv.imread('../Resources/Photos/park.jpg')
cv.imshow('Original', img)

# This variable keeps track of the current output image.
current_img = img.copy()


# ------------------------------------------------------------
# Translation Function
# Moves the image horizontally (x) and vertically (y).
# Positive x → right, negative x → left
# Positive y → down, negative y → up
# ------------------------------------------------------------
def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])  # Translation matrix
    dimensions = (img.shape[1], img.shape[0])      # (width, height)
    return cv.warpAffine(img, transMat, dimensions)


# ------------------------------------------------------------
# Rotation Function
# Rotates the image by a given angle around a rotation point.
# If no rotation point is given, the image center is used.
# Negative angle → clockwise rotation
# Positive angle → counterclockwise rotation
# ------------------------------------------------------------
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width // 2, height // 2)       # Rotate around image center
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)


# ------------------------------------------------------------
# Interactive Transformation Loop
# User presses keys to perform transformations:
# T → Translate
# R → Rotate
# S → Resize (square size)
# F → Flip (0, 1, -1 only)
# C → Crop
# Any other key → exit program
# ------------------------------------------------------------
while True:
    key = cv.waitKey(0)

    # ---------------------------
    # 1. Translation (T)
    # ---------------------------
    if key == ord('t') or key == ord('T'):
        print("Translation selected.")
        current_img = translate(img, -100, 100)    # Example translation
        cv.imshow('Result', current_img)

    # ---------------------------
    # 2. Rotation (R)
    # ---------------------------
    elif key == ord('r') or key == ord('R'):
        print("Rotation selected.")
        angle = input("Enter rotation angle (e.g., -45): ")

        try:
            angle = float(angle)
            current_img = rotate(img, angle)
            cv.imshow('Result', current_img)
        except:
            print("Invalid angle. No changes applied.")

    # ---------------------------
    # 3. Resizing (S) — Square resize
    # ---------------------------
    elif key == ord('s') or key == ord('S'):
        print("Resize selected.")
        size = input("Enter new square size (e.g., 500): ")

        try:
            size = int(size)
            current_img = cv.resize(img, (size, size), interpolation=cv.INTER_CUBIC)
            cv.imshow('Result', current_img)
        except:
            print("Invalid size. No changes applied.")

    # ---------------------------
    # 4. Flipping (F)
    # Acceptable values: 0 (vertical), 1 (horizontal), -1 (both)
    # ---------------------------
    elif key == ord('f') or key == ord('F'):
        print("Flip selected.")
        mode = input("Enter flip mode (0, 1, -1): ")

        if mode in ['0', '1', '-1']:
            current_img = cv.flip(img, int(mode))
            cv.imshow('Result', current_img)
        else:
            print("Invalid flip mode. Must be 0, 1, or -1. Keeping previous image.")

    # ---------------------------
    # 5. Cropping (C)
    # Crops a manually chosen region of the original image.
    # ---------------------------
    elif key == ord('c') or key == ord('C'):
        print("Cropping selected.")
        cropped = img[200:400, 300:400]  # Example crop
        current_img = cropped
        cv.imshow('Result', current_img)

    # ---------------------------
    # Any other key → Exit program
    # ---------------------------
    else:
        print("Exiting program. All windows will close.")
        break


# ------------------------------------------------------------
# Close all OpenCV windows
# ------------------------------------------------------------
cv.destroyAllWindows()
