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