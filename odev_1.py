import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
img = cv.imread ("north.jpg",0)
img_yukseklik = img.shape[0]
img_genislik = img.shape[1]
Histogram =np.zeros([256])
for x in range (0,img_yukseklik):
    for y in range (0,img_genislik):
        Histogram [img[x,y]] +=1
plt.plot(Histogram)
plt.title("Histogram")
plt.show()