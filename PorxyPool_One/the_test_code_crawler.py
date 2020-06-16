# """
# project = 'Code', file_name = 'test_crawler.py', author = 'AI悦创'
# time = '2020/6/1 13:28', product_name = PyCharm, 公众号：AI悦创
# code is far away from bugs with the god animal protecting
#     I love animals. They taste delicious.
# """
#



class MyList(object):
	def __init__(self, value):
		self.value = value
	def add(self):
		self.data = append()
	



# import re
#
# import requests
# from utils import get_page
# from pyquery import PyQuery as pq
# from db import RedisClient
#
# def kuaidaili():
# 	url = 'https://www.kuaidaili.com/free/inha/1/'
# 	html = get_page(url)
# 	# print(html)
# 	pattern = re.compile('<td data-title="IP">(.*)</td>\s*<td data-title="PORT">(\w+)</td>')
# 	# ip_addres = re.findall(pattern, html) # 写法一
# 	ip_addres = pattern.findall(str(html))
# 	for adress, port in ip_addres:
# 		print(adress, port)
# 		result = f"{adress}:{port}".strip()
# 		yield result
#
# # if __name__ == '__main__':
# # 	a =  kuaidaili()
# # 	for _ in a:
# # 		print(_)
#
#
# def crawl_xicidaili():
# 	for page in range(1, 4):
# 		start_url = 'https://www.xicidaili.com/wt/{}'.format(page)
# 		html = get_page(start_url)
# 		# print(html)
# 		ip_adress = re.compile(
# 			'<td class="country"><img src="//fs.xicidaili.com/images/flag/cn.png" alt="Cn" /></td>\s*<td>(.*?)</td>\s*<td>(.*?)</td>'
# 		)
# 		# \s* 匹配空格，起到换行作用
# 		re_ip_adress = ip_adress.findall(str(html))
# 		for adress, port in re_ip_adress:
# 			result = f"{adress}:{port}".strip()
# 			yield result
#
# # if __name__ == '__main__':
# # 	a = crawl_xicidaili()
# # 	for _ in a:
# # 		print(_)
#
#
# def crawl_daili66(page_count=4):
# 	start_url = 'http://www.66ip.cn/{}.html'
# 	urls = [start_url.format(page) for page in range(1, page_count + 1)]
# 	for url in urls:
# 		print('Crawling', url)
# 		html = get_page(url)
# 		if html:
# 			doc = pq(html)
# 			trs = doc('.containerbox table tr:gt(0)').items()
# 			for tr in trs:
# 				ip = tr.find('td:nth-child(1)').text()
# 				port = tr.find('td:nth-child(2)').text()
# 				yield ':'.join([ip, port])
#
# # if __name__ == '__main__':
# # 	a = crawl_daili66()
# # 	for _ in a:
# # 		print(_)
#
#
#
#
# def crawl_data5u():
# 	start_url = 'http://www.data5u.com'
# 	html = get_page(start_url)
# 	# print(html)
# 	ip_adress = re.compile(
# 		'<ul class="l2">\s*<span><li>(.*?)</li></span>\s*<span style="width: 100px;"><li class=".*">(.*?)</li></span>'
# 	)
# 	# \s * 匹配空格，起到换行作用
# 	re_ip_adress = ip_adress.findall(str(html))
# 	for adress, port in re_ip_adress:
# 		result = f"{adress}:{port}"
# 		yield result.strip()
#
# # if __name__ == '__main__':
# # 	a = crawl_data5u()
# # 	for _ in a:
# # 		print(_)
#
#
#
# def crawl_kxdaili():
# 	"""
# 	开心代理-高匿
# 	:return:
# 	"""
# 	for i in range(1, 4):
# 		start_url = 'http://www.kxdaili.com/dailiip/1/{}.html'.format(i)
# 		try:
# 			html = requests.get(start_url)
# 			if html.status_code == 200:
# 				html.encoding = 'utf-8'
# 				# print(html.text)
# 				ip_adress = re.compile('<tr.*?>\s*<td>(.*?)</td>\s*<td>(.*?)</td>')
# 				# \s* 匹配空格，起到换行作用
# 				re_ip_adress = ip_adress.findall(str(html.text))
# 				for adress, port in re_ip_adress:
# 					result = f"{adress}:{port}"
# 					yield result.strip()
# 			return None
# 		except:
# 			pass
#
# # if __name__ == '__main__':
# # 	a = crawl_kxdaili()
# # 	for _ in a:
# # 		print(_)
#
#
#
# # import re
# # name='\img\黑色长发紫色衬'
# # pattern = re.compile(r"\\img\\(\w+)")
# # name1=re.findall(pattern, name)
# # print(name1)
#
#
# def crawl_premproxy():
# 	headers = {
# 		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
# 		'Host': 'premproxy.com',
# 	}
# 	for i in ['China-01', 'China-02', 'China-03', 'China-04', 'Taiwan-01']:
# 		start_url = 'https://premproxy.com/proxy-by-country/{}.htm'.format(i)
# 	# for page in range(1, 5):
# 	# 	start_url = 'https://premproxy.com/list/0{page}.htm'.format(page = page)
# 		html = get_page(start_url)
# 		print(html)
# 		# if html:
# 		# 	ip_adress = re.compile('<td data-label="IP:port ">(.*?)</td>')
# 		# 	re_ip_adress = ip_adress.findall(str(html))
# 		# 	for adress_port in re_ip_adress:
# 		# 		yield adress_port.replace(' ', '')
#
# # if __name__ == '__main__':
# # 	a = crawl_premproxy()
# # 	for _ in a:
# # 		print(_)
#
#
# MAX_PAGE = 5
#
#
#
# def IP3366Crawler():
# 	"""
# 	云代理
# 	parse html file to get proxies
# 	:return:
# 	"""
# 	start_url = 'http://www.ip3366.net/free/?stype=1&page={page}'
# 	urls = [start_url.format(page=i) for i in range(1, 8)]
# 	# \s * 匹配空格，起到换行作用
# 	ip_address = re.compile('<tr>\s*<td>(.*?)</td>\s*<td>(.*?)</td>')
# 	for url in urls:
# 		html = get_page(url)
# 		re_ip_address = ip_address.findall(str(html))
# 		for adress, port in re_ip_address:
# 			result = f"{adress}:{port}"
# 			yield result.strip()
#
# #
# # if __name__ == '__main__':
# # 	crawler = IP3366Crawler()
# # 	for proxy in crawler:
# # 		print(proxy)
#
#
#
# class PoolAdder(object):
# 	"""
# 	add proxy to pool
# 	"""
#
# 	def __init__(self, threshold):
# 		self.threshold = threshold
# 		self.conn = RedisClient()
# 		self.tester = ValidityTester()
# 		self.crawler = FreeProxyGetter()
#
# 	def is_over_threshold(self):
# 		"""
# 		超过阈值
# 		judge if count is overflow.
# 		"""
# 		if self.conn.queue_len >= self.threshold:
# 			return True
# 		else:
# 			return False
#
# 	def add_to_queue(self):
# 		print('PoolAdder is working')
# 		proxy_count = 0
# 		while not self.is_over_threshold():
# 			for callback_label in range(self.crawler.__CrawlFuncCount__):
# 				callback = self.crawler.__CrawlFunc__[callback_label]
# 				raw_proxies = self.crawler.get_raw_proxies(callback)
# 				# test crawled proxies
# 				self.tester.set_raw_proxies(raw_proxies)
# 				self.tester.test()
# 				proxy_count += len(raw_proxies)
# 				if self.is_over_threshold():
# 					print('IP is enough, waiting to be used')
# 					break
# 			if proxy_count == 0:
# 				raise ResourceDepletionError
