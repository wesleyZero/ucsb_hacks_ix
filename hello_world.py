import numpy as np
# import pandas as pd  
import cv2
from PIL import Image
from matplotlib import pyplot as plt 


import sys
# sys.path.append('newfolder/')
import newmod
newmod.my_class().something()


sys.path.append('new_folder/')
import otherdir
otherdir.my_class().something()

print("beg of the file")
# location = './img/cheater.jpg'
location = "./pikachu.jpg"
cheater_img = cv2.imread(location, cv2.IMREAD_COLOR)

img0 = Image.open(location)
# img0.show("using PIL")







# cv2.imshow("cheater", cheater_img)
# cv2.waitKey(10)
# cv2.destroyAllWindows()

print("hello ucsb hacks helloo hey")




