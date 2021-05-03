import numpy as np
from scipy import ndimage as ndi
from skimage.io import imread
from skimage.color import rgb2gray
import os

dire = '/home/kuba/Downloads'
os.chdir(dire)

img = rgb2gray(imread('comic(1).png'))
w,h = img.shape

