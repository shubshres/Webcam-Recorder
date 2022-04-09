import numpy as nm
import cv2
from cv2 import VideoWriter_fourcc, VideoWriter

# camera video capture
cam = cv2.VideoCapture(1)

# save video path
# for .avi
out = VideoWriter('recording.avi', VideoWriter_fourcc(*'MP42'), 30.0, (1280, 720))

# for mp4
# out = VideoWriter('recording.mp4', VideoWriter_fourcc(*'FMP4'), 30.0, (1280, 720))

# loop that will run the program
while True:
    # reading camera frame
    stream_ok, frame = cam.read()

    # if webcam is detected
    if stream_ok:
        # show camera
        cv2.imshow('Webcam', frame)

        # write frame to video file
        out.write(frame)

        # if user presses q, exit program
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break

# release camera
cam.release()

# close windows
cv2.destroyAllWindows()

# release video output file stream
out.release()
