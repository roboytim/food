import requests
from bs4 import  BeautifulSoup
from datetime import datetime
import json
import re
import pandas

res = requests.get('https://www.ele.me/restapi/shopping/restaurants?extras%5B%5D=activities&geohash=wx4g933m9xj4&latitude=39.998083&limit=24&longitude=116.423907&offset=0&terminal=web')
res.encoding = 'utf-8'

jd = json.loads(res.text)
for i in range(len(jd)):
    print(jd[i]['activities'])