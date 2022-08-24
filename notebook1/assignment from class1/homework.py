# %% 1 - Abrindo a imagem 
from IPython.display import Image
import cv2 as cv 
import matplotlib.pyplot as plt
import numpy as np

Image(filename='noite-estrelada.png')

# %% 1 - Lendo a imagem com OpenCV

night_img = cv.imread('noite-estrelada.png', 1)

#%% 2 - Imprimindo array matricial da imagem

print(night_img)

# %% 3 - Apresentando a imagem com matplotlib

plt.imshow(night_img)

# %% 4 - Apresentando a imagem em escala de cinza

night_gray = cv.cvtColor(night_img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray_image', night_gray)

cv.waitKey(0)
cv.destroyAllWindows()

# %% 5 - Apresentando versão negativa da imagem

night_negative_img = (255-night_img)
plt.imshow(night_negative_img) 

# %% 6 - Decompondo a imagem em RGB

b,g,r = cv.split(night_img)

plt.figure(figsize=[20,5])
plt.subplot(141);plt.imshow(r,cmap='gray');plt.title("Red Channel");
plt.subplot(142);plt.imshow(g,cmap='gray');plt.title("Green Channel");
plt.subplot(143);plt.imshow(b,cmap='gray');plt.title("Blue Channel");

night_merged_img = cv.merge((b,g,r))
plt.subplot(144);plt.imshow(night_merged_img[:,:,::-1]);plt.title("Merged Output");

# %% 7 - Decompondo a imagem nos canais HSV

night_hsv_img = cv.cvtColor(night_img, cv.COLOR_BGR2HSV)

h, s, v = cv.split(night_hsv_img)

plt.figure(figsize=[20,5])
plt.subplot(141);plt.imshow(h,cmap='gray');plt.title("H Channel");
plt.subplot(142);plt.imshow(s,cmap='gray');plt.title("S Channel");
plt.subplot(143);plt.imshow(v,cmap='gray');plt.title("V Channel");
plt.subplot(144);plt.imshow(night_hsv_img);plt.title("Original");

# %% 8 - Salvando as imagens em arquivos PNG individuais
cv.imwrite('noite-estrelada-gray.png', night_gray)
cv.imwrite('noite-estrelada-negative.png', night_negative_img)
cv.imwrite('noite-estrelada-rgb-merged.png', night_merged_img)
cv.imwrite('noite-estrelada-hsv.png', night_hsv_img)


# %%
