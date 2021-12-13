# __*__ coding: utf-8 __*__
'''
name: quoted_company_info
author:  Ouyang Shi
version: 2.0
function: collect quoted company's infomation from 'eastmoney.com'
date: 2019/2/8
'''

#import modules
import codecs
import csv
import requests
import time
import bs4

#define global variables
quote_list_url = 'http://quote.eastmoney.com/stocklist.html'

#system testcase
test_head = ['企业简称','企业股票代码','公司名称','注册资本','组织形式','董秘','公司电话','董秘电话','公司邮箱','董秘邮箱','注册地址',
			'所属行业','2018-09-30','2018-06-30','2018-03-31','2017-12-31','2017-09-30']
test_file_name = 'systemtest_fifth.csv'


def build_csv(list,file_name='raw_report_info.csv'):
    with codecs.open(file_name,"w","utf_8_sig") as datacsv:
        csvwriter = csv.writer(datacsv,dialect=("excel"))
        csvwriter.writerow(list)

def url_to_soup(url,watitime = 2,responetime = 2):
	while True:
		try:
			print('break {}s.'.format(watitime))
			time.sleep(watitime)
			html = requests.get(url,timeout = responetime).text
			try:
				html = html.encode('latin1').decode('gbk')	#decode text, from gb2312 to readable
			except:
				pass
			soup = bs4.BeautifulSoup(html,'html.parser')
			return soup
		except:
			print('Connecting timeout, waiting for next connecct...')

def collect_pre_info(url):
	name_list = []
	code_list = []
	url_list = []
	soup = url_to_soup(url)
	for i in soup.find(id='quotesearch').find_all('a'):
		#collect names and codes
		text = i.get_text()
		name_list.append(text[:-8])
		code_list.append(text[-7:-1])
	return name_list, code_list

def check_code(stock_code):
	acode_range = ['600', '601', '603', '000'] #深沪A股
	bcode_range = ['900', '200'] #深沪B股
	ecode_range = ['300']
	ncode_range = ['002']
	if stock_code[0:3] in ecode_range:
		return True
	else:
		return False

def check_quoted_compy(name_list, code_list):
	quoted_cmy_list = []
	for i in range(len(code_list)):
		if check_code(code_list[i]):
			quoted_info = []
			quoted_info.append(name_list[i])
			quoted_info.append(code_list[i])
			#quoted_info.append(url_list[i])
			quoted_cmy_list.append(quoted_info)
	return quoted_cmy_list

def add_to_csv(list,file_name='raw_report_info.csv'):
    with codecs.open(file_name,"a","utf_8_sig") as datacsv:
        csvwriter = csv.writer(datacsv,dialect=("excel"))
        for index in range(len(list)):
            csvwriter.writerow(list[index])

def pre_process(head_list,file_name,url):
	build_csv(head_list,file_name)
	#collect raw info from main page
	raw_name_list, raw_code_list = collect_pre_info(url)
	#filter quoted companies and form a new list
	quoted_cmy_list = check_quoted_compy(raw_name_list, raw_code_list)
	return quoted_cmy_list

def collect_sum_info(stock_code):
	#monitor info
	while True:
		try:
			print('collecting summary info for stock No.{}...'.format(stock_code))
			#those target infomation wanted to collect, which looks like in notes
			target_info_list = [1,15,19,21,23,25,31,33,43]
			sum_url = 'http://vip.stock.finance.sina.com.cn/corp/go.php/vCI_CorpInfo/stockid/' + stock_code + '.phtml'
			sum_soup = url_to_soup(sum_url)
			sum_soup = sum_soup.find(id='con02-0').find_all('td')
			sum_list = []
			for index in range(len(sum_soup)):
				text = sum_soup[index].get_text(strip=True)
				if index in target_info_list:
					sum_list.append(text)
			return sum_list
		except:
			print('collecting fail....waiting for next collect..')

def collect_ind_info(stock_code):
	#monitor info
	while True:
		try:
			print('collecting industry info for stock No.{}...'.format(stock_code))
			#those target infomation wanted to collect, which looks like in notes
			target_info_list = [14]
			ind_url = 'http://vip.stock.finance.sina.com.cn/corp/go.php/vCI_CorpOtherInfo/stockid/' + stock_code + '/menu_num/2.phtml'
			ind_soup = url_to_soup(ind_url)
			ind_soup = ind_soup.find_all('td')
			ind_list = []
			for index in range(len(ind_soup)):
				text = ind_soup[index].get_text(strip=True)
				if index in target_info_list:
					ind_list.append(text)
			return ind_list	
		except:
			print('collecting fail....waiting for next collect..')

def collect_fin_info(stock_code):
	while True:
		try:
			#monitor info
			print('collecting financial info for stock No.{}...'.format(stock_code))
			#those target infomation wanted to collect, which looks like in notes
			target_info_list = [9,10,11,12,13,111,112,113,114,115]
			fin_url = 'http://vip.stock.finance.sina.com.cn/corp/go.php/vFD_ProfitStatement/stockid/' + stock_code + '/ctrl/part/displaytype/4.phtml'
			fin_soup = url_to_soup(fin_url)
			fin_soup = fin_soup.find(id='con02-1').find_all('td')
			fin_list = []
			for index in range(len(fin_soup)):
				text = fin_soup[index].get_text(strip=True)
				if index in target_info_list:
					fin_list.append(text)
			return fin_list
		except:
			print('collecting fail....waiting for next collect..')

def collect_info(quoted_url_list, file_name='raw_report_info.csv'):
	#parameters to control write process
	counter = 0
	csvwriter = []
	for quoted_info in quoted_url_list:
		cmp_info = []
		#briviation of company 
		cmp_info.append(quoted_info[0])
		#stock code of company
		cmp_info.append(quoted_info[1])
		#summary infomation of company
		summary_info_list = collect_sum_info(quoted_info[1])
		#print(summary_info_list)
		for sum_info in summary_info_list:
			cmp_info.append(sum_info)
		industry_info_list = collect_ind_info(quoted_info[1])
		if industry_info_list:
			for ind_info in industry_info_list:
				cmp_info.append(ind_info)
		else:
			cmp_info.append('NA')			
		#financial infomation of company
		financial_info_list = collect_fin_info(quoted_info[1])
		for fin_info in financial_info_list:
			cmp_info.append(fin_info)
		csvwriter.append(cmp_info)
		counter += 1
		#write to csv when all element in list are collected
		if quoted_info is quoted_url_list[-1]:
			add_to_csv(csvwriter, file_name=file_name)
		#write to csv every 50 companies' infomation is collected
		if counter == 10:
			add_to_csv(csvwriter, file_name=file_name)
			#clear counter and writer
			counter = 0
			csvwriter = []

def collect_flow(quoted_cmy_list, file_name='raw_report_info.csv'):
	cmp_list = collect_info(quoted_cmy_list, file_name = file_name)

#main
#pre-process
quoted_cmy_list = pre_process(test_head, test_file_name, quote_list_url)
print('pre-process done!')
print('total number of company is {}.'.format(len(quoted_cmy_list)))
print('head of quoted_cmy_list is :')
print(quoted_cmy_list[0:10])
#collecting flow 
collect_flow(quoted_cmy_list, test_file_name)
print('OK!')