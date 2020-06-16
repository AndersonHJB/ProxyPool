"""
project = 'Code', file_name = 'utils.py', author = 'AI悦创'
time = '2020/6/1 12:34', product_name = PyCharm, 公众号：AI悦创
code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""
import requests
import asyncio
import aiohttp
from requests.exceptions import ConnectionError
from fake_useragent import UserAgent,FakeUserAgentError
import random

def get_page(url, options={}):
	"""
	构造随机请求头，如果不理解的可以阅读此文章：
	两行代码设置 Scrapy UserAgent：https://www.aiyc.top/archives/533.html
	"""
	try:
		ua = UserAgent()
	except FakeUserAgentError:
		pass
	# 生成随机的请求头，加 try...except... 使代码更加健壮
	base_headers = {
		'User-Agent':  ua.random,
		'Accept-Encoding': 'gzip, deflate, sdch',
		'Accept-Language': 'zh-CN,zh;q=0.8'
	}
	# 如果使用者有传入请求头，则将此请求头和随机生成的合成在一起
	headers = dict(base_headers, **options)
	# 当前请求的 url
	# print('Getting', url)
	try:
		r = requests.get(url, headers=headers)
		# print('Getting result', url, r.status_code)
		if r.status_code == 200:
			return r.text
		return None
	except ConnectionError:
		print('Crawling Failed', url)
		return None


class Downloader(object):
	"""
	一个异步下载器，可以对代理源异步抓取，但是容易被 BAN。
	self._htmls: 把请求的 html 放入列表当中
	升级版的请求类
	"""

	def __init__(self, urls):
		self.urls = urls
		self._htmls = []

	async def download_single_page(self, url):
		"""
		下载单页
		"""
		async with aiohttp.ClientSession() as session:
			async with session.get(url) as response:
				self._htmls.append(await response.text())

	def download(self):
		loop = asyncio.get_event_loop()
		tasks = [self.download_single_page(url) for url in self.urls]
		loop.run_until_complete(asyncio.wait(tasks))

	@property
	def htmls(self):
		self.download()
		return self._htmls

