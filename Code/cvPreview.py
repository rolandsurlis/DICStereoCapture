import cv2
import numpy as np

# Open both camera feeds
cap_left = cv2.VideoCapture(0)
cap_right = cv2.VideoCapture(1)

while cap_left.isOpened() and cap_right.isOpened():
    retL, frame_left = cap_left.read()
    retR, frame_right = cap_right.read()

    if retL and retR:
        
        frame_left = cv2.resize(frame_left, (640, 480))
        frame_right = cv2.resize(frame_right, (640, 480))

        # Concatenate images side by side
        stereo_frame = np.hstack((frame_left, frame_right))

        cv2.imshow("Stereo Preview", stereo_frame)
    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap_left.release()
cap_right.release()
cv2.destroyAllWindows()

