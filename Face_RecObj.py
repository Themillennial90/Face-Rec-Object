


import cv2

#gets camera
capture = cv2.VideoCapture(0) # opens camera, 0 = the first camera on the camera if their are more than 1 

while True:
    timer = cv2.getTickCount() #display timer counter
    success, img = capture.read()

    
    fps = cv2.getTickFrequency()/(cv2.getTickCount() - timer) #(f/t)-time = frames per second
    cv2.putText(img,str(fps),(75,50),cv2.FONT_HERSHEY_PLAIN,3,(0,0,255),2) #places timer at 75,50( top right corner)  Font= Hershey , Size of Font = 3, Font Color  0 0 255 , linetype 2
    cv2.imshow("Tracking",img) #window name = Tracking
    
    if cv2.waitKey(1) & 0xff == ord('e'):#frames milesecond 1 , exit video using lowercase e
        break 
    
    
   
