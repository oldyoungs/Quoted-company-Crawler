# __*__ coding: utf-8 __*__
'''
name: quoted_company_info
author:  Ouyang Shi
version: 2.0
function: collect quoted company's infomation from 'eastmoney.com'
date: 2019/2/8
'''

#import modules
from pre_process import pre_process
from collect_flow import collect_flow
#import post_process

#define global variables
quote_list_url = 'http://quote.eastmoney.com/stocklist.html'


#system testcase
test_head = ['企业简称','企业股票代码','URL链接','概况信息'，'财务信息']
test_file_name = 'systemtest_fir.csv'

#main
#pre-process
quoted_cmy_list = pre_process(test_head, test_file_name, quote_list_url)
#collecting flow 
collect_flow(quoted_cmy_list, test_file_name)
print('system test pass')