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

### 4. Common Issues & 
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
    p	Display Original Image  
    g	Display Grayscale Image  
    b	Display Blurred Image  
    c	Display Canny Edges  
    d	Display Dilated Image  
    e	Display Eroded Image  
    r	Display Resized Image  
    x	Display Cropped Image  
    0 / ESC	Exit Program  
