import skimage
from skimage.feature import daisy

from skimage import data
import matplotlib.pyplot as plt


img = skimage.io.imread('resized.bmp')
descs, descs_img = daisy(img, visualize=True)
print(descs.shape)
fig, ax = plt.subplots()
ax.axis('off')
ax.imshow(descs_img)
descs_num = descs.shape[0] * descs.shape[1]
ax.set_title('%i DAISY descriptors extracted:' % descs_num)
plt.show()