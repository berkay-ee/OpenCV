import cv2
import os
import numpy as np

# Initialize the camera
camera = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not camera.isOpened():
    print("Could not open camera.")

else:

    #Get a camera specifications
    frame_width  = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))   # Width in pixels
    frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))  # Height in pixels
    fps          = camera.get(cv2.CAP_PROP_FPS)                # Frames per second
    fourcc       = int(camera.get(cv2.CAP_PROP_FOURCC))        # Codec
    brightness   = camera.get(cv2.CAP_PROP_BRIGHTNESS)         # Brightness level
    contrast     = camera.get(cv2.CAP_PROP_CONTRAST)           # Contrast level
    saturation   = camera.get(cv2.CAP_PROP_SATURATION)         # Saturation level


    # Print camera specifications   
    print(" Webcam Specifications:")
    print(f"Resolution   : {frame_width}x{frame_height}")
    print(f"FPS          : {fps}")
    print(f"FOURCC Codec : {fourcc} ({fourcc.to_bytes(4, 'little').decode(errors='ignore')})")
    print(f"Brightness   : {brightness}")
    print(f"Contrast     : {contrast}")
    print(f"Saturation   : {saturation}")


    # Read and display frames from the camera
    while True:
        ret, frame = camera.read()
        if not ret:
            print("Could not read frame.")
            break

        cv2.imshow("Camera", frame)

        # Wait for key press
        key = cv2.waitKey(1) & 0xFF

        if key == ord('s'):
            # Delete previous image
            if os.path.exists("captured_image.jpg"):
                os.remove("captured_image.jpg")
                print("Previous image deleted.")

            # Save the current frame as an image
            save_path = "captured_image.jpg"
            cv2.imwrite(save_path, frame)
            # Print the absolute path where the image is saved
            print(f"Image saved to {os.path.abspath(save_path)}")

        #gray scale image saving and displaying    
        elif key == ord('q') and os.path.exists("captured_image.jpg"):
            # Convert to grayscale and save

            base_path = os.path.dirname(__file__)
            save_grayImg_path = os.path.join(base_path, "Img_gray.jpg")
            grayImg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(save_grayImg_path, grayImg)
            cv2.imshow("Grayscale Image", grayImg)
            print(f"Grayscale image saved to {os.path.abspath(save_grayImg_path)}") 

        #Show a combine image of gray and colored
        elif key == ord('w'):
            if os.path.exists("captured_image.jpg"):
                colorImg = cv2.imread("captured_image.jpg")
                grayImg = cv2.cvtColor(colorImg, cv2.COLOR_BGR2GRAY)
                grayImg_colored = cv2.cvtColor(grayImg, cv2.COLOR_GRAY2BGR)
                combinedImg = np.hstack((colorImg, grayImg_colored))
                cv2.imshow("Combined Image", combinedImg)
            else:
                print("No captured image to combine.")


        elif key == ord('e'):
             
             if os.path.exists("captured_image.jpg"):

                colorImg = cv2.imread("captured_image.jpg")
                grayImg = cv2.cvtColor(colorImg, cv2.COLOR_BGR2GRAY)
                grayImg_colored = cv2.cvtColor(grayImg, cv2.COLOR_GRAY2BGR)

                height, width = colorImg.shape[:2]   # you can choose a size
                grayImg_colored = cv2.resize(grayImg_colored, (width,height))
                grayImg = cv2.resize(grayImg, (width,height))

                combinedImg = np.hstack((colorImg, grayImg_colored))
                cv2.imshow("Combined Image", combinedImg)
           

        
          
      


