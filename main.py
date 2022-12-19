import cv2
from age_and_gender import detect_age_and_gender


 
capture = cv2.VideoCapture('video.mp4')
 

while (True):

    success, frame = capture.read()
    print(success)
    if success : 
        sr = cv2.dnn_superres.DnnSuperResImpl_create()
        path = 'models/EDSR_x4.pb'
        sr.readModel(path)
        sr.setModel("edsr",4)
        result = sr.upsample(frame)
        
        newresult = detect_age_and_gender(result)
        cv2.imwrite(f'image_{fr_no}.jpg',result)
        fr_no=fr_no+1        
    else:
        break
    
 
capture.release()
