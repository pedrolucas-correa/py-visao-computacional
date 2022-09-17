#%% 1 Lendo a imagem
import cv2
import numpy as np 
from matplotlib import pyplot as plt 
from IPython.display import Image
from PIL import Image 

baloes_img = cv2.imread('baloes.png', 1)

# %% Histograma padrão

h = cv2.calcHist([baloes_img], [0], None, [256], [0, 256])
plt.figure()
plt.title('Histograma P&B')
plt.xlabel('Intensidade')
plt.ylabel('Qtde de pixels')
plt.plot(h)
plt.xlim([0,256])
plt.show()

# %% Histograma RGB

# baloes_img = cv2.imread('baloes.png', 1)
# baloes_img = baloes_img[:,:,::-1] 

canais = cv2.split(baloes_img)
cores = ('b', 'g', 'r')

plt.figure()
plt.title('Histograma RGB')
plt.xlabel('Intensidade')
plt.ylabel('Qtde de pixels')
for (canal, cor) in zip(canais, cores):
    hist = cv2.calcHist([canal], [0], None, [256], [0,256])
    plt.plot(hist, cor)
    plt.xlim([0,256])
plt.show()

# %% Equalize

baloes_gray_img = cv2.cvtColor(baloes_img, cv2.COLOR_BGR2GRAY)
h_eq = cv2.equalizeHist(baloes_gray_img)

plt.figure()
plt.title("Histograma Equalizado")
plt.xlabel("Intensidade")
plt.ylabel("Qtde de Pixels")
plt.hist(h_eq.ravel(), 256, [0,256])
plt.xlim([0,256])
plt.show()

plt.figure()
plt.title("Histograma Original")
plt.xlabel('Intensidade')
plt.ylabel('Qtde de pixels')
plt.hist(baloes_gray_img.ravel(), 256, [0,256])
plt.xlim([0,256])
plt.show()
cv2.waitKey(0)

plt.imshow(h_eq, cmap="gray")

# %% Aproximando imagem

cropped_region = baloes_img[100:800, 150:900]
plt.imshow(cropped_region[:,:,::-1])


# %% Desenhando um circulo

baloesCircle =  cropped_region

cv2.circle(baloesCircle, (250,270), 250, (0, 0, 255), thickness=5, lineType=cv2.LINE_AA);

plt.imshow(baloesCircle[:,:,::-1])
# %%
