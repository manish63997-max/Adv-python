import cv2

# Read image from the same folder as the Python file
image = cv2.imread(r"C:\Users\birad\OneDrive\Pictures\Camera Roll\Me.jpg")

# Check if image is loaded
if image is None:
    print("Error: Image not found!")
else:
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Edge detection using Canny
    edges = cv2.Canny(gray, 40, 90)

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Grayscale Image", gray)
    cv2.imshow("Edge Detection", edges)

    # Wait until any key is pressed
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()

