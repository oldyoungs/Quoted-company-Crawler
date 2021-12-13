#coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr
import csv
import codecs

smtp_server = 'smtp.exmail.qq.com'
from_addr = 'oliver.ou@geonol.com'
password = 'GWURizYeuqMEhsAE'  #这是你邮箱的第三方授权客户端密码，并非你的登录密码
csv_file = 'quoted_company_List.csv' #读取数据的列表
error_report_file = 'error_report.txt'
#for test
#csv_file = 'Book1.csv'

#邮件内容编辑
def edit_text(reciever):
	name_content = '尊敬的董事会秘书{}总，'.format(reciever[0:1])
	name_content = bytes(name_content, 'utf8')
	name_content = name_content.decode('utf8')
	front = '''<html>\
			<head>\
			<style class="fox_global_style">div.fox_html_content { line-height: 1.5; }ol, ul { margin-top: 0px; margin-bottom: 0px; list-style-position: inside; }div.fox_html_content { font-size: 10.5pt; font-family: 微软雅黑; color: rgb(0, 0, 0); line-height: 1.5; }div.fox_html_content { font-size: 10.5pt; font-family: 微软雅黑; color: rgb(0, 0, 0); line-height: 1.5; }</style>\
			</head>\
			<body>\
			<div>\
			<span></span>\
			<span style="color: rgb(0, 0, 0); background-color: rgba(0, 0, 0, 0);"></span>\
			<span style="color: rgb(0, 0, 0); background-color: rgba(0, 0, 0, 0);"></span> \
			</div>\
			<div>\
			<font face="Microsoft YaHei UI"><span style="font-size: 10.5pt; line-height: 1.5; background-color: transparent;">您好，</span><span style="font-size: 10.5pt; line-height: 1.5; background-color: transparent;">'''
	tail = '''
			</span></font>\
			</div>\
			<div>\
			<span style="font-size: 10.5pt; line-height: 1.5; background-color: transparent;"><font face="Microsoft YaHei UI"><br /></font></span>\
			</div>\
			<div>\
			<font face="Microsoft YaHei UI"><span style="orphans: 2; text-indent: 28px; widows: 2; line-height: 1.5;">与您分享现代管理学之父，</span><span style="line-height: 1.5;">彼</span><span style="font-size: 10.5pt; line-height: 1.5; background-color: transparent;">得&middot;德鲁克的一句话：</span></font>\
			</div>\
			<div>\
			<span style="font-size: 10.5pt; line-height: 1.5; background-color: transparent;"><font face="Microsoft YaHei UI">&nbsp; &nbsp; &nbsp; &nbsp;“管理的本质是激发和释放人本身固有的潜能创造价值，为他人谋福祉。”</font></span>\
			</div> \
			<div>\
			<font face="Microsoft YaHei UI">&nbsp;</font>\
			</div> \
			<div>\
			<font face="Microsoft YaHei UI">乔诺商学院成立于2009年，<span style="font-size: 10.5pt; line-height: 1.5; background-color: transparent;">为中国主流企业提供</span><span style="font-size: 10.5pt; line-height: 1.5; background-color: transparent;">战略管理、流程变革、人力资源、财经变革</span><span style="font-size: 10.5pt; line-height: 1.5; background-color: transparent;">等命题的管理培训与咨询服务。</span></font>\
			</div>\
			<div>\
			<font face="Microsoft YaHei UI"><br /></font>\
			</div>\
			<div>\
			<font face="Microsoft YaHei UI"><br /></font>\
			</div> \
			<div>\
			<font face="Microsoft YaHei UI">乔诺商学院3月公开课安排如下：</font>\
			</div> \
			<div>\
			<font face="Microsoft YaHei UI">------------------------------------------------------</font>\
			</div> \
			<div>\
			<font face="Microsoft YaHei UI">【<span style="font-size: 10.5pt; line-height: 1.5; background-color: transparent;">业绩管理班</span><span style="font-size: 10.5pt; line-height: 1.5; background-color: transparent;">】：高效达成年度业绩的销售管理路径</span></font>\
			</div>\
			<div>\
			<font face="Microsoft YaHei UI">时间：3月15-16日</font>\
			</div> \
			<div>\
			<font face="Microsoft YaHei UI">地点：上海</font>\
			</div> \
			<div>\
			<font face="Microsoft YaHei UI">价值：</font>\
			</div> \
			<div>\
			<ul style="margin-top: 0px; margin-bottom: 0px; list-style-position: inside;">\
			<li><span style="font-size: 10.5pt; line-height: 1.5; background-color: transparent;"><font face="Microsoft YaHei UI">建立完整的销售业绩管理路线图，让业绩处于可控状态</font></span></li>\
			<li><span style="font-size: 10.5pt; line-height: 1.5; background-color: transparent;"><font face="Microsoft YaHei UI">掌握公司业绩分解和管理的方法，让业绩对准战略</font></span></li>\
			<li><span style="font-size: 10.5pt; line-height: 1.5; background-color: transparent;"><font face="Microsoft YaHei UI">掌握使用增长策略控制销售业绩的方法，确保销售代表的精力放在高影响力活动上</font></span></li>\
			<li><span style="font-size: 10.5pt; line-height: 1.5; background-color: transparent;"><font face="Microsoft YaHei UI">通过九宫格模型，掌握业绩、策略、销售活动的选择、设计和管理</font></span></li>\
			<li><span style="font-size: 10.5pt; line-height: 1.5; background-color: transparent;"><font face="Microsoft YaHei UI">量身定做一个具有实操性的销售管理手册，改善作为销售经理的管理行为</font></span></li>\
			</ul>\
			</div> \
			<div>\
			<font face="Microsoft YaHei UI">嘉宾：</font>\
			</div> \
			<div>\
			<ul style="margin-top: 0px; margin-bottom: 0px; list-style-position: inside;">\
			<li><span style="font-size: 10.5pt; line-height: 1.5; background-color: transparent;"><font face="Microsoft YaHei UI">崔建中（原浪潮集团产品市场部总经理/原用友集团大客户经理/《市场与销售》、《商界评论》专栏作家）</font></span></li>\
			</ul>\
			</div> \
			<div>\
			<font face="Microsoft YaHei UI">&nbsp;</font>\
			</div> \
			<div>\
			<font face="Microsoft YaHei UI">------------------------------------------------------</font>\
			</div> \
			<div>\
			<font face="Microsoft YaHei UI">【<span style="font-size: 10.5pt; line-height: 1.5; background-color: transparent;">变革论坛</span><span style="font-size: 10.5pt; line-height: 1.5; background-color: transparent;">】：突破瓶颈、有效增长——成就下一个行业领导者</span></font>\
			</div>\
			<div>\
			<font face="Microsoft YaHei UI">时间：3月22-24日</font>\
			</div> \
			<div>\
			<font face="Microsoft YaHei UI">地点：上海</font>\
			</div> \
			<div>\
			<font face="Microsoft YaHei UI">价值：</font>\
			</div> \
			<div>\
			<ul style="margin-top: 0px; margin-bottom: 0px; list-style-position: inside;">\
			<li><span style="font-size: 10.5pt; line-height: 1.5; background-color: transparent;"><font face="Microsoft YaHei UI">还原华为长期增长背后的管理哲学、组织演进、战略管理、流程变革、干部管理与绩效激励机制</font></span></li>\
			</ul>\
			</div> \
			<div>\
			<font face="Microsoft YaHei UI">嘉宾：</font>\
			</div> \
			<div>\
			<ul style="margin-top: 0px; margin-bottom: 0px; list-style-position: inside;">\
			<li><span style="font-size: 10.5pt; line-height: 1.5; background-color: transparent;"><font face="Microsoft YaHei UI">黄卫伟（华为公司首席管理科学家/《华为基本法》执笔人/蓝血十杰/华为公司22年长期管理顾问）</font></span></li>\
			<li><span style="font-size: 10.5pt; line-height: 1.5; background-color: transparent;"><font face="Microsoft YaHei UI">林强（华为公司原产品线研发总裁/华为现役战略顾问/蓝血十杰/17年华为工作经验）</font></span></li>\
			<li><span style="font-size: 10.5pt; line-height: 1.5; background-color: transparent;"><font face="Microsoft YaHei UI">李岳洲（华为公司原全球销售部、行销产品部、研发产品线人力资源部部长/20年华为工作经验）</font></span></li>\
			</ul>\
			</div> \
			<div>\
			<font face="Microsoft YaHei UI">&nbsp;</font>\
			</div> \
			<div>\
			<font face="Microsoft YaHei UI">------------------------------------------------------</font>\
			</div> \
			<div>\
			<font face="Microsoft YaHei UI">【<span style="font-size: 10.5pt; line-height: 1.5; background-color: transparent;">全面预算班</span><span style="font-size: 10.5pt; line-height: 1.5; background-color: transparent;">】</span><span style="font-size: 10.5pt; line-height: 1.5; background-color: transparent;">：基于战略的全面预算管理与成本管理</span></font>\
			</div>\
			<div>\
			<font face="Microsoft YaHei UI">时间：3月22-23日</font>\
			</div> \
			<div>\
			<font face="Microsoft YaHei UI">地点：上海</font>\
			</div> \
			<div>\
			<font face="Microsoft YaHei UI">价值：</font>\
			</div> \
			<div>\
			<ul style="margin-top: 0px; margin-bottom: 0px; list-style-position: inside;">\
			<li><span style="font-size: 10.5pt; line-height: 1.5; background-color: transparent;"><font face="Microsoft YaHei UI">理解公司经营本质，匹配公司的业务发展阶段，找到合适自己的全面预算管理模式</font></span></li>\
			<li><span style="font-size: 10.5pt; line-height: 1.5; background-color: transparent;"><font face="Microsoft YaHei UI">理解业务战略，实现业财融合，更有针对性的弹性管理</font></span></li>\
			<li><span style="font-size: 10.5pt; line-height: 1.5; background-color: transparent;"><font face="Microsoft YaHei UI">在目标确定、预算授权和绩效评价间达到平衡，牵引业务改进</font></span></li>\
			<li><span style="font-size: 10.5pt; line-height: 1.5; background-color: transparent;"><font face="Microsoft YaHei UI">适当划分经营单元（责任中心）激发组织活力，实现经营成功从偶然到必然</font></span></li>\
			</ul>\
			</div> \
			<div>\
			<font face="Microsoft YaHei UI">嘉宾：</font>\
			</div> \
			<div>\
			<ul style="margin-top: 0px; margin-bottom: 0px; list-style-position: inside;">\
			<li><span style="font-size: 10.5pt; line-height: 1.5; background-color: transparent;"><font face="Microsoft YaHei UI">石军（华为公司原海外客户及项目CFO/核心网产品线CFO/10年华为工作经验）</font></span></li>\
			</ul>\
			</div> \
			<div>\
			<font face="Microsoft YaHei UI">&nbsp;</font>\
			</div> \
			<div>\
			<font face="Microsoft YaHei UI">------------------------------------------------------</font>\
			</div> \
			<div>\
			<font face="Microsoft YaHei UI">【<span style="font-size: 10.5pt; line-height: 1.5; background-color: transparent;">激励机制工作坊</span><span style="font-size: 10.5pt; line-height: 1.5; background-color: transparent;">】：导向冲锋的组织绩效考核与激励机制设计</span></font>\
			</div>\
			<div>\
			<font face="Microsoft YaHei UI">时间：3月28-30日</font>\
			</div> \
			<div>\
			<font face="Microsoft YaHei UI">地点：上海</font>\
			</div> \
			<div>\
			<font face="Microsoft YaHei UI">价值：</font>\
			</div> \
			<div>\
			<ul style="margin-top: 0px; margin-bottom: 0px; list-style-position: inside;">\
			<li><span style="font-size: 10.5pt; line-height: 1.5; background-color: transparent;"><font face="Microsoft YaHei UI">掌握战略解码工具，将公司战略解码到组织绩效，实现外部压力无衰减的内部传递</font></span></li>\
			<li><span style="font-size: 10.5pt; line-height: 1.5; background-color: transparent;"><font face="Microsoft YaHei UI">掌握组织绩效方案设计，讲组织绩效与奖金包强关联，牵引挣钱而不是分钱</font></span></li>\
			<li><span style="font-size: 10.5pt; line-height: 1.5; background-color: transparent;"><font face="Microsoft YaHei UI">掌握个人绩效方案设计，有效识别奋斗者，绩效与激励联动，给奋斗者加满油</font></span></li>\
			<li><span style="font-size: 10.5pt; line-height: 1.5; background-color: transparent;"><font face="Microsoft YaHei UI">掌握工资包设计方法，实现公司经营指标与薪酬包的强关联，牵引人均效率与人均薪酬均衡增长</font></span></li>\
			<li><span style="font-size: 10.5pt; line-height: 1.5; background-color: transparent;"><font face="Microsoft YaHei UI">掌握奖金包设计方法，奖金包从“自上而下、人为分配”转变为“自下而上、获取分享”，促使员工将所有努力聚焦到业务经营发展上</font></span></li>\
			</ul>\
			</div> \
			<div>\
			<font face="Microsoft YaHei UI">嘉宾：</font>\
			</div> \
			<div>\
			<ul style="margin-top: 0px; margin-bottom: 0px; list-style-position: inside;">\
			<li><span style="font-size: 10.5pt; line-height: 1.5; background-color: transparent;"><font face="Microsoft YaHei UI">李岳洲（华为公司原全球销售部、行销产品部、研发产品线人力资源部部长/20年华为工作经验）</font></span></li>\
			<li><span style="font-size: 10.5pt; line-height: 1.5; background-color: transparent;"><font face="Microsoft YaHei UI">曾小军（乔诺商学院高级合伙人/咨询中心总经理）</font></span></li>\
			</ul>\
			</div> \
			<div>\
			<font face="Microsoft YaHei UI">&nbsp;</font>\
			</div>\
			<div>\
			<div>\
			<font face="Microsoft YaHei UI">------------------------------------------------------</font>\
			</div>\
			<div>\
			<font face="Microsoft YaHei UI">【<span style="font-size: 10.5pt; line-height: 1.5; background-color: transparent;">从战略到执行工作坊</span><span style="font-size: 10.5pt; line-height: 1.5; background-color: transparent;">】：打通企业战略、年度业务计划、战略绩效与激励的任督二脉</span></font>\
			</div>\
			<div>\
			<font face="Microsoft YaHei UI">时间：3月28-30日</font>\
			</div>\
			<div>\
			<font face="Microsoft YaHei UI">地点：上海</font>\
			</div>\
			<div>\
			<font face="Microsoft YaHei UI">价值：</font>\
			</div>\
			<div>\
			<ul style="margin-top: 0px; margin-bottom: 0px; list-style-position: inside;">\
			<li><span style="font-size: 10.5pt; line-height: 1.5; background-color: transparent;"><font face="Microsoft YaHei UI">制定中长期规划与创新业务设计</font></span></li>\
			<li><span style="font-size: 10.5pt; line-height: 1.5; background-color: transparent;"><font face="Microsoft YaHei UI">制定年度业务计划与预算</font></span></li>\
			<li><span style="font-size: 10.5pt; line-height: 1.5; background-color: transparent;"><font face="Microsoft YaHei UI">匹配业务战略的组织结构设计与定位</font></span></li>\
			<li><span style="font-size: 10.5pt; line-height: 1.5; background-color: transparent;"><font face="Microsoft YaHei UI">导向长期有效增长的考核、工资、奖金与股权激励机制</font></span></li>\
			<li><span style="font-size: 10.5pt; line-height: 1.5; background-color: transparent;"><font face="Microsoft YaHei UI">激发组织活力的干部选拔与淘汰机制</font></span></li>\
			</ul>\
			</div>\
			<div>\
			<font face="Microsoft YaHei UI">嘉宾：</font>\
			</div>\
			<div>\
			<ul style="margin-top: 0px; margin-bottom: 0px; list-style-position: inside;">\
			<li><span style="font-size: 10.5pt; line-height: 1.5; background-color: transparent;"><font face="Microsoft YaHei UI">林强（华为公司原产品线研发总裁/华为现役战略顾问/蓝血十杰/17年华为工作经验）</font></span></li>\
			<li><span style="font-size: 10.5pt; line-height: 1.5; background-color: transparent;"><font face="Microsoft YaHei UI">马良（华为公司原集团财经副总裁//内部控制与风险管理部部长/海外片区首席财务官/投资管理部部长/会计总监）</font></span></li>\
			<li><span style="font-size: 10.5pt; line-height: 1.5; background-color: transparent;"><font face="Microsoft YaHei UI">刘文超（华为公司原财经体系干部部部长/中国区干部部部长/22年华为工作经验）</font></li>\
			</ul>\
			</div>\
			</div>\
			<div>\
			<font face="Microsoft YaHei UI"><br /></font>\
			</div> \
			<div>\
			<font face="Microsoft YaHei UI">------------------------------------------------------</font>\
			</div> \
			<div>\
			<font face="Microsoft YaHei UI">【<span style="font-size: 10.5pt; line-height: 1.5; background-color: transparent;">品牌与营销班</span><span style="font-size: 10.5pt; line-height: 1.5; background-color: transparent;">】</span><span style="font-size: 10.5pt; line-height: 1.5; background-color: transparent;">：渗透消费者的市场营销管理与品牌建设</span></font>\
			</div>\
			<div>\
			<font face="Microsoft YaHei UI">时间：3月29-30日</font>\
			</div> \
			<div>\
			<font face="Microsoft YaHei UI">地点：上海</font>\
			</div> \
			<div>\
			<font face="Microsoft YaHei UI">价值：</font>\
			</div> \
			<div>\
			<ul style="margin-top: 0px; margin-bottom: 0px; list-style-position: inside;">\
			<li><span style="font-size: 10.5pt; line-height: 1.5; background-color: transparent;"><font face="Microsoft YaHei UI">掌握Go to marketing的核心流程，让产品以最合理的方式抵达消费者</font></span></li>\
			<li><span style="font-size: 10.5pt; line-height: 1.5; background-color: transparent;"><font face="Microsoft YaHei UI">掌握塑造高端品牌的品牌策略</font></span></li>\
			<li><span style="font-size: 10.5pt; line-height: 1.5; background-color: transparent;"><font face="Microsoft YaHei UI">掌握体系化作战方式，构建marketing整体的组织能力</font></span></li>\
			</ul>\
			</div> \
			<div>\
			<font face="Microsoft YaHei UI">嘉宾：</font>\
			</div> \
			<div>\
			<ul style="margin-top: 0px; margin-bottom: 0px; list-style-position: inside;">\
			<li><span style="font-size: 10.5pt; line-height: 1.5; background-color: transparent;"><font face="Microsoft YaHei UI">鲍圣霞（华为终端原全球营销管理部部长/10年华为工作经验）</font></span></li>\
			<li><span style="font-size: 10.5pt; line-height: 1.5; background-color: transparent;"><font face="Microsoft YaHei UI">吉慧（原华为消费者业务(终端公司)旗舰产品营销总监/原华为公司高级营销经理）</font></span></li>\
			</ul>\
			</div> \
			<div>\
			<font face="Microsoft YaHei UI">&nbsp;</font>\
			</div> \
			<div>\
			<br />\
			</div> \
			<div>\
			<font face="Microsoft YaHei UI">Best regards,​</font>\
			</div> \
			<div>\
			<font face="Microsoft YaHei UI">------------------</font>\
			</div> \
			<div>\
			<font face="Microsoft YaHei UI">乔诺商学院|乔诺咨询</font>\
			</div> \
			<div>\
			<font face="Microsoft YaHei UI">渠道部 欧阳仕</font>\
			</div> \
			<div>\
			<font face="Microsoft YaHei UI">手机：</font>\
			<span style="font-family: 'Segoe UI', Tahoma; line-height: normal;">183 1712 2293</span>\
			<font face="Microsoft YaHei UI">（微信同号）</font>\
			</div> \
			<div>\
			<font face="Microsoft YaHei UI">邮箱：oliver.ou@geonol.com</font>\
			</div> \
			<div>\
			<font face="Microsoft YaHei UI">地址：上海市长宁区金钟路968号凌空SOHO-2号楼305</font>\
			</div> \
			<div>\
			<font face="Microsoft YaHei UI">使命：通过持续管理变革，成就下一个行业领导者（www.geonol.com）</font>\
			</div>\
			</body>\
			</html>'''

	return front + name_content + tail

#读取表格内容
def get_reciever_list(file_name):
	with open(file_name,newline='',encoding='UTF-8') as csvfile:
		reader = csv.DictReader(csvfile,dialect='excel')
		company_list = []
		secretary_list = []
		email_list = []
		for row in reader:
			if row['公司名称']:
				company_list.append(row['公司名称'])
			else:
				company_list.append('NA')
			if row['董秘']:
				secretary_list.append(row['董秘'])
			else:
				secretary_list.append('NA')
			if row['董秘邮箱']:
				email_list.append(row['董秘邮箱'])
			else:
				email_list.append('NA')
		return company_list, secretary_list, email_list

# 中文处理
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

#异常处理
def write_to_txt(error_report_file,company_list):
    f = codecs.open(error_report_file,'a','utf-8')
    f.write('以下企业发送失败：\r\n')
    for i in range(len(company_list)):
    	f.write('{}: {};'.format(i+1,company_list[i]) + '\r\n')
    f.close()

#发邮件
def send(company_list, secretary_list, email_list,error_report_file):
	error_name_list = []
	for i in range(2001,3000):
		print('------------------------------SENDING NO.{} EMAIL------------------------------------------'.format(i+1))
		try:
			email_content = edit_text(secretary_list[i])
			msg = MIMEText(email_content,"html","utf-8")
			#msg = MIMEText('python email',"plain","utf-8")
			#MIMETextt是生成email 的一种格式
				# 参数一:邮件的内容
				# 参数二:邮件的类型
				# 参数三:邮件的编码
			head = '成就下一个行业领导者——乔诺商学院【三月】课程表'
			msg['Subject'] = Header(head, 'utf-8').encode() #邮件的标题
			msg['From'] = _format_addr('乔诺商学院 <%s>' % from_addr) #发件人
			msg['To'] = _format_addr('{} <%s>'.format(company_list[i]) % email_list[i])  #‘管理员’字段与'to_addr'匹配代入
			#msg['To'] = ",".join(to_addrs) #收件人
				 
			#发送邮件  实例化腾讯的邮件(smtp)服务器
			server = smtplib.SMTP_SSL(smtp_server,465)
			#设置调试模式
			server.set_debuglevel(1)
			#登录实例化的邮件服务器
			server.login(from_addr,password)
			server.sendmail(from_addr,email_list[i],msg.as_string())
		except:
			error_name_list.append(company_list[i])
		print('-------------------------------------------------------------------------------------------')
	print(error_name_list)
	write_to_txt(error_report_file, error_name_list)
	server.quit()#退出

#main
#change input to get_reciever_list()
company_list, secretary_list, email_list = get_reciever_list(csv_file)
#change
send(company_list,secretary_list,email_list,error_report_file)
