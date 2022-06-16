import os
import time
import urllib.request
import PIL.Image as pil

url = json_data[0]['cctvfileList'][0]['image_flph']

img_path= 'test.jpg'
json_path = 'test.json'
class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"
urllib._urlopener = AppURLopener()
urllib._urlopener.retrieve(url, img_path)

img = pil.open(img_path)
img
