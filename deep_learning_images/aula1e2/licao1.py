# -*- coding: utf-8 -*-
"""Licao1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1W26mN6meWnvtrY2ZxWL9Qb0jFyPYDqdS

# Aula 1
"""

from google.colab import drive
drive.mount("/content/drive")

# Commented out IPython magic to ensure Python compatibility.
# %cd "/content/drive/My Drive/PSI3472/aula1"

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline

import cv2

img = cv2.imread("download.jpeg")

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img);

img = cv2.resize(img, (100,100))

plt.imshow(img)

cv2.imwrite("spfc_transformado.png", img)