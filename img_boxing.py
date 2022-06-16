from PIL import Image, ImageDraw
import random

url = json_data[0]['cctvfileList'][0]['image_flph']
img_path= 'test.jpg'
json_path = 'test.json'
class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"
urllib._urlopener = AppURLopener()
urllib._urlopener.retrieve(url, img_path)

url_json = json_data[0]['cctvfileList'][0]['cctv_json_stor_flph']
response = requests.get(url_json)

json_data1 = json.loads(response.content)
#pprint.pprint(json_data1, width=40)
bbox = json_data1['annotations'][0]['info']
bbox1 = json_data1['annotations']

img = Image.open(img_path).convert('RGB')
draw = ImageDraw.Draw(img)
for i in range(0, len(bbox1)):
  draw.rectangle((json_data1['annotations'][i]['info'][0],
                  json_data1['annotations'][i]['info'][1],
                  json_data1['annotations'][i]['info'][0]
                  +json_data1['annotations'][i]['info'][2],
                  json_data1['annotations'][i]['info'][1]
                  +json_data1['annotations'][i]['info'][3]),
                  outline=(random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)), width = 3)
img.show()
img
