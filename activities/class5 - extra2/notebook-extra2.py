#%% Imports
import cv2
import argparse

#%% Read Images

image1 = cv2.imread('image1.jpg')

image2 = cv2.imread('image2.jpg')

image3 = cv2.imread('image3.jpg')

image4 = cv2.imread('image4.jpg')

#%% Average

cv2.imshow("Original", image1)
kernelSizes = [(3, 3), (9, 9), (15, 15)]
# loop over the kernel sizes
for (kX, kY) in kernelSizes:
	# apply an "average" blur to the image using the current kernel
	# size
	blurred = cv2.blur(image1, (kX, kY))
	cv2.imshow(f"Average ({kX}, {kY})", blurred)
	
	cv2.waitKey(0)
	cv2.destroyAllWindows()

#%% 
#  
cv2.imshow("Original", image2)
# loop over the kernel sizes again
for (kX, kY) in kernelSizes:
	# apply a "Gaussian" blur to the image
    blurred = cv2.GaussianBlur(image2, (kX, kY), 0)
    cv2.imshow(f"Gaussian ({kX}, {kY})", blurred)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#%%

cv2.imshow("Original", image3)
# loop over the kernel sizes a final time
for k in (3, 9, 15):
	# apply a "median" blur to the image
	blurred = cv2.medianBlur(image3, k)
	cv2.imshow(f"Median {k}", blurred)
	
	cv2.waitKey(0)
	cv2.destroyAllWindows()

#%% Usado para realçar as bordas das frutas

cv2.imshow("Original", image4)
params = [(11, 21, 7), (11, 41, 21), (11, 61, 39)]
# loop over the diameter, sigma color, and sigma space
for (diameter, sigmaColor, sigmaSpace) in params:
	# apply bilateral filtering to the image using the current set of
	# parameters
	blurred = cv2.bilateralFilter(image4, diameter, sigmaColor, sigmaSpace)
	# show the output image and associated parameters
	title = f"Blurred d={diameter}, sc={sigmaColor}, ss={sigmaSpace}"

	cv2.imshow(title, blurred)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
