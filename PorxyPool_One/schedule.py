"""
project = 'Code', file_name = 'test.py', author = 'AI悦创'
time = '2020/5/30 18:47', product_name = PyCharm, 公众号：AI悦创
code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""
import asyncio
import time
from multiprocessing.context import Process

import aiohttp
from db import RedisClient
from Spider import FreeProxyGetter
from error import ResourceDepletionError
from aiohttp import ServerDisconnectedError, ClientResponseError, ClientConnectorError
from socks import ProxyConnectionError

get_proxy_timeout = 9


class ValidityTester(object):
	"""
	代理的有效性测试
	"""
	def __init__(self):
		self.raw_proxies = None
		self.usable_proxies = [] # 可用代理
		self.test_api = 'http://www.baidu.com'

	def set_raw_proxies(self, proxies):
		self.raw_proxies = proxies # 临时存储一些代理


	async def test_single_proxy(self, proxy):
		"""
		python3.5 之后出现的新特性
		text one proxy, if valid, put them to usable_proxies.
		"""
		try:
			async with aiohttp.ClientSession() as session:
				try:
					if isinstance(proxy, bytes):
						proxy = proxy.decode('utf-8')
					real_proxy = 'http://' + proxy
					print('Testing', proxy)
					async with session.get(self.test_api, proxy=real_proxy, timeout=get_proxy_timeout) as response:
						if response.status == 200:
							print('Valid proxy', proxy)
				except (ProxyConnectionError, TimeoutError, ValueError):
					print('Invalid proxy', proxy)
		except (ServerDisconnectedError, ClientResponseError, ClientConnectorError) as s:
			print(s)
			pass

	def test(self):
		"""
		aio test all proxies.
		"""
		print('ValidityTester is working')
		try:
			loop = asyncio.get_event_loop()
			tasks = [self.test_single_proxy(proxy) for proxy in self.raw_proxies]
			loop.run_until_complete(asyncio.wait(tasks))
		except ValueError:
			print('Async Error')



class Schedule(object):
	@staticmethod
	def valid_proxy():
		"""
		Get half of proxies which in Spider
		"""
		tester = ValidityTester()
		free_proxy_getter = FreeProxyGetter()
		# 获取 Spider 数据库数据
		# 调用测试类
		tester.set_raw_proxies(free_proxy_getter.run())
		# 开始测试
		tester.test()



	def run(self):
		print('Ip processing running')
		valid_process = Process(target=Schedule.valid_proxy) # 获取代理并筛选
		valid_process.start()
if __name__ == '__main__':
	schedule = Schedule().run()