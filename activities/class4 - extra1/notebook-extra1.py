#%% Imports 
import cv2

#%% Read Image1

Image1 = cv2.imread ('background.jpg')
cv2.imshow('Background', Image1)
cv2.waitKey(0)
cv2.destroyAllWindows()

#%% Read Image2

Image2 = cv2.imread ('flower.jpg')
cv2.imshow('Flower', Image2)
cv2.waitKey(0)
cv2.destroyAllWindows()

#%% Sum Images

Image1_add_Image2 = cv2.add (Image1, Image2)
cv2.imwrite('image1_sum_image2.png', Image1_add_Image2)
cv2.imshow('image1 add image2', Image1_add_Image2)
cv2.waitKey(0)
cv2.destroyAllWindows()

#%% Sum with weights
dst = cv2.addWeighted (Image1,0.3, Image2,0.7,0)
cv2.imwrite('Sum with weights.png', Image1_add_Image2)
cv2.imshow ( 'Weights' , dst)
cv2.waitKey (0)
cv2.destroyAllWindows ()

# %% Subtraction

Image2_sub_Image1 = cv2.subtract (Image2, Image1)
cv2.imwrite('image2_sub_image1.png', Image2_sub_Image1)
cv2.imshow('Image2 subtracts Image1', Image2_sub_Image1)
cv2.waitKey(0)
cv2.destroyAllWindows()

# %% Multiply

Image1_mult_Image2 = cv2.multiply (Image1, Image2)
cv2.imwrite('Image1_mult_Image1.png', Image1_mult_Image2)
cv2.imshow('Image1 multiply Image2', Image1_mult_Image2)
cv2.waitKey(0)
cv2.destroyAllWindows()

#%% Divide

Image1_divis_Image2 = cv2.divide (Image1, Image2)
cv2.imwrite('Image1_divide_Image2.png', Image1_divis_Image2)
cv2.imshow('Image1 divide Image2', Image1_divis_Image2)
cv2.waitKey(0)
cv2.destroyAllWindows()

#%% AND

Image1_and_Image2 = cv2.bitwise_and (Image1, Image2)
cv2.imwrite('Image1_and_Image2.png', Image1_and_Image2)
cv2.imshow('Image1 and Image2', Image1_and_Image2)
cv2.waitKey(0)
cv2.destroyAllWindows()

#%% OR

Image1_or_Image2 = cv2.bitwise_or (Image1, Image2)
cv2.imwrite('Image1_or_Image2.png', Image1_or_Image2)
cv2.imshow('Image1 or Image2', Image1_or_Image2)
cv2.waitKey(0)
cv2.destroyAllWindows()

#%% XOR

Image1_xor_Image2 = cv2.bitwise_xor (Image1, Image2)
cv2.imwrite('Image1_xor_Image2.png', Image1_xor_Image2)
cv2.imshow('Image1 xor Image2', Image1_xor_Image2)
cv2.waitKey(0)
cv2.destroyAllWindows()

#%% NOT

Image1_not_Image2 = cv2.bitwise_not (Image2, Image1)
cv2.imwrite('Image1_not_Image2.png', Image1_not_Image2)
cv2.imshow('Image1 not Image2', Image1_not_Image2)
cv2.waitKey(0)
cv2.destroyAllWindows()
