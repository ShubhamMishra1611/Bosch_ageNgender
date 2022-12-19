import cv2
from age_and_gender import detect_age_and_gender
from sr import increase_resolution

 
capture = cv2.VideoCapture('video.mp4')
 

while (True):

    success, frame = capture.read()
    print(success)
    if success: 
    	
        result = increase_resolution('models/EDSR_x4.pb',frame)
        newresult = detect_age_and_gender(result)
        cv2.imwrite(f'image_{fr_no}.jpg',result)
        fr_no=fr_no+1        
    else:
        break
    
 
capture.release()
