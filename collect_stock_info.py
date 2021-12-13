# __*__ coding: utf-8 __*__

'''
name: collect_stock_info
author: Ouyang Shi
version: 1.0
function: collect infomation of stocks
date: 2019-2-1
'''

#initialization
##import modules
import requests
import time
import bs4
import csv
import codecs
import random
##define global variables
waittime = 2
stock_url_list = []
stock_code_url = 'http://quote.eastmoney.com/stocklist.html'
##build class
class Company:
	def __int__(self, scode, abbr, name, tel, email, industry_1, industry_2, region, num_employee, income, revenue):
		self.scode = scode
		self.abbr = abbr
		self.name = name
		self.tel = tel
		self.email = email
		self.industry_1 = industry_1
		self.industry_2 = industry_2
		self.region = region
		self.num_employee = num_employee
		self.income = income
		self.revenue = revenue


#function definition
#---MODULES---
#initialization
def initialization():
	#初始化模块

#collect_info
def collect_info(url):
	#爬取信息模块
	html = get_html(url)


#output_data
def output_data():
	#输出数据模块

#---FUNCTIONS---
#general function
def get_html(url):
	#获取html
    while True:
        try:
            print('break {}s...'.format(waittime))
            time.sleep(waittime)
            html = requests.get(url,timeout = waittime).text
            return(html)
        except:
            print('Connecting timeout,waiting for next connect...')

#create_class
def create_class():
	#创建类

#collect_detail_flow
def collect_detail_flow(url):
	#爬取企业信息流程控制
	raw_list = []
	list_html = get_html(url)
	#find all urls in html
	#append all url into raw_list
	#loop start
	#fetch one url in raw_list, which is define as stock_url
	stock_html = get_html(stock_url)
	if check_stock():
		collect_short_names(stock_html)
		#collect url for brief and finance
		collect_brief(brief_url)
		collect_finance(finance_url)
		#keep the right url

#check_stock
def check_stock():
	#确认股票正确性
	#find infomation to check the url is validity or not
	if validity:
		return True
	else:
		return False

#collect_short_names
def collect_short_names(html):
	#爬取企业简称名录
	#collect brief name
	#collect code

#collect_brief
def collect_brief(url):
	#爬取企业概况
	html = get_html(url)
	#find company name
	#find telephone
	#find email
	#find industries type 1
	#find industries type 2
	#find location
	#find num of employees
	#write to class

#collect_finance
def collect_finance(url):
	#爬取企业财务
	html = get_html(url)
	#adapt to annual data mode
	#find total income
	#find revenue
	#write to class

#build_csv
def build_csv(list):
	#创建表格文档
	with codecs.open("raw_report_info.csv","w","utf_8_sig") as datacsv:
        csvwriter = csv.writer(datacsv,dialect=("excel"))
        csvwriter.writerow(list)

#write_to_csv
def write_to_csv():
	#写入文档

#exception_report
def exception_report():
	#打印错误

#main
#1. initialization
#1.1 create_class

#2. collect_info
#2.1 check_stock
#2.2 collect_flow

#3. ouput
#3.1 build_csv
#3.2 write_to_csv
#3.3 exception_report
