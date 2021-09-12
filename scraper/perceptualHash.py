# example_averagehash.py

# Import dependencies
import os
import numpy

from PIL import Image
import imagehash

img1 = ''


root = '/home/x/specialty/scamDeliverers/zonixlogistics.com/Images'

nums = {}


for img in os.scandir(root):

    imgPath = os.path.join(root, img.name)
    hashCode = imagehash.phash(Image.open(imgPath))

    nums[img.name] = hashCode

for key in nums:
    print("{} : {}".format(key, nums[key]))

import numpy as np



# ['1' '0' '0' '1' '1' '0']

#
# # Create the Hash Object of the first image
# HDBatmanHash = imagehash.phash(Image.open('/home/x/dissertation/legitDeliverers/ivhq8.com/Images/image12'))
# print('Batman HD Picture: ' + str(HDBatmanHash))
#
# # Create the Hash Object of the second image
# SDBatmanHash = imagehash.phash(Image.open('/home/x/dissertation/legitDeliverers/ivhq8.com/Images/image12'))
# print('Batman HD Picture: ' + str(SDBatmanHash))
#
# # Compare hashes to determine whether the pictures are the same or not
# if(HDBatmanHash == SDBatmanHash):
#     print("The pictures are perceptually the same !")
# else:
#     print("The pictures are different, distance: " + (HDBatmanHash - SDBatmanHash))