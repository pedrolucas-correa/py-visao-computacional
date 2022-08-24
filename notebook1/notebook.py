# %%matplotlib inline 
from IPython.display import Image
import cv2 
import numpy as np
import matplotlib.pyplot as plt

# Image("coca-cola-logo.png")

# coke_img = cv2.imread("coca-cola-logo.png",1)

# print("Image size is:", coke_img.shape)
# print("Image type is:", coke_img.dtype)
# print("")

# plt.imshow(coke_img) ## plt uses RGB and cv2 works with BGR Mode;
 
## Reverse colors of image and print using plt.imshow();
# coke_img_channels_reversed = coke_img[:, :, ::-1]
# plt.imshow(coke_img_channels_reversed)

img_NZ_bgr = cv2.imread("New_Zealand_Lake.jpg",cv2.IMREAD_COLOR)  
b,g,r = cv2.split(img_NZ_bgr) ## Split the image into the BGR components (BLUE, GREEN, RED)

## Shows the channels 
plt.figure(figsize=[20,5])
plt.subplot(141);plt.imshow(r,cmap='gray');plt.title("Red Channel");
plt.subplot(142);plt.imshow(g,cmap='gray');plt.title("Green Channel");
plt.subplot(143);plt.imshow(b,cmap='gray');plt.title("Blue Channel");

## Merge the channels into a BGR image and show the merged output
imgMerged = cv2.merge((b,g,r)) ## Show
plt.subplot(144);
plt.imshow(imgMerged[:,:,::-1]);plt.title("Merged Output"); ## Merge

# %%
