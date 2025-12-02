# OpenCV Study Notes

## Section #1 - Basics

**File: 'read.py'**  
**Date: 2025-10-28**  
**Topic: Image and Video Reading in OpenCV**

### 1. Overview
This code demonstrates the basic image and video input/output functions in OpenCV. It loads and displays an image, then reads a video file frame by frame until the user presses the 'd' key or the video ends.

### 2. Code Summary
- Image section  
img = cv.imread(path)  
cv.imshow('Window', img)  
cv.waitKey(0)  

- Video section  
capture = cv.VideoCapture(video_path)  
while True:  
    isTrue, frame = capture.read()  
    if isTrue:  
        cv.imshow('Video', frame)  
    else:  
        break  

Read -> Display -> Wait for key -> Break -> Release resources.

### 3. Learned Functions
- cv.imread(path)  
Reads an image from the specified file path and returns it as a Numpy array.  
- cv.imshow(window_name, image)  
Displays an image or frame in a window.  
- cv.waitKey(delay)  
Waits for a key event for a given time (in ms).  Return the ASCII code of the pressed key.  
- cv.VideoCapture(source)  
Opens a video file or camera stram. 0 or 1 for webcams.  
- capture.read()  
Returns (isTrue, frame). isTrue indicates whether reading the frame succeeded.  
- capture.release()  
Frees video capture resources.  
- cv.destroyAllWindows()  
Closes all OpenCV-created windows.  

### 4. Common Issues & Fixes  
- Program freezes: Always include cv.waitKey() inside loops. It keeps the window responsive.

### 5. Notes & Insights
- The cv.waitKey() function is esstiontial for GUI responsiveness and frame control.
- Checking isTrue before displaying frames prevents errors when reaching the end of the file.
- For real-time video processing, this pattern (read -> process -> display -> wait) is the standard loop structure.
- After calling capture.release(), OpenCV releases the video memory; always pair with cv.destroyAllWindows() to fully close windows.

### How to Upload Files to GitHub Using VS Code Terminal
git add .  
(git add <specific file>)  
git commit -m "update: added GitHub upload guide"  
git push  

-------------------------------------------

**File: 'basic_functions.py'**  
**Date: 2025-11-11**  
**Topic: Basic Image Processing Funtions in OpenCV**  

### 1. Overview
This script demonstrates fundamental image processing techniques using OpenCV. It loads an image and applies several basic transformations such as grayscale conversion, blurring, edge detection, dilation, erosion, resizing, and cropping. It also introduces an interactive viewer that lets users display specific results by pressing keys on the keyboard.

### 2. Code Summary
- Load Image  
img = cv.imread('../Resources/Photos/park.jpg')  
cv.imshow('Park', img)  
- Convert to Grayscale  
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  
- Apply Gaussian Blur  
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)  
- Detect Edges (Canny)  
canny = cv.Canny(blur, 125, 175)  
- Dilate and Erode  
dilated = cv.dilate(canny, (7,7), iterations=3)  
eroded = cv.erode(dilated, (7,7), iterations=3)  
- Resize and Crop  
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)  
cropped = img[50:200, 200:400]  
- Interactive Control (Added Feature)  
Users can display each processed image by pressing specific keys.  
Only one window appears at a time, and pressing 0 or ESC closes the program.

### 3. Learned Functions  
- cv.cvtColor(src, flag) -> Converts color spaces  
- cv.GaussianBlur(src, ksize, borderType) -> Smooths image and reduces noise.  
- cv.Canny(src, threshold1, threshold2) -> Expands white regions, thickening edges.  
- cv.dilate(src, kernel, iterations) -> Expands white regions, thickening edges.  
- cv. erode(src, kernel, iterations) -> Shrinks white regions, thinning edges or removing noise.  
- cv.resize(src, dsize, interpolation) -> Resizes an image with interpolation.  

### 4. Common Issues & Fixes
- Multiple windows remain open:  
Use cv.destroyAllWindows() before displaying a new image to ensure only one active window.

### 5. Notes & Insights
- Gaussian blur helps reduce noise before applying edge detection.  
- Dilation and erosion refine binary images and emphasize structural shapes.  
- Resizing with INTER_CUBIC provies high-quality results, especially for enlargements.  
- The interactive key control system allows dynamic visualization of each image processing step.  
- Always close OpenCV windows with cv.destroyAllWindows() to release resources.

### 6. Added Interactive Feature
- Startup Prompt  
The program now asks the user:  
Do you want to display the image? (Y/N)  
    -If the user enters y, it prints "Displaying the original image..." and opens the interactive viewer.  
    - If the user enters N, it prints "Exiting program..." and terminates.  
    - Any other input leads to "Invalid input. Please restart and enter Y or N."  
- Key-to-Image Mapping
Key	Action  
    p:	Display Original Image  
    g:	Display Grayscale Image  
    b:	Display Blurred Image  
    c:	Display Canny Edges  
    d:	Display Dilated Image  
    e:	Display Eroded Image  
    r:	Display Resized Image  
    x:	Display Cropped Image  
    0 / ESC:  Exit Program

  -------------------

**File: contours.py**  
** Date: 2025-11-11**  
** Topic: Detecting and Visualizing Contours in OpenCV**  

### 1. Overview  
This script demonstrates how to detect and visualize object contours using OpenCV. Contours represent continuous curves that connect points with the same intensity, making them useful for shape detection, segmentation, and boundary analysis.  
The code reads an image of cats, processes it through muliple stages, and finally draws contours on a blank canvas.  
This version also includes stepwise section comments and minor improvements for clarity.  

### 2. Code Summary  
**-  Load Image**
img = cv.imread('../Resources/Photos/cats.jpg')
cv.imshow('Cats', img)
Loads and displays the original image.
**-  Create Blank Canvas**  
blank = np.zeros(imag.shape, dtype='uint8')  
cv.imshow('Blank', blank)  
A blank image with the same dimensions as the original - used later for drawing contours separately.  
**-  Convert to Grayscale**  
gray = cv.cvtColor(img, cv.COLOR_BGR2RGRAY)  
cv.imshow('Gray', gray)  
Converts the imgae to grayscale, simplifying the data for edge detection.  
**- Apply Gaussian Blur**  
blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)  
cv.imshow('Blur', blur)  
Reduces noise and softens edges to improve edge detection results.  
**- Detect Edges (Canny)**  
canny = cv.Canny(blur, 125, 175)  
cv.imshow('Canny Edges', canny)  
Detects edges using gradient thresholds (125, 175). Produces a binary image (white deges, black background).  
**- Find and Draw Contours**  
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)  
print(f'{len(contours)} contours, -1, (0, 0, 255), 1)  
cv.imshow('Contours Drawn', blank)  
cv.waitKey(0)  
Finds all contours in the image, prints the total count, and draws them in red on the blank canvas.  

### 3. Learned Functions  
**- cv.Canny(src, threshold1, threshold2)**  
Detects edges using intensity gradients. Produces a binary edge map.  
**- cv.findContours(image, mode, method)**  
Finds contours (object outlines) from a binary or edge-detected image.  
- cv.RETR_LIST: retrieves all contours.
- cv.CHAIN_APPROX_SIMPLE: compresses redundant points for efficiency.
**- cv.drawContours(image, contours, contourldx, color, thickness)**
Draws on or more contours on the image.
- contourIdx = -1: draws all contours.
- (0, 0, 255): red color (in BGR).
**- np.zeros(shape, dtype)**
Creates a blank image (filled with black) of the same size as the original.
**- cv.cvtColor(src, flag)**
Converts image color space, here used for BGR -> GRAY conversion.
**- cv.GaussianBlur(src, ksize, borderType)**
Applies Gaussian smoothing to reduce image noise.
**- cv.waitKey(delay)**
Waits for user input; 0 means infinite wait until a key is pressed.

### 4. Common Issues & Fixes  
**- Contours not visible:**  
Ensure contours are drawn on a 3-channel (BGR) image, not a grayscale one.  
**- Too many contours detected:**  
Apply Gaussian Blur before Canny to remove small noisy edges.  
**- Canny edges too weak or too strong:**  
Adjust threshold values (125, 175) to find a balance.  
**- Program window closes instantly:**  
Always include cv.waitKey(0) at the end to keep windows open until a key is pressed.

### 5. Notes & Insights  
- cv.Canny() and cv.threshold() can both generate binary images suitable for contour detection.
- Using a blank canvas (np.zeros) to draw contours make visualization clearer and isolates the result.

### 6. Added Interactive Feature (Structural Improvements)  
**- Stepwise Code Structure:**  
The script was reorganized into numbered sections [1], [2], [3], etc., for readability and consistent documentation.
**- Debug Information:**
Added print(f'{len(contours)} contour(s) found!') to provide immediate feedback on detection results.  
**- Alternative Method (Commented):**  
Included thresholding (cv.threshold) as a secondary contour detection method for comparison.  
**- Blank Canvas Visualization:**  
Introduced a new blank image to isolate contours visually from the original image background.
**- Improved Commenting Style:**  
Matched section-based structure from previous scripts (read.py, basic_functions.py) for consistency.
