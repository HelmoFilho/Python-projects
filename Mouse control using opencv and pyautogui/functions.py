# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 13:24:48 2020

@author: Helmo
"""

import cv2
import numpy as np

def move_xy(xy, k1, k2, dx, dy, mode):
    
    (x,y) = xy[0], xy[1]
    
    if ((x > 100) and (x <= 200)) and ((y > 0) and (y <= 100)):
        dy -= 10
    elif ((x > 100) and (x <= 200)) and ((y > 200) and (y <= 300)):
        dy += 10
    elif ((x > 0) and (x <= 100)) and ((y > 100) and (y <= 200)):
        dx -= 10
    elif ((x > 200) and (x <= 300)) and ((y > 100) and (y <= 200)):
        dx += 10
        
    return (dx, dy)


def count_defects(Cotour_max, c_hull):
    
    count_defects = 0

    print(f"{type(Cotour_max)}")
    print(f"{type(c_hull)}")
    
    defects = cv2.convexityDefects(Cotour_max, c_hull)
            
    for i in range(defects.shape[0]):
        s, e, f, d = defects[i, 0]
        start = tuple(Cotour_max[s][0])
        end = tuple(Cotour_max[e][0])
        far = tuple(Cotour_max[f][0])
        
        a = np.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
        b = np.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
        c = np.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
        angle = (np.arccos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)) * 180) / 3.14
        
        if angle <= 90:
            count_defects += 1         
            if count_defects > 4:
                count_defects = 4
    
    return count_defects