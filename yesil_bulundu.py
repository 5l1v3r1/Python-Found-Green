#!/usr/bin/env python
# -*- coding:utf-8 -*-

#########################################################
#          PYTHON - FOUND GREEN - GH0ST S0FTWARE        #
######################################################### 
#                       CONTACT                         #
#########################################################
#              DEVELOPER : İSMAİL TAŞDELEN              #                       
#        Mail Address : pentestdatabase@gmail.com       #
# LINKEDIN : https://www.linkedin.com/in/ismailtasdelen #
#           Whatsapp : + 90 534 295 94 31               #
#########################################################

import cv2 as cv
import numpy as np

goruntu_yakala = cv.VideoCapture(0)
 
while(1):
    _, resim = goruntu_yakala.read()
    bgr2hsv = cv.cvtColor(resim, cv.COLOR_BGR2HSV)
    dusuk_yesil_orani = np.array([49,50,50], dtype=np.uint8)
    yuksek_yesil_orani = np.array([80, 255, 255], dtype=np.uint8)
    maske = cv.inRange(bgr2hsv, dusuk_yesil_orani, yuksek_yesil_orani)
    an = cv.moments(maske)
    alan = an['m00']
 
    if(alan > 2000000):
        x = int(an['m10']/an['m00'])
        y = int(an['m01']/an['m00'])
        print "x = ", x
        print "y = ", y
        cv.rectangle(resim, (x-5, y-5), (x+5, y+5),(0,0,255), 2)
        cv.putText(resim, "pos:"+ str(x)+","+str(y), (x+10,y+10), cv.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
    cv.imshow('Python - Kontrast Görüntüsü', maske)
    cv.imshow('Python - Görüntü İşleme', resim)
   
    if cv.waitKey(1) & 0xFF == ord('q'):
        goruntu_yakala.release()
        break

cv.destroyAllWindows()
