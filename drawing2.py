import cv2

cap = cv2.VideoCapture(0)

drawing = False
start_point = None
end_point = None

# Store all completed lines
lines = []


def draw_line(event, x, y, flags, param):
    global drawing, start_point, end_point, lines

    # Mouse button pressed
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start_point = (x, y)
        end_point = (x, y)

    # Mouse movement while holding button
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            end_point = (x, y)

    # Mouse button released
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        end_point = (x, y)

        # Add the new line to the list
        lines.append((start_point, end_point))


cv2.namedWindow("frame")
cv2.setMouseCallback("frame", draw_line)


while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Draw all previously completed lines
    for start, end in lines:
        cv2.line(frame, start, end, (0, 255, 0), 2)

    # Draw the current line while dragging
    if drawing and start_point is not None:
        cv2.line(frame, start_point, end_point, (0, 255, 0), 2)

    cv2.imshow("frame", frame)

    # Press q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()