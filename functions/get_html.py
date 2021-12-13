# __*__ coding: utf-8 __*__
import requests
import time

waittime = 2

def get_html(url):
	while True:
		try:
			print('break {}s...'.format(waittime))
			time.sleep(waittime)
			html = requests.get(url,timeout = waittime).text
			html = html.encode('latin1').decode('gbk')
			#print('breakpoint')
			return html
		except:
			print('Connecting timeout,waiting for next connect...')

#testcase
'''
url = 'http://quote.eastmoney.com/stocklist.html'
html = get_html(url)
print(html)
'''
#问题：爬取的网页出现乱man
#原因：网页源码为gb2312模式编码（charset=gb2312）
#解决：译码、编码解决（.encode()/.decode())