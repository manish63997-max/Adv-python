import cv2
import numpy as np

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Define the range for the color to track (e.g., blue)
# Adjust these values based on the object color
lower_blue = np.array([100, 150, 50])
upper_blue = np.array([140, 255, 255])

# Canvas to store the drawing
canvas = None

while True:
    ret, frame = cap.read()
    if not ret: break
    
    # Flip the frame for a mirror effect
    frame = cv2.flip(frame, 1)
    
    if canvas is None:
        canvas = np.zeros_like(frame)

    # Convert to HSV color space for better color detection
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Create a mask for the color
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    
    # Find the contours of the object
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if contours:
        # Get the largest contour
        c = max(contours, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        
        if radius > 10:
            # Draw on the canvas
            cv2.circle(canvas, (int(x), int(y)), 5, (0, 255, 0), -1)

    # Combine the camera frame and the canvas
    result = cv2.addWeighted(frame, 0.5, canvas, 0.5, 0)
    
    cv2.imshow("Virtual Painter", result)
    
    # Press 'c' to clear the canvas, 'q' to quit
    key = cv2.waitKey(1) & 0xFF
    if key == ord('c'):
        canvas = np.zeros_like(frame)
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()