import cv2 as cv
import numpy as np

# -----------------------------
# 1. Create a mint-choco checkered background
# -----------------------------
height, width = 500, 500
blank = np.zeros((height, width, 3), dtype='uint8')

# Mint & Choco (realistic palette)
mint  = (209, 240, 170)
choco = (55, 78, 111)
tile = 50

for y in range(0, height, tile):
    for x in range(0, width, tile):
        if ((x // tile + y // tile) % 2 == 0):
            blank[y:y+tile, x:x+tile] = mint
        else:
            blank[y:y+tile, x:x+tile] = choco

# -----------------------------
# 2. Draw ellipse
# -----------------------------
center = (width // 2, height // 2)
axes = (180, 70)
cx, cy = center
ry = axes[1]

ellipse_top = cy - ry
ellipse_bottom = cy + ry

cv.ellipse(blank, center, axes, 0, 0, 360, (255, 255, 255), thickness=-1)
cv.ellipse(blank, center, axes, 0, 0, 360, (0, 0, 0), thickness=4)

# -----------------------------
# 3. Perfectly centered 3-line patterns (top & bottom)
# -----------------------------
thin = 2
thick = 8
gap = 6     # spacing between lines

# Calculate midpoints
y_mid_top = ellipse_top // 2
y_mid_bottom = (ellipse_bottom + height) // 2

def draw_three_lines(y_mid):
    # thin - thick - thin centered around midpoint
    y1 = y_mid - (gap + thick//2)   # thin line above
    y2 = y_mid                      # thick line center
    y3 = y_mid + (gap + thick//2)   # thin line below

    cv.line(blank, (0, y1), (width, y1), (255,255,255), thin)
    cv.line(blank, (0, y2), (width, y2), (255,255,255), thick)
    cv.line(blank, (0, y3), (width, y3), (255,255,255), thin)

# Draw above and below
draw_three_lines(y_mid_top)
draw_three_lines(y_mid_bottom)

# -----------------------------
# 4. Text inside ellipse
# -----------------------------
text = "Hello I'm Seoeun"
font = cv.FONT_HERSHEY_SIMPLEX
scale = 1.1
thickness = 2
(text_w, text_h), baseline = cv.getTextSize(text, font, scale, thickness)

text_x = cx - text_w // 2
text_y = cy + text_h // 2

cv.putText(blank, text, (text_x, text_y), font, scale, (0, 0, 0), thickness)

# -----------------------------
# Display
# -----------------------------
cv.imshow("Mint Choco Output", blank)
cv.waitKey(0)
cv.destroyAllWindows()
