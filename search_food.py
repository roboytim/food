import requests
from bs4 import  BeautifulSoup
from datetime import datetime
import json
import re
import pandas

def getIndex(url):
    res = requests.get(url)
    res.encoding = 'utf-8'
    jd = json.loads(res.text)
    res_list = []
    for i in jd:
        res_info = {}
        res_info['name'] = i.get('name')
        res_info['address'] = i.get('address')
        res_info['id'] = i.get('id')
        res_info['rating'] = i.get('rating')
        res_info['piecewise_agent_fee'] = i.get('piecewise_agent_fee')['description']
        res_list.append(res_info)
    return res_list
def getDetail(id):
    url = 'https://www.ele.me/restapi/shopping/v2/menu?restaurant_id={}'
    newurl = url.format(id)
    res = requests.get(newurl)
    res.encoding = 'utf-8'
    jd = json.loads(res.text)
    foods_list = []
    #print(res.text)
    for i in jd:
        print(len(i.get('foods')))
        for j in i.get('foods'):
            foods_info = {}
            foods_info['name'] = j['name']
            foods_info['rating'] = j['rating']
            foods_info['tip'] = j['tips']
            foods_info['description'] = j['description']
            foods_info['virtual_food_id'] = j['virtual_food_id']
            foods_list.append(foods_info)
    return foods_list
df = pandas.DataFrame(getIndex('https://www.ele.me/restapi/shopping/restaurants?extras%5B%5D=activities&geohash=wx4g933m9xj4&latitude=39.998083&limit=24&longitude=116.423907&offset=0&terminal=web'))
#print(df.sort_values(by='rating',ascending=False).head(20))
df2 = pandas.DataFrame(getDetail(150099552))
print(df2.sort_values(by='rating',ascending=False).head(20))