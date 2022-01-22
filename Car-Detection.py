 #!/usr/bin/env python
import cv2
import numpy as np
import time

bg_subtractor = cv2.createBackgroundSubtractorMOG2(detectShadows=True,varThreshold=35) #,varThreshold=30
erode_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
dilate_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
cap = cv2.VideoCapture('carPark.mp4')
ret, frame = cap.read()


loc = [] # Holde 3 lists [ [(cx,cy), time.time()], [],  []     ]
time_diff = []
 
def inRange(a1, a2):
    diff_org = tuple(map(lambda i, j: i - j, (a1,a2), loc[0][0]))
    diff_abs = (abs(diff_org[0]), abs(diff_org[1]))
    if diff_abs[0] <= 20:
        return (diff_abs[1] <= 20)  
    else:
        return False

while ret:
   
    roi = frame[20:640, 20:588]
    mog_mask = bg_subtractor.apply(roi)
    _, thresh = cv2.threshold(mog_mask, 244, 255, cv2.THRESH_BINARY)
    cv2.erode(thresh, erode_kernel, thresh, iterations=2)
    cv2.dilate(thresh, dilate_kernel, thresh, iterations=2)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    id_count = 0
    for cnt in contours:
        if cv2.contourArea(cnt) > 1250:
            x, y, w, h = cv2.boundingRect(cnt)
            id_count += 1
            cx = int((x+x+w)/2)
            cy = int((y+y+h)/2)
            
            ## For first time of detection to hold timestamp and location of object center (cx, cy)
            if len(loc) == 0:
                loc.append([(cx,cy), time.time()])
            elif inRange(cx,cy):
                timDif = time.time() - loc[0][1]
                prev_dif=0
                if len(time_diff) > 0:
                    prev_dif = timDif - time_diff[-1]
                time_diff.append(timDif)

                if prev_dif > 2.5: # time limit
                    print([x,y,w,h], prev_dif)
                    crop_img = roi[y-5:y + h+5, x-5:x + w+6]
                    # resize image
                    crop_img = cv2.resize(crop_img, (int(crop_img.shape[1] * 5), int(crop_img.shape[0] * 5)), 
                     interpolation = cv2.INTER_AREA)
                    name = 'detected_TimeLimit_'+ str(round(prev_dif,2)) + '.jpg'
                    cv2.imshow('DoubleParking', crop_img) 
                    # cv2.imwrite(name, crop_img)
            cv2.rectangle(roi, (x, y), (x+w, y+h), (255, 255, 0), 2)
            cv2.circle(roi,(cx,cy), 3, (0,0,255), -1)

    cv2.imshow('MOG2', mog_mask) 
    cv2.imshow('detection', roi)
 
    
    k = cv2.waitKey(30)
    if k == 27: # Escape break
        break

    ret, frame = cap.read()
