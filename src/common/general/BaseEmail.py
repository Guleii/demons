# coding:utf-8
__author__ = 'Alan'
'''
description:发送邮箱的工具类
'''
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import smtplib
import os
import time
from config import GlobalConfig as gl
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


# 读取邮箱配置信心
to_addr = gl.email_To
mail_host = gl.smtp_sever
mail_user = gl.email_from
mail_pass = gl.email_password
port = gl.email_port
header_msg = gl.email_title
attach = gl.email_content
report = gl.report_path+gl.report_name
log = gl.report_path+gl.log_name
log_name = gl.log_name
report_name = gl.report_name


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def send_mail(**kwargs):
    '''
    :param f: 附件路径
    :param to_addr:发给的人 []
    :return:
    '''
    from_addr = kwargs["mail_user"]
    password = kwargs["mail_pass"]
    # to_addr = "ashikun@126.com"
    smtp_server = kwargs["mail_host"]

    msg = MIMEMultipart()

    # msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
    msg['From'] = _format_addr('来自<%s>接口测试' % from_addr)
    msg['To'] = _format_addr(' <%s>' % kwargs["to_addr"])
    msg['Subject'] = Header(kwargs["header_msg"], 'utf-8').encode()
    msg.attach(MIMEText(kwargs["attach"], 'plain', 'utf-8'))

    # html报告
    if kwargs.get("report", "0") != "0":
        part = MIMEApplication(open(kwargs["report"], 'rb').read())
        part.add_header('Content-Disposition', 'attachment', filename=('gb2312', '', kwargs["report_name"]))
        msg.attach(part)

    # logcat日志
    if kwargs.get("log", "0") != "0":
        part = MIMEApplication(open(kwargs["log"], 'rb').read())
        part.add_header('Content-Disposition', 'attachment', filename=('gb2312', '', kwargs["log_name"]))
        msg.attach(part)

    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, kwargs["to_addr"], msg.as_string())
    server.quit()


"""
    调用此函数发送邮箱
"""


def start_send_email():
    # report_list = os.listdir(gl.report_path)
    # report_list.sort(
    #     key=lambda fn: os.path.getmtime(gl.report_path + fn) if not os.path.isdir(gl.report_path + fn) else 0)
    # new_report = os.path.join(gl.report_path, report_list[-1])
    time.sleep(5)  # 设置睡眠时间，等待测试报告生成完毕（不然邮件会因为报告为空而无法发送）
    send_mail(to_addr=to_addr, mail_host=mail_host, mail_user=mail_user, port=port, mail_pass=mail_pass,
              header_msg=header_msg, report=report, attach=attach, report_name=report_name, log=log, log_name=log_name)


if __name__ == "__main__":
    start_send_email()
