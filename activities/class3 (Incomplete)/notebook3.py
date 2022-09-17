#%% Imports

import requests
import cv2
import numpy as np
import imutils

#%% Acessando a camera do celular pela URL.

# Necessário aplicativo IP Webcam no celular


# URL do celular 
url = "http://192.168.1.113:8080/shot.jpg"

# While para continuar buscando dados pela URL
while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)
    img = imutils.resize(img, width=1000, height=1800)
    cv2.imshow("Camera Android", img)
  
    # Press Esc key to exit
    if cv2.waitKey(1) == 27:
        break
  
cv2.destroyAllWindows()

# %% Gravando video e convertendo para GrayScale

source = 0

cap = cv2.VideoCapture(source)

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

out = cv2.VideoWriter('video_teste.mp4',cv2.VideoWriter_fourcc(*'XVID'), 10, (frame_width,frame_height))

while(True): 
    
    ret, frame = cap.read()  
    
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
      
    
    out.write(gray)  
      
    
    cv2.imshow('Original', frame) 
  
    
    cv2.imshow('frame', gray) 
      
    if cv2.waitKey(1) & 0xFF == ord('a'): 
        break

cap.release() 
cv2.destroyAllWindows() 

# %%
