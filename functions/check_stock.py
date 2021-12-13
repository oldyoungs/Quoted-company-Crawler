import unittest

def check_stock(stock_code):
	acode_range = ['600', '601', '603', '000'] #深沪A股
	bcode_range = ['009', '200'] #深沪B股
	ecode_range = ['300']
	ncode_range = ['002']
	if stock_code[0:3] in acode_range:
		return True
	else:
		return False

#testcase1
print(check_stock('603885'))#True
print(check_stock('500002'))
print(check_stock('900901'))
print(check_stock('000035'))#True
print(check_stock('002524'))
print(check_stock('150001'))
print(check_stock('201004'))
print(check_stock('123456'))
print(check_stock('654321'))

#testcase2
'''result = check_stock('603885')
unittest.TestCase.assertIs(result, True)'''