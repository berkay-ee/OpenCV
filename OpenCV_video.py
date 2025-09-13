import cv2


#open the camera
cap = cv2.VideoCapture(0)

#set a vidde format 
video = cv2.VideoWriter_fourcc(*'mp4v')

#24 fps and 640x480 resolution
out = cv2.VideoWriter('output.mp4', video, 24.0, (640, 480))

#write a each frame and display it
while True:
    #read a frame from the camera
    ret, frame = cap.read()
    #if there is no frame, break the loop
    if not ret:
        break

    # Show the live frame
    cv2.imshow('Live', frame)

    # Write the frame to the MP4 file
    out.write(frame)

    key = cv2.waitKey(1) & 0xFF

    # Exit when 'q' is pressed
    if key == ord('q'):
        break


cap.release()
out.release()
cv2.destroyAllWindows()
