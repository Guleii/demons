# coding:utf-8
__author__ = 'Alan'
'''
description:配置全局参数
'''
import time
import os

# 配置生成报告与日志的名称与目录
# 获取项目路径
# project_path = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)[0]), '.'))
project_path = os.path.abspath(os.path.join(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]), '.'))
# 测试用例代码存放路径（用于构建suite,注意该文件夹下的文件都应该以test开头命名）
test_case_path = project_path+"\\src\\test_case"
# print u'日志路径：'+log_path
# 测试报告存储路径，并以当前时间作为报告名称前缀
report_path = project_path+"\\report\\"
report_name = "report.html"
log_name = "Launcher.log"
# report_name = report_path+time.strftime('%Y%m%d%H%S', time.localtime())

# 截屏存储路径
screen_shot_path = project_path+"\\screenshot\\"
screen_shot_picture_format = ".png"



# 配置Html的样式
html_title = "Launcher测试报告"  # Html报告标题
html_description = "Launcher Tab模块测试"   # Html报告描述
test_case_retry_count = 0  # 测试用例失败后重试的次数
save_last_try_result = True  # Html报告是否只输出最后重试的结果





# 设置发送测试报告的QQ企业公共邮箱、用户名和密码
smtp_sever = 'smtp.exmail.qq.com'  # 邮箱SMTP服务，各大运营商的smtp服务可以在网上找，然后可以在foxmail这些工具中验正
email_from = "alan.li@xgimi.com"  # 发件人邮箱
email_port = 25  # 默认是25 不需要改动
email_password = "Yy123456"  # 发件人邮箱的登录密码
email_To = ["alan.li@xgimi.com", "1291380515@qq.com"]  # 收件人 可发送多个，多个邮件以英文逗号分隔
email_title = 'Launcher测试报告'  # 邮件标题
email_content = 'Launcher测试用例已完成测试，请查收，报告与日志'  # 邮件内容







# 设置发送测试报告的QQ个人邮箱、用户名和密码
# smtp_sever = 'smtp.qq.com'  # 邮箱SMTP服务，各大运营商的smtp服务可以在网上找，然后可以在foxmail这些工具中验正
# email_from = "1291380515@qq.com"  # 发件人邮箱
# email_port = 25  # 默认是25 不需要改动
# email_password = "nquhwnclzhnwbagf"  # 发件人邮箱的授权密码（不是邮箱登录密码，是邮箱生成的授权密码）
# email_To = ["alan.li@xgimi.com", "1291380515@qq.com"]  # 收件人 可发送多个，多个邮件以英文逗号分隔
# email_title = 'Launcher测试报告'  # 邮件标题
# email_content = 'Launcher测试用例已完成测试，请查收，报告与日志'  # 邮件内容
