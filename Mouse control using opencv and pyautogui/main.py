# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 20:37:26 2020

@author: Helmo
"""

#-------------------------------------------
# modules
#-------------------------------------------

import cv2
import numpy as np
import pyautogui
import functions

#-------------------------------------------
# OpenCV setup
#-------------------------------------------

cap = cv2.VideoCapture(0)
cap.set(10, 200)

top, right, bottom, left = 340, 0, 640, 300

screenWidth, screenHeight = pyautogui.size()
screenWidth, screenHeight = (screenWidth - 1, screenHeight - 1)
factor = (round(screenWidth/300), round(screenHeight/300))

bgModel = cv2.createBackgroundSubtractorMOG2(0, 50)

lista = []

pyautogui.FAILSAFE = False

lower = np.array([0, 50, 90], dtype="uint8")
upper = np.array([20, 255, 255], dtype="uint8")

#-------------------------------------------
# Main loop
#-------------------------------------------

while(True):
    
    #-------------------------------------------
    # Image acquisition
    #-------------------------------------------
    
    ret, frame = cap.read()
    
    #-------------------------------------------
    # Image pre-processing
    #-------------------------------------------
    
    frame = cv2.bilateralFilter(frame, 5, 50, 100)  # Smoothing
    frame = cv2.flip(frame, 1)  #Horizontal Flip
    
    #-------------------------------------------
    # Image ROI
    #-------------------------------------------

    region = frame.copy()
    region = region[right:left, top:bottom]
    
    cv2.rectangle(frame, (440,0), (540,100), (0, 255, 0), 1)
    cv2.rectangle(frame, (440,200), (540,300), (0, 255, 0), 1)
    cv2.rectangle(frame, (340,100), (440,200), (0, 255, 0), 1)
    cv2.rectangle(frame, (540,100), (640,200), (0, 255, 0), 1)
    cv2.rectangle(frame, (top,right), (bottom,left), (255, 0, 0), 5)

    fgmask = bgModel.apply(region)
    img = cv2.bitwise_and(region, region, mask=fgmask)

    #-------------------------------------------
    # ROI human skin segmentation
    #-------------------------------------------
    
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    skinMask = cv2.inRange(hsv, lower, upper)
    kernel = np.ones((3,3),np.uint8)
    skinMask = cv2.dilate(skinMask,kernel,iterations = 4)
    skinMask = cv2.GaussianBlur(skinMask,(5,5),100)
        
    #-------------------------------------------
    # Segmentation
    #-------------------------------------------
        
    contours, hierarchy = cv2.findContours(skinMask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    count_defects = 0
    
    if len(contours) > 0:
        
        area = [cv2.contourArea(c) for c in contours]
        area2 = area.index(max(area))
        
        if max(area) > 350:
            
            hull = cv2.convexHull(contours[area2])
            chull = cv2.convexHull(contours[area2],returnPoints=False)
            
            defects = functions.count_defects(contours[area2], chull)
            
            extreme_top = tuple(hull[hull[:, :, 1].argmin()][0])
            print(defects)
            (move_x, move_y) = pyautogui.position()
            (move_x, move_y) = functions.move_xy(extreme_top, screenWidth, screenHeight, move_x, move_y, 0)
            
            if (defects == 0 or defects == 1):
                pyautogui.moveTo(move_x, move_y)
            elif (defects == 2 or defects == 3):
                pyautogui.click(button = "left", interval = 0.15)
            elif defects >= 4:
                pyautogui.doubleClick(button = "right", interval = 0.1)  
                
    #-------------------------------------------
    # Final Results
    #-------------------------------------------

    cv2.imshow("s", frame)
    cv2.imshow("s1", skinMask)
    if (cv2.waitKey(1) == 27):  #ESC to Terminate
        break
    
cap.release()
cv2.destroyAllWindows()