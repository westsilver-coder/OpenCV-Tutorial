# pylint:disable=no-member
import cv2 as cv
import numpy as np

# ---------------------------------------
# Shape Generation Functions
# ---------------------------------------
def create_blank():
    return np.zeros((500, 500, 3), dtype="uint8")

def triangle_image():
    img = create_blank()
    pts = np.array([[250, 50], [50, 400], [450, 400]], np.int32)
    cv.fillPoly(img, [pts], (0, 0, 255))
    return img

def rectangle_image():
    img = create_blank()
    cv.rectangle(img, (80, 80), (420, 420), (255, 0, 0), -1)
    return img

def circle_image():
    img = create_blank()
    cv.circle(img, (250, 250), 170, (0, 255, 0), -1)
    return img

# ---------------------------------------
# Color Inversion
# ---------------------------------------
def complement(img):
    return 255 - img

# ---------------------------------------
# Masks & Coloring Output
# ---------------------------------------
def to_mask(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    _, mask = cv.threshold(gray, 1, 255, cv.THRESH_BINARY)
    return mask

def color_AND(mask):
    out = np.zeros((500, 500, 3), dtype="uint8")
    out[mask == 255] = (255, 255, 255)
    return out

def color_OR(mask):
    out = np.zeros((500, 500, 3), dtype="uint8")
    out[mask == 255] = (0, 255, 255)
    return out

def color_XOR(mask):
    out = np.zeros((500, 500, 3), dtype="uint8")
    out[mask == 255] = (255, 255, 255)
    return out

# ---------------------------------------
# Shape Function Table
# ---------------------------------------
shapes = {
    1: ("Triangle", triangle_image),
    2: ("Rectangle", rectangle_image),
    3: ("Circle", circle_image)
}

operations = {1: "AND", 2: "OR", 3: "XOR", 4: "NOT"}

# ---------------------------------------
# Main Loop
# ---------------------------------------
print("=== Shape Boolean Operation Program ===")
print("Press ESC anytime to exit.\n")

while True:
    print("Select a shape to display:")
    print("1. Triangle (Red)")
    print("2. Rectangle (Blue)")
    print("3. Circle (Green)")
    print("4. Exit")

    choice = input("Enter choice: ")
    if choice == "4":
        break
    if choice not in ["1", "2", "3"]:
        print("Invalid choice\n")
        continue

    s1 = int(choice)
    name1, func1 = shapes[s1]
    img1 = func1()

    cv.imshow(name1, img1)
    print("Press any key on the image window to continue...")
    key = cv.waitKey(0)
    cv.destroyAllWindows()

    print("\nSelect Operation:")
    print("1. AND")
    print("2. OR")
    print("3. XOR")
    print("4. NOT")

    op = input("Enter operation: ")
    if op not in ["1", "2", "3", "4"]:
        print("Invalid operation\n")
        continue
    op = int(op)

    # NOT
    if op == 4:
        result = complement(img1)
        cv.imshow("NOT Result", result)
        print("Press any key on image window...")
        cv.waitKey(0)
        cv.destroyAllWindows()
        continue

    # AND / OR / XOR needs second shape
    print("\nSelect second shape:")
    print("1. Triangle")
    print("2. Rectangle")
    print("3. Circle")

    choice2 = input("Enter shape: ")
    if choice2 not in ["1", "2", "3"]:
        print("Invalid choice\n")
        continue

    s2 = int(choice2)
    name2, func2 = shapes[s2]
    img2 = func2()

    mask1 = to_mask(img1)
    mask2 = to_mask(img2)

    if op == 1:  # AND
        out = cv.bitwise_and(mask1, mask2)
        result = color_AND(out)

    elif op == 2:  # OR
        out = cv.bitwise_or(mask1, mask2)
        result = color_OR(out)

    elif op == 3:  # XOR
        out = cv.bitwise_xor(mask1, mask2)
        result = color_XOR(out)

    cv.imshow(f"{operations[op]} Result", result)
    print("Press any key on image window...")
    cv.waitKey(0)
    cv.destroyAllWindows()

print("Program terminated.")
