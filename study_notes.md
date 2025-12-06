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
**Date: 2025-11-11**  
**Topic: Detecting and Visualizing Contours in OpenCV**  

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

---------------

**File: draw_revised.py**  
**Date: 2025-12-05**  
**Topic: Custom Backgrounds, Ellipses, Symmetric Lines, and Centered Text in OpenCV**

### 1. Overview  
This script is an extened version of the original **draw.py** file from OpenCV drawing basics. While the original demonstrated simple primitives such as rectangles, circles, lines, and text on a blank canvas, this reviesd version creates a complete mint-choco themed graphic layout using geometric reasoning and custom color palettes.

New features include:
- A mint-choco checkered background  
- A centered white ellipse with a black outline  
- Symmetric decorative **thin-thick-thin** horizontal line patterns above and below the ellipse  
- Perfectly centered text inside the ellipse  
- Use of geometric calculations to ensure symmetry and proportional spacing  

This script showcases how OpenCV can be used not only for computer vision tasks, but also for graphic design, UI mockups, and visual composition.

### 2. Code Summary  
- **Create a blank canvas**  
`blank = np.zeros((500, 500, 3), dtype = 'uint8')`

- **Define mint-choco colors**
```
mint = (209, 240, 170)  
choco = (55, 78, 111)  
```

- **Generate checkered pattern**
 Uses tile logic:  
  ```  
  for y in range(0, height, tile):  
      for x in range(0, width, tile):  
          if ((x // tile + y // tile) % 2 == 0):  
              blank[y:y+tile, x:x+tile] = mint  
          else:  
              blank[y:y+tile, x:x+tile] = choco  
  ```
- **Draw white ellipse + black border**  
  ```  
  cv.ellipse(blank, center, axes, 0, 0, 360, (255,255,255), -1)  
  cv.ellipse(blank, center, axes, 0, 0, 360, (0,0,0), 4)  
  ```  

- **Compute vertical geometry**  
  ```  
  ellipse_top = cy - ry  
  ellipse_bottom = cy + ry  
  y_mid_top = ellipse_top // 2  
  y_mid_bottom = (ellipse_bottom + height) // 2  
  ```  

- **Draw symmetric thin–thick–thin lines**  
  ```  
  cv.line(blank, (0, y1), (width, y1), (255,255,255), thin)  
  cv.line(blank, (0, y2), (width, y2), (255,255,255), thick)  
  cv.line(blank, (0, y3), (width, y3), (255,255,255), thin)  
  ```

- **Center text inside ellipse**  
  ```  
  (text_w, text_h), baseline = cv.getTextSize  (text, font, scale, thickness)  
  text_x = cx - text_w // 2  
  text_y = cy + text_h // 2  
  ```

- **Display final result**  
  `cv.imshow('Mint Choco Output', blank)`

### 3. Learned Functions

- `np.zeros(shape, dtype)`    
  Creates a blank BGR image.

- `cv.ellipse(image, center, axes, angle, startAngle, endAngle, color, thickness)`    
  Draws both filled and bordered ellipses.

- `cv.line(image, pt1, pt2, color, thickness)`    
  Draws straight segments between two points.

- `cv.getTextSize(text, fontFace, fontScale, thickness)`    
  Finds width and height of text → used for perfect centering.

- `cv.putText(image, text, org, fontFace, fontScale, color, thickness)`  
  Renders text onto the canvas.

- **Geometric spacing and alignment**  
  - Computing ellipse top/bottom  
  - Computing vertical midpoints  
  - Building symmetric layouts  

### 4. Common Issues & Fixes

- **Lines appear misaligned**  
  Fix: verify midpoint calculations (ellipse_top, ellipse_bottom).

- **Ellipse looks distorted**  
  Ensure axes = (horizontal_radius, vertical_radius).

- **Colors look incorrect**  
  Remember OpenCV uses **BGR**, not RGB.

- **Text not centered**  
  Must use `getTextSize()` to compute proper placement.

### 5. Notes & Insights
- Alternating tile patterns allow easy checkered backgrounds.  
- Ellipses with borders require two draw calls: one filled, one outlined.  
- Geometric formulas are essential for clean visual layout design.  
- The thin–thick–thin decorative pattern demonstrates how OpenCV can mimic poster/graphic design elements.  
- Centering text is not automatic; manual measurements are required.

### 6. Added Features (Compared to original draw.py)

- **Mint–choco checkered background** (replaces plain black)  
- **Ellipse instead of simple rectangle/circle**  
- **Symmetric decorative separators**    
- **Mathematically centered text**  
- **Color palette design using BGR**  
- **Modular layout calculations (ellipse_top, y_mid_top, etc.)**  
- Overall structure is more design-focused than primitive-focused

--------

**File: thresh.py**  
**Date: 2025-12-05**  
**Topic: Simple Thresholding & Adaptive Thresholding in OpenCV**

### 1. Overview
This script demonstrates two major thresholding techniques in OpenCV:

1. **Simple Thresholding** – applies one global threshold value to the entire image.  
2. **Adaptive Thresholding** – calculates a different threshold for each pixel based on local neighborhood intensity.

The program loads an image of cats, converts it to grayscale, and applies various binary segmentation methods to compare how each approach behaves under different lighting conditions.

### 2. Code Summary  
- **Load Image and Convert to Grayscale**  
  ```  
  img = cv.imread('../Resources/Photos/cats.jpg')  
  gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  
  ```  

- **Simple Thresholding (Binary)**  
  ```  
  threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)  
  ```  

- **Simple Thresholding (Inverse)**  
  ```  
  threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)  
  ```

- **Adaptive Thresholding (Gaussian Method)**  
  ```  
  adaptive_thresh = cv.adaptiveThreshold(  
      gray,  
      255,  
      cv.ADAPTIVE_THRESH_GAUSSIAN_C,  
      cv.THRESH_BINARY_INV,  
      11,  
      9  
  )  
  ```

- **Display Results**  
  ```  
  cv.imshow('Simple Thresholded', thresh)  
  cv.imshow('Simple Thresholded Inverse',   thresh_inv)  
  cv.imshow('Adaptive Thresholding',   adaptive_thresh)  
  ```
### 3. Learned Functions

- **cv.threshold(src, thresh, maxVal, type)**  
  Performs global thresholding. Returns `(actual_threshold_used, output_image)`.

- **cv.adaptiveThreshold(src, maxVal, adaptiveMethod, thresholdType, blockSize, C)**  
  Computes a threshold for each pixel based on the weighted sum of neighboring pixels.

### 4. Notes & Insights

- Simple thresholding is fast but sensitive to lighting differences.  
- Adaptive thresholding is far more robust when brightness varies across the image.  
- The parameters `blockSize` and `C` significantly affect segmentation quality.  
- Using grayscale is required for thresholding because the operation depends on pixel intensity values.

--------

**File: transformations.py**  
**Date: 2025-12-06**  
**Topic: Interactive Image Transformations (Translations, Rotation, Resize, Flip, Crop)**

### 1. Overview
This script demonstrates several fundamental geometric transformations using OpenCV in an interactive format.  
Instead of executing all operations sequentially, the program waits for user input and performs transformations based on keyboard commands.

The supported operations include:  
- Translation   
- Rotation (user-defined angle)  
- Resize (square, user-defined size)  
- Flip (mode 0, 1, -1)  
- Crop  

Each transformation is displayed in a separate result window, and pressing any non-assigned key exits the program.

### 2. Code Summary

- **Load Original Image**  
  ```  
  img = cv.imread('../Resources/Photos/park.jpg')  
  cv.imshow('Original', img)  
  ```

- **Translation**  
  ```  
  transMat = np.float32([[1,0,x],[0,1,y]])  
  cv.warpAffine(img, transMat, dimensions)  
  ```
  Moves the image horizontally and vertically using an affine transformation matrix.

- **Rotation**  
  ```  
  rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)  
  cv.warpAffine(img, rotMat, dimensions)  
  ```  
  Rotates the image around the given rotation point (default: image center).

- **Resize (Square)**  
  ```  
  cv.resize(img, (size, size), interpolation=cv.INTER_CUBIC)    
  ```  
  Resizes the image to a user-defined square dimension.

- **Flip**  
  ```  
  cv.flip(img, mode)  
  ```  
  Performs vertical (0), horizontal (1), or both (-1) flipping.

- **Crop**  
  ```  
  cropped = img[200:400, 300:400]  
  ```  
  Extracts a manually defined rectangular region from the image.

- **Interactive Loop**  
  ```   
  key = cv.waitKey(0)  
  ```  
  - T → translation    
  - R → rotation      
  - S → resize    
  - F → flip    
  - C → crop    
  - Other keys → exit    

- **Close All Windows**  
  ```  
  cv.destroyAllWindows()
  ```

### 3. Learned Functions

- **cv.warpAffine(src, M, dsize)**  
  Applies a 2×3 affine transformation matrix to the image.

- **cv.getRotationMatrix2D(center, angle, scale)**  
  Generates a rotation matrix for 2D rotation.

- **cv.resize(src, dsize, interpolation)**  
  Resizes the image with several interpolation options;  
  `INTER_CUBIC` provides high-quality enlargement.

- **cv.flip(src, flipCode)**  
  Flips the image:   
  - 0 → vertical  
  - 1 → horizontal  
  - -1 → both axes  

- **Numpy slicing for cropping**  
  Used to extract specific regions of the image.

- **cv.waitKey(delay)**  
  Waits for key input and enables interactive execution.

---

### 4. Notes & Insights  
- Affine transformations (translation, rotation) rely on matrix multiplication, handled internally by `cv.warpAffine`.    
- Using user input allows flexible control over transformation behavior.  
- Limiting flip mode to 0, 1, -1 preserves OpenCV’s expected parameters and avoids errors.  
- Resizing to a square dimension simplifies user input.  
- The interactive structure is useful for experimenting with image transformations in real time.

----------

## Section #2 - Advanced  

**File: bitwise.py**  
**Date: 2025-12-07**  
**Topic: Boolean Shape Operations (AND, OR, XOR, NOT) with Interactive Selection**

### 1. Overview
This script demonstrates how to construct basic geometric shapes in OpenCV (triangle, rectangle, circle), convert them into binary masks, and apply Boolean operations (AND, OR, XOR, NOT).  
The program is interactive: the user selects shapes and operations through console input, and each result is displayed in a separate OpenCV window.

Boolean mask logic is used rather than color-based operations, ensuring consistent behavior across different shapes and colors.

Supported operations:  
- AND (intersection)  
- OR (union)  
- XOR (exclusive regions)  
- NOT (color complement of a single shape)

Each result is recolored according to predefined rules (white, yellow, black, complement), and any key press inside the image window closes the current display.

---

### 2. Code Summary

- **Create Blank Canvas**  
```python  
img = np.zeros((500, 500, 3), dtype='uint8')  
```  
Generates a black background on which shapes are drawn.

- **Draw Triangle**  
```python  
pts = np.array([[250, 50], [50, 400], [450, 400]], np.int32)  
cv.fillPoly(img, [pts], (0, 0, 255))  
```  
Creates a filled red triangle.

- **Draw Rectangle**  
```python  
cv.rectangle(img, (80,80), (420,420), (255,0,0), -1)  
```  
Draws a filled blue square.  

- **Draw Circle**  
```python  
cv.circle(img, (250,250), 170, (0, 255, 0), -1)  
```  
Draws a filled green circle.

- **Grayscale Mask Conversion**  
```python  
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  
mask = cv.threshold(gray, 1, 255, cv.THRESH_BINARY)  
```  
Converts a colored shape to a binary mask (0 or 255), which is required for correct Boolean operations.

- **Boolean Operations Using Masks**  
```python  
cv.bitwise_and(mask1, mask2)  
cv.bitwise_or(mask1, mask2)  
cv.bitwise_xor(mask1, mask2)  
```  
OpenCV performs logic at the pixel level using 1-channel masks.

- **Coloring Boolean Results**  
```python  
out[mask == 255] = (255, 255, 255) # AND (white)  
out[mask == 255] = (0, 255, 255) # OR (yellow)  
out[mask == 255] = (0, 0, 0) # XOR (black)  
```  
Colors are applied after the Boolean mask is obtained.

- **Color Complement for NOT**  
```python  
result = 255 - img  
```  
Produces the color-inverted version of the selected shape.

- **Display Loop**  
```python  
cv.imshow("Result", img)  
cv.waitKey(0)  
cv.destroyAllWindows()  
```  
Each result waits for a key press inside the GUI window before closing.

### 3. Learned Functions  
- **cv.fillPoly(img, pts, color)**  
Draws filled polygons such as triangles using an array of vertex points.

- **Binary Mask Generation (Critical for Boolean Ops)**  
```python  
gray = cv.cvtColor(...)  
cv.threshold(...)  
```  
Ensures reliable AND/OR/XOR behavior by reducing all color channels into a single binary mask.

- **cv.bitwise_* functions (AND, OR, XOR)**  
Operate correctly only on 1-channel binary masks when performing pure geometric Boolean operations.

- **Custom Color Maping After Masking**  
```python  
out[mask == 255] = desired_color  
```  
Allows complete control over how Boolean regions are visualized.

- **Color Complement Operation**  
```python  
255-img  
```  
Simple and fast method to produce negative/inverted images.

- **Interactive Console + OpenCV GUI Workflow**  
Learned how to:  
- accept user console input    
- display results in OpenCV windows    
- avoid `input()` freezing OpenCV GUI by using `cv.waitKey()`  

### 4. Notes & Insights
- Boolean geometry works **only with binary masks**, not with multi-channel (BGR) images.  
- XOR becomes invisible (all black) if the output color for XOR regions is also black; visibility depends entirely on color mapping.  
- `cv.waitKey(0)` must handle all GUI pauses—mixing it with `input()` freezes windows.  
- Interaction design matters: shape selection → operation selection → per-window display creates a smooth workflow.  
- Separating:  
- shape creation (color)  
- mask extraction  
- Boolean combination  
- visualization  
makes the transformation pipeline clean and extendable.
