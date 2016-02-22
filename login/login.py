import requests
from time import sleep
import unittest
import json

class TestLogin(unittest.TestCase):
	def test_login(self):
		#使用session
		s = requests.Session()
		url = 'http://192.168.100.67:8080/szgps/home/home.do?act=getHomeBody'
		r = s.get(url,timeout=10)
		if r.status_code == 200 and '实时在线' in r.text:
			ok = True
		else:
			ok = False

		self.assertTrue(ok)


if __name__ == '__main__':
	unittest.main()