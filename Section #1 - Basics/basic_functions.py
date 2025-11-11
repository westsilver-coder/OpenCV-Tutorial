# pylint:disable=no-member
import cv2 as cv

# ===============================================
# [0] Ask User Before Starting
# ===============================================
answer = input("Do you want to display the image? (Y/N): ").strip().lower()

if answer == 'n':
    print("Exiting program...")
    exit()
elif answer != 'y':
    print("Invalid input. Please restart and enter Y or N.")
    exit()

print("Displaying the original image...")

# ===============================================
# [1] Load the Original Image
# ===============================================
img = cv.imread('../Resources/Photos/park.jpg')

# ===============================================
# [2] Precompute All Processed Variants
# ===============================================
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
canny = cv.Canny(blur, 125, 175)
dilated = cv.dilate(canny, (7,7), iterations=3)
eroded = cv.erode(dilated, (7,7), iterations=3)
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cropped = img[50:200, 200:400]

# ===============================================
# [3] Key-to-Image Mapping
# ===============================================
images = {
    ord('p'): ('Park', img),
    ord('g'): ('Gray', gray),
    ord('b'): ('Blur', blur),
    ord('c'): ('Canny', canny),
    ord('d'): ('Dilated', dilated),
    ord('e'): ('Eroded', eroded),
    ord('r'): ('Resized', resized),
    ord('x'): ('Cropped', cropped)
}

print("🔹 OpenCV window must be active for key detection!")
print("   p=Park, g=Gray, b=Blur, c=Canny, d=Dilated, e=Eroded, r=Resized, x=Cropped, 0=Exit")

# ===============================================
# [4] Main Loop — Wait for Key in OpenCV Window
# ===============================================
cv.namedWindow('Image Viewer')

current_title = 'Park'
cv.imshow(current_title, img)

while True:
    key = cv.waitKey(0)  # Wait for key press (only works in OpenCV window)

    # If '0' or ESC is pressed, exit the program
    if key == ord('0') or key == 27:
        print("Exiting program...")
        break

    # If the key matches one of the image mappings
    elif key in images:
        title, img_to_show = images[key]

        # Close all previous windows before showing the new one
        cv.destroyAllWindows()

        # Show the new image in the same window
        cv.imshow(title, img_to_show)
        current_title = title
        print(f"Displaying {title}...")

    # If key is undefined
    else:
        print("⚠️ Invalid key. Please press one of the defined keys.")

# ===============================================
# [5] Clean Up — Close All Windows
# ===============================================
cv.destroyAllWindows()

# ===============================================
# Changes from original version
# ===============================================
# (1) Added a startup prompt asking the user "Do you want to display the image? (Y/N)".
# (2) If 'Y' is entered, the program continues to the image viewer.
# (3) If 'N' or invalid input is entered, the program exits immediately.
# (4) The rest of the code remains the same: key-controlled display logic with one active window.
# (5) Maintained all original section structure and comment style for consistency.
