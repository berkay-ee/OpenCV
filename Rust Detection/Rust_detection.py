import cv2
import numpy as np



img = cv2.imread("Rust Detection/rust_bridge.jpg") 

gray_convert  = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

print("Pixel before:", gray_convert[160, 100])
gray_convert[100:160, 50:100] = 255
print("Pixel after:", gray_convert[160, 100])


# Show the image in a window
cv2.imshow("My JPG Picture", gray_convert)

# Wait until a key is pressed
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()

















