import requests
import json
import pprint

serviceKey = '/Uc44UJfRtWB6WzFmX+iCtuNPySS+w1EZLyzZPcL5Yz2VVjNCoqrjEKAAxtGfAzOfhLj72IdwUy3FO0RYsRFsQ=='
url = 'http://apis.data.go.kr/C100006/zerocity/getCctvList/event/2DBoundingBox'
params ={'serviceKey' : serviceKey, 'type' : '', 'numOfRows' : '1', 'pageNo' : '1', 'eventType' : '03', 'startDt' : '2015-07-02', 'endDt' : '2022-09-01' }
response = requests.get(url, params=params)
json_data = json.loads(response.content)
pprint.pprint(json_data, width=40)
