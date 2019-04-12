import jsonpickle
import requests
from jsonpickle import json
from lxml import etree

from fake_useragent import UserAgent

headers = {'User-Agent':UserAgent().chrome}

URL= 'https://static.soufunimg.com/homepage/new/family/css/allcitys2018061301.js?v=20180827'

req = requests.get(URL,headers=headers)
# req.encoding = 'gb2312'
print(req.text)
# e = etree.HTML(req.text)




