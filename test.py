import numpy as np
import matplotlib.image as mpimg
import cv2
import pandas as pd
import os
from PIL import Image

image = Image.open("data\\0.png")
image = image.convert(mode='RGB')
X = np.asarray(image)
print(X)
while(True):
    pass