import requests
import json
import pprint
import pandas as pd


serviceKey = '/Uc44UJfRtWB6WzFmX+iCtuNPySS+w1EZLyzZPcL5Yz2VVjNCoqrjEKAAxtGfAzOfhLj72IdwUy3FO0RYsRFsQ=='
url = 'http://apis.data.go.kr/C100006/zerocity/getCctvList/event/2DBoundingBox'
params ={'serviceKey' : serviceKey, 'type' : '', 'numOfRows' : '1000', 'pageNo' : '1', 'eventType' : '03', 'startDt' : '2019-07-02', 'endDt' : '2022-05-01' }
response = requests.get(url, params=params)
json_data1 = json.loads(response.content)
params ={'serviceKey' : serviceKey, 'type' : '', 'numOfRows' : '1000', 'pageNo' : '2', 'eventType' : '04', 'startDt' : '2019-07-02', 'endDt' : '2022-05-01' }
response = requests.get(url, params=params)
json_data2 = json.loads(response.content)
params ={'serviceKey' : serviceKey, 'type' : '', 'numOfRows' : '1000', 'pageNo' : '3', 'eventType' : '07', 'startDt' : '2019-07-02', 'endDt' : '2022-05-01' }
response = requests.get(url, params=params)
json_data3 = json.loads(response.content)
params ={'serviceKey' : serviceKey, 'type' : '', 'numOfRows' : '1000', 'pageNo' : '4', 'eventType' : '02', 'startDt' : '2019-07-02', 'endDt' : '2022-05-01' }
response = requests.get(url, params=params)
json_data4 = json.loads(response.content)

# pprint.pprint(json_data, width=40)
json_data = json_data1
url_json = json_data[0]['cctvfileList'][0]['cctv_json_stor_flph']
for i in range(0, len(json_data[0]['cctvfileList'])):
  url_json = json_data[0]['cctvfileList'][i]['cctv_json_stor_flph']
  response = requests.get(url_json)
  json_data_t = json.loads(response.content)
  print(json_data[0]['cctvfileList'][i]['recd_strt_dt'], 
        json_data[0]['cctvfileList'][i]['recd_end_dt'], 
        json_data[0]['cctvfileList'][i]['cctv_fclt_id'],
        len(json_data_t['annotations']))






