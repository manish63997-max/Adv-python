import cv2

cap = cv2.VideoCapture(0)

flip_mode = 1

print("Controls:\n  Press 'f' to toggle flip modes\n  Press 'q' to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break

    
    if flip_mode in (1, 0, -1):
        display_frame = cv2.flip(frame, flip_mode)
    else:
        display_frame = frame  

    cv2.imshow('Live Camera (Press F to Flip, Q to Quit)', display_frame)

    key = cv2.waitKey(1) & 0xFF
    
    
    if key == ord('f'):
        if flip_mode == 1:
            flip_mode = 0      
        elif flip_mode == 0:
            flip_mode = -1     
        elif flip_mode == -1:
            flip_mode = 2      
        else:
            flip_mode = 1      

    
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()