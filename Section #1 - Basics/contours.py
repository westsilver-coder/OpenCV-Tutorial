# pylint:disable=no-member
import cv2 as cv
import numpy as np

# ===============================================
# [1] Load Image and Preprocess
# ===============================================
img = cv.imread('../Resources/Photos/cats.jpg')
blank = np.zeros(img.shape, dtype='uint8')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
canny = cv.Canny(blur, 125, 175)
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(blank, contours, -1, (0,0,255), 1)

# ===============================================
# [2] Create One Stable and Large Window
# ===============================================
cv.namedWindow('Viewer', cv.WINDOW_NORMAL)
cv.resizeWindow('Viewer', 1000, 700)

# ===============================================
# [3] Steps with Descriptions
# ===============================================
steps = [
    ("Original Image - Unprocessed input image of cats.", img),
    ("Blank Canvas - Black image of the same size.", blank),
    ("Grayscale - Converted to grayscale.", gray),
    ("Gaussian Blur - Smoothed to reduce noise.", blur),
    ("Canny Edge Detection - Edges highlighted in white.", canny),
    (f"Contours Drawn - {len(contours)} contour(s) outlined in red.", blank)
]

# ===============================================
# [4] Display Function
# ===============================================
def show_step(index):
    """Display current step with text overlay."""
    desc, frame = steps[index]
    display = frame.copy() if len(frame.shape) == 3 else cv.cvtColor(frame, cv.COLOR_GRAY2BGR)

    # --- Calculate bottom-center text position ---
    h, w = display.shape[:2]
    text_size, _ = cv.getTextSize(desc, cv.FONT_HERSHEY_SIMPLEX, 0.6, 2)
    text_w, text_h = text_size
    x = (w - text_w) // 2
    y = h - 20

    cv.putText(display, desc, (x, y), cv.FONT_HERSHEY_SIMPLEX,
               0.6, (255, 255, 255), 2, cv.LINE_AA)
    cv.imshow('Viewer', display)
    print(f"[{index+1}/{len(steps)}] {desc}")

# ===============================================
# [5] Manual Slide Control Loop
# ===============================================
index = 0
show_step(index)

print("Use → (Right Arrow) for next, ← (Left Arrow) for previous, 0 or ESC to exit.")

while True:
    key = cv.waitKey(0)  # Wait indefinitely for a key press

    # → next
    if key == 83 or key == ord('d'):  # right arrow or 'd'
        index = (index + 1) % len(steps)
        show_step(index)

    # ← previous
    elif key == 81 or key == ord('a'):  # left arrow or 'a'
        index = (index - 1) % len(steps)
        show_step(index)

    # 0 or ESC → exit
    elif key == ord('0') or key == 27:
        print("Exiting program...")
        break

cv.destroyAllWindows()
