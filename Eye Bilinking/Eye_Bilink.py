import cv2
import cvzone  
from cvzone.FaceMeshModule import FaceMeshDetector
from cvzone.PlotModule import LivePlot

# Web camera open
cap = cv2.VideoCapture(0)

# Face detector only 1 face
detector = FaceMeshDetector(maxFaces=1)

# Eye 
plot = LivePlot(700,400,[20,50])

#Face matrix at around eye
idList = [22,23,24,26,110,130,157,159,160,161,243]


blink_count = 0
blink_flag = 0

while True:
    
    #Reaing a freame from the camera
    success, frame = cap.read()
    frame= cv2.resize(frame,(800,600))
    if not success:
        print("Frame is not found")
        continue

    # Detect face at camera
    frame, faces = detector.findFaceMesh(frame)
    
    #İf face is found draw a circle around the face eye
    if faces:
        face = faces[0]
        for id in idList:
            cv2.circle(frame,face[id],5,(255,0,255)) # circle drawing the eye which is determine the position at the ID matrix

    # Vertical distance at the lower and uppder side of the eye
    leftUp = face [159]
    leftDown = face[23]
    Eye_VerLength,_ = detector.findDistance(leftUp,leftDown) 
    cv2.line(frame,leftUp,leftDown,(0,200,0),3) #draw a line vertial distance
    
    #Horizantyal distance left and right of the eye
    leftRight = face [130]
    leftLeft = face[243]
    Eye_HorLength,_ = detector.findDistance(leftRight,leftLeft) 
    cv2.line(frame,leftRight,leftLeft,(0,200,0),3) # draw a line horizontal distance
    
    # If eyes get far away verital distance get a smaller value 
    #Prevent this effect, horizontal and vertial distance get ration eachother
    # Both value get smaller or bigger depening on the eyes position so ration is not change
    ratio = (Eye_VerLength/Eye_HorLength) * 100
    print(ratio)
    
    # Detect the bilink with a thershold value if is lower bilink is accuor
    #Adding a bilink flah to not count at the staying bilinking position
    if ratio < 36 and blink_flag == 1:
        blink_count += 1 
        blink_flag = 0
    elif ratio > 33 and blink_flag == 0:
        blink_flag = 1
    
    
    # Draw blink counter
    cvzone.putTextRect(frame, f'Blink Count: {blink_count}', (100, 100), scale=2, thickness=2, colorT=(255, 255, 255))
    cv2.imshow("Camera", frame)
    cv2.imshow("Plot",plot.update(ratio))
    

    # Key is press
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
