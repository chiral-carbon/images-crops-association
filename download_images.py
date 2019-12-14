import urllib.request
import numpy as np
import cv2
import os
from tqdm import tqdm

if not os.path.exists('images'):
    os.mkdir('images')
if not os.path.exists('crops'):
    os.mkdir('crops')

IMGFOLDER = os.getcwd() + '/images/'
CROPSFOLDER = os.getcwd() + '/crops/'

images_url = "https://bit.ly/2JcmBIU"
crops_url = "https://bit.ly/2DYz9iw"

images_data = urllib.request.urlopen(images_url)
crops_data = urllib.request.urlopen(crops_url)

images = []; crops = []

for url in images_data:
    images.append(url.decode('utf-8'))

for url in crops_data:
    crops.append(url.decode('utf-8'))

print("Number of images:", len(images))
print("Number of crops: ", len(crops))

def downloadImage(url, idx, type, foldername):
    try:
        #print("Downloading ", url)
        img_name = type+"_name_"+str(idx)+".jpg"
        response = urllib.request.urlopen(url)
        img = np.asarray(bytearray(response.read()), dtype="uint8")
        img = cv2.imdecode(img, cv2.IMREAD_COLOR)
        cv2.imwrite(foldername + img_name, img)
    except Exception as error:
        print(error)

print("Downloading images")
for idx in tqdm(range(len(images))):
    downloadImage(images[idx], idx+1, "image", IMGFOLDER)

print("Downloading image crops")
for idx in tqdm(range(len(crops))):
    downloadImage(crops[idx], idx+1, "crop", CROPSFOLDER)