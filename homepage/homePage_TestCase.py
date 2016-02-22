import requests
from time import sleep
import unittest
import json


s = requests.Session()

url = 'http://192.168.100.67:8080/szgps/home/home.do?act=getHomeBody'

r = s.get(url,timeout=10)
if '实时在线' in r.text:
	print('登录成功')


url = 'http://192.168.100.67:8080/szgps/stat/vehBuinsTab.do?queryType=basic&act=getTab'
car555 = {'strTabRowConditionPara':'1`busNumber`车牌号码`555``1`companyName`业户名称`集团``9`vehOfProfessionNo`所属行业`012---包车客运-=-900---其他','page':'1','pagesize':'20'}

car = s.post(url,data=car555)
print(car.text)
#carDict = json.loads(car.text)
#cars = carDict['Rows']