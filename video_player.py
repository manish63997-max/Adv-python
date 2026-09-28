import cv2 as cv
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Hide the Tkinter root window
Tk().withdraw()

# Open file dialog to select a video
video_path = askopenfilename(
    title="Select a Video File",
    filetypes=[
        ("Video Files", "*.mp4 *.avi *.mov *.mkv *.wmv"),
        ("All Files", "*.*")
    ]
)

# Check if a file was selected
if not video_path:
    print("No video file selected.")
    exit()

# Open the selected video
cap = cv.VideoCapture(video_path)

# Check if the video opened successfully
if not cap.isOpened():
    print("Error: Unable to open the video file.")
    exit()

# Get the video's FPS
fps = cap.get(cv.CAP_PROP_FPS)
if fps > 0:
    delay = int(1000 / fps)
else:
    delay = 30  # Default delay

print("Press 'Q' to quit.")

# Display the video
while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv.imshow("Video Player", frame)

    # Press Q to exit
    if cv.waitKey(delay) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv.destroyAllWindows()

print("Video playback completed.")