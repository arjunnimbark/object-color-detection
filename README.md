# object-color-detection
The provided Python code captures real-time video from a webcam using OpenCV. 
It analyzes the dominant color at the center of each frame based on hue values in the HSV color space.


The code performs the following steps:

Captures video from the default webcam using cv.VideoCapture.
Sets the height and width of the video feed to 720 pixels and 1280 pixels, respectively.
Enters a loop to continuously read frames from the webcam.
Converts the current frame from BGR to HSV color space using cv.cvtColor.
Determines the center pixel coordinates (cx, cy) of the frame.
Extracts the hue value of the center pixel to identify the dominant color.
Maps the hue value to a specific color label (e.g., red, orange, yellow, etc.).
Retrieves the BGR values of the center pixel to display the color with the appropriate color.
Draws a circle at the center of the frame using cv.circle.
Displays the color label and circle on the video frame using cv.putText and cv.imshow.
Continues looping until the 'Esc' key is pressed (key code 27).
Releases the webcam video feed using cap.release() and closes the OpenCV windows using cv.destroyAllWindows().
