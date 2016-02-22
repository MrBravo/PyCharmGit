import requests
import HTMLTestRunner
import json
import unittest


class MyTest(unittest.TestCase):
	def setUp(self):
		#生成session
		self.s = requests.Session()
		#登录地址
		self.url ='http://192.168.100.67:8080/szgps/login/login.do?act=login'
		#self.getData = {'act':'login','ts':'1449538441380'}
		self.postData = {'loginForce':'1','loginName':'firefox','loginPwd':'ab067c7db857f90c60ce5fbf60b1258411f29dc7','imgCode':'','isShow':'n'}
		#self.s.post(self.url,data=self.postData)
		try:
			self.s.post(self.url,data=self.postData)
		except:
			print('登录失败!')
		else:
			#print('登录成功!')
			pass

	#------------------ 查询车辆 ----------------
	def testQueryAllVehicle(self):
		''' 查询所有车辆 '''
		url = 'http://192.168.100.67:8080/szgps/stat/vehBuinsTab.do?queryType=basic&act=getTab'
		#查询所有车辆
		#allCar = {'strTabRowConditionPara':'srchNull','page':'1','pagesize':'20'}
		car555 = {'strTabRowConditionPara':'1`busNumber`车牌号码`555``1`companyName`业户名称`集团``9`vehOfProfessionNo`所属行业`012---包车客运-=-900---其他','page':'1','pagesize':'20'}

		car = self.s.post(url,data=car555)
		carDict = json.loads(car.text)
		cars = carDict['Rows']
		ok = True
		for d in cars:
			print(d['busNumber'],d['companyName'])
			if '555' not in d['busNumber'] or '集团' not in d['companyName']:
				ok = False
				break

		self.assertTrue(ok)



		#直接用get 是无法获取的,
		#url = 'http://192.168.100.67:8080/szgps/stat/vehBuinsTab.do?queryType=basic&act=getTab&strTabRowConditionPara=1`busNumber`车牌号码`555``1`companyName`业户名称`集团'
		# car = s.get(url)
		# carDict = json.loads(car.text)
		# cars = carDict['Rows']

if __name__ == '__main__':
	suite = unittest.TestSuite()
	suite.addTest(MyTest('testQueryAllVehicle'))

	#runner = unittest.TextTestRunner()
	logFile = open(r'D:\autoTestReport.html','w+') #保存测试报告
	runner = HTMLTestRunner.HTMLTestRunner(stream=logFile,description="自动测试结果",title="自动化测试车辆查询报告")
	runner.run(suite)
	logFile.close()