"""
project = 'Code', file_name = 'Spider.py', author = 'AI悦创'
time = '2020/6/1 12:33', product_name = PyCharm, 公众号：AI悦创
code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""
import requests

from utils import get_page
from pyquery import PyQuery as pq
import re



class ProxyMetaclass(type):
	"""
	定义 ProxyMetaclass ，按照默认习惯，metaclass 的类名总是以 Metaclass 结尾，以便清楚地表示这是一个metaclass ：
	元类，在 FreeProxyGetter 类中加入
	CrawlFunc_list 和 CrawlFuncCount
	两个参数，分别表示爬虫函数，和爬虫函数的数量。
	"""
	def __new__(cls, name, bases, attrs):
		count = 0
		attrs['CrawlFunc_List'] = [] # 添加：CrawlFunc_List 列表方法
		for k, v in attrs.items():
			if 'crawl_' in k:
				# 判断这个函数里面是否携带 crawl_ 也就是利用 value in xxx
				attrs['CrawlFunc_List'].append(k)
				count += 1
		attrs['CrawlFuncCount'] = count # 检测添加的函数的总数量
		return type.__new__(cls, name, bases, attrs) # 返回所修改的



class FreeProxyGetter(object, metaclass=ProxyMetaclass):
	"""
	免费代理获取
	1. 快代理
	2. 西刺代理
	3. 66代理
	4. 无忧代理
	5. 开心代理-高匿
	6. 云代理
	"""
	# def get_raw_proxies(self, callback):
	# 	proxies = []
	# 	print('Callback', callback)
	# 	for proxy in eval("self.{}()".format(callback)):
	# 		print('Getting', proxy, 'from', callback)
	# 		proxies.append(proxy)
	# 	return proxies
	
	def run(self):
		# print(self.__CrawlFunc__)
		proxies = []
		callback = self.CrawlFunc_List
		for i in callback:
			# print('Callback', i)
			for proxy in eval("self.{}()".format(i)):
				# print('Getting', proxy, 'from', i)
				proxies.append(proxy)
		return proxies
		# return self.__CrawlFunc__
	
	# 代理网站已废
	# def crawl_ip181(self):
	# 	start_url = 'http://www.ip181.com/'
	# 	html = get_page(start_url)
	# 	ip_adress = re.compile('<tr.*?>\s*<td>(.*?)</td>\s*<td>(.*?)</td>')
	# 	# \s* 匹配空格，起到换行作用
	# 	re_ip_adress = ip_adress.findall(str(html))
	# 	for adress, port in re_ip_adress:
	# 		result = adress + ':' + port
	# 		yield result.replace(' ', '')

	def crawl_kuaidaili(self):
		"""
		快代理
		:return:
		"""
		for page in range(1, 4):
			# 国内高匿代理
			start_url = 'https://www.kuaidaili.com/free/inha/{}/'.format(page)
			html = get_page(start_url)
			# print(html)
			pattern = re.compile(
				'<td data-title="IP">(.*)</td>\s*<td data-title="PORT">(\w+)</td>'
			)
			# \s * 匹配空格，起到换行作用
			# ip_addres = re.findall(pattern, html) # 写法一
			ip_addres = pattern.findall(str(html))
			for adress, port in ip_addres:
				# print(adress, port)
				result = f"{adress}:{port}".strip()
				yield result
	
	def crawl_xicidaili(self):
		"""
		西刺代理
		:return:
		"""
		for page in range(1, 4):
			start_url = 'https://www.xicidaili.com/wt/{}'.format(page)
			html = get_page(start_url)
			# print(html)
			ip_adress = re.compile(
				'<td class="country"><img src="//fs.xicidaili.com/images/flag/cn.png" alt="Cn" /></td>\s*<td>(.*?)</td>\s*<td>(.*?)</td>'
			)
			# \s* 匹配空格，起到换行作用
			re_ip_adress = ip_adress.findall(str(html))
			for adress, port in re_ip_adress:
				result = f"{adress}:{port}".strip()
				yield result
	
	def crawl_daili66(self, page_count=4):
		"""
		66代理
		:param page_count:
		:return:
		"""
		start_url = 'http://www.66ip.cn/{}.html'
		urls = [start_url.format(page) for page in range(1, page_count + 1)]
		for url in urls:
			# print('Crawling', url)
			html = get_page(url)
			if html:
				doc = pq(html)
				trs = doc('.containerbox table tr:gt(0)').items()
				for tr in trs:
					ip = tr.find('td:nth-child(1)').text()
					port = tr.find('td:nth-child(2)').text()
					yield ':'.join([ip, port])
	
	def crawl_data5u(self):
		"""
		无忧代理
		:return:
		"""
		start_url = 'http://www.data5u.com'
		html = get_page(start_url)
		# print(html)
		ip_adress = re.compile(
			'<ul class="l2">\s*<span><li>(.*?)</li></span>\s*<span style="width: 100px;"><li class=".*">(.*?)</li></span>'
		)
		# \s * 匹配空格，起到换行作用
		re_ip_adress = ip_adress.findall(str(html))
		for adress, port in re_ip_adress:
			result = f"{adress}:{port}"
			yield result.strip()
	
	def crawl_kxdaili(self):
		"""
		开心代理-高匿
		:return:
		"""
		for i in range(1, 4):
			start_url = 'http://www.kxdaili.com/dailiip/1/{}.html'.format(i)
			try:
				html = requests.get(start_url)
				if html.status_code == 200:
					html.encoding = 'utf-8'
					# print(html.text)
					ip_adress = re.compile('<tr.*?>\s*<td>(.*?)</td>\s*<td>(.*?)</td>')
					# \s* 匹配空格，起到换行作用
					re_ip_adress = ip_adress.findall(str(html.text))
					for adress, port in re_ip_adress:
						result = f"{adress}:{port}"
						yield result.strip()
				return None
			except:
				pass
	
	def IP3366Crawler(self):
		"""
		云代理
		parse html file to get proxies
		:return:
		"""
		start_url = 'http://www.ip3366.net/free/?stype=1&page={page}'
		urls = [start_url.format(page=i) for i in range(1, 8)]
		# \s * 匹配空格，起到换行作用
		ip_address = re.compile('<tr>\s*<td>(.*?)</td>\s*<td>(.*?)</td>')
		for url in urls:
			html = get_page(url)
			re_ip_address = ip_address.findall(str(html))
			for adress, port in re_ip_address:
				result = f"{adress}:{port}"
				yield result.strip()
	
	# 此代理需要科学上网，代码仅供参考
	# def crawl_premproxy(self):
	# 	for i in ['China-01', 'China-02', 'China-03', 'China-04', 'Taiwan-01']:
	# 		start_url = 'https://premproxy.com/proxy-by-country/{}.htm'.format(
	# 			i)
	# 		html = get_page(start_url)
	# 		if html:
	# 			ip_adress = re.compile('<td data-label="IP:port ">(.*?)</td>')
	# 			re_ip_adress = ip_adress.findall(str(html))
	# 			for adress_port in re_ip_adress:
	# 				yield adress_port.replace(' ', '')

	# 此代理网站需要科学上网
	# def crawl_xroxy(self):
	# 	for i in ['CN', 'TW']:
	# 		start_url = 'http://www.xroxy.com/proxylist.php?country={}'.format(
	# 			i)
	# 		html = get_page(start_url)
	# 		if html:
	# 			ip_adress1 = re.compile(
	# 				"title='View this Proxy details'>\s*(.*).*")
	# 			re_ip_adress1 = ip_adress1.findall(str(html))
	# 			ip_adress2 = re.compile(
	# 				"title='Select proxies with port number .*'>(.*)</a>")
	# 			re_ip_adress2 = ip_adress2.findall(html)
	# 			for adress, port in zip(re_ip_adress1, re_ip_adress2):
	# 				adress_port = adress + ':' + port
	# 				yield adress_port.replace(' ', '')
if __name__ == '__main__':
	Tester = FreeProxyGetter()
	Tester.run()
# proxies = []
# for callback in a.run():
# 	# print(type(callback))
# 	print('Callback', callback)
# 	for proxy in eval("{}()".format(callback)):
# 		print('Getting', proxy, 'from', callback)
# 		proxies.append(proxy)
# 	# return proxies
# print(proxies)