class Company():
	def __init__(self, scode=None, abbr=None, name=None, tel=None, 
		email=None, industry_1=None, industry_2=None, region=None, 
		num_employee=None, income=None, revenue=None):
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


def create_class(info_list):
	company = Company(info_list[0], info_list[1], info_list[2], info_list[3], info_list[4],
					info_list[5], info_list[6], info_list[7], info_list[8], info_list[9], 
					info_list[10])
	return company


#testcase1
test_list = ['001', '乔诺', '上海乔诺企业管理咨询有限公司', '021-11111111', \
			'geonol@geonol.com', 'consulting', 'training', 'Shanghai', '40',\
			'60,000,000', 'unknow']
geonol = create_class(test_list)

print(geonol.scode)


#testcase2
#geonol = Company('001', '乔诺', '上海乔诺企业管理咨询有限公司', '021-11111111', 'geonol@geonol.com', 'consulting', 'training', 'Shanghai', '40','60,000,000', 'unknow')
#print('stock code is:', geonol.scode)

#testcase3
'''test_list = ['001', '乔诺', '上海乔诺企业管理咨询有限公司', '021-11111111', 
			'geonol@geonol.com', 'consulting', 'training', 'Shanghai', '40',
			'60,000,000', 'unknow']

geonol = Company(scode=test_list[0], abbr=test_list[1], name=test_list[2], tel=test_list[3], 
		email=test_list[4], industry_1=test_list[5], industry_2=test_list[6], region=test_list[7], 
		num_employee=test_list[8], income=test_list[9], revenue=test_list[10])'''

print(geonol.abbr)
print(geonol.scode)
print(geonol.name)
print(geonol.revenue)