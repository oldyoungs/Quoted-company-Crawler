# __*__ coding: utf-8 __*__
import bs4
import time
from get_html import get_html

def collect_short_names(html):
	name_list = []
	code_list = []
	soup = bs4.BeautifulSoup(html,'html.parser')
	for i in soup.find(id='quotesearch').find_all('a'):
		text = i.get_text()
		name_list.append(text[:-8])		
		code_list.append(text[-7:-1])
	return name_list, code_list


#testcase
switch = False
if switch is True:
	url = 'http://quote.eastmoney.com/stocklist.html'
	html = get_html(url)
	name_list, code_list = collect_short_names(html)
	print(name_list[0],code_list[0])