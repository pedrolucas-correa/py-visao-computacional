#%% 1 Lendo a imagem
import cv2
import numpy as np 
from matplotlib import pyplot as plt 
from IPython.display import Image

baloes_img = cv2.imread('baloes.png', 1)
baloes_img = baloes_img[:,:,::-1] 
plt.imshow(baloes_img)

# %% Separando os canais

b,g,r = cv2.split(baloes_img)


# %% Histograma padrão

h = cv2.calcHist([baloes_img], [0], None, [256], [0, 256])
plt.figure()
plt.title('Histograma P&B')
plt.xlabel('Intensidade')
plt.ylabel('Qtde de pixels')
plt.plot(h)
plt.xlim([0,256])
plt.show()
cv2.waitKey(0)

# %% Histograma RGB

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

# %%
