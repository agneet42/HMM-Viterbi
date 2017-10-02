import skimage
from skimage.feature import daisy
from skimage import data
import matplotlib.pyplot as plt
import os
import numpy as np
import csv

file = csv.writer(open("featurefile1.csv",'a'))

s = os.listdir()
for i in s:
	if(i[0]=='r'):
		img = skimage.io.imread(i)
		descs, descs_img = daisy(img, visualize=True)
		arr_to_write = []
		for row in range(0,5):
			for col in range(0,5):
				arr = descs[row][col]
				arr1,extra = np.histogram(arr,bins =10)
				# print(type(arr1))
				arr_to_write = np.append(arr_to_write,arr1)
		arr_to_write = arr_to_write.astype(np.int64)
		arr_to_write = arr_to_write.tolist()
		arr_to_write.append('A49') # to be changed as per class name
		file.writerow(arr_to_write)
