#!/usr/bin/python
# -*- coding: UTF-8 -*-

import HTMLTestRunnerCN
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import unittest
import time
import os
'''
封装发送邮件、筛选最新报告、生成报告
'''
# ==============定义发送邮件==========
def send_mail(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header(u"云办公自动化测试报告", 'utf-8')
    msg['from'] = 'zhenghuaining@163.com'
    msg['to'] = 'zhenghuaining@xdf.cn'
    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com')  # 邮箱服务器
    smtp.login('zhenghuaining@163.com', 'Chm594210')  # 登录邮箱
    smtp.sendmail('zhenghuaining@163.com', 'zhenghuaining@xdf.cn', msg.as_string())  # 发送者和接收者
    smtp.quit()
    print(u"邮件已发出！注意查收。")

# ======查找测试目录，找到最新生成的测试报告文件======
def new_report(test_report):
    #定义报告目录
    lists = os.listdir(test_report)  # 列出目录的下所有文件和文件夹保存到lists
    lists.sort(key=lambda fn: os.path.getmtime(test_report + "\\" + fn))  # 按时间排序
    file_new = os.path.join(test_report, lists[-1])  # 获取最新的文件保存到file_new
    #print(file_new)
    return file_new

if __name__ == "__main__":
    test_dir = "D:\\pytestdemo\\caselist"
    test_report = "D:\\pytestdemo\\test_report"
    #通过unittest框架的discover()找到匹配的测试用例，由HTMLTestRunner的run()方法执行测试用例并生成最新的测试报告
    discover = unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py')
    now = time.strftime("%Y-%m-%d_%H-%M-%S")
    filename = test_report + '\\' + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fp,
                            title=U'云办公APP测试报告',
                            description=u'用例执行情况：')
    runner.run(discover)
    fp.close()

    #调用new_report()函数找到测试报告目录下最新生成的测试报告，返回测试报告的路径
    new_report = new_report(test_report)
    #将得到的最新测试报告的完整路径传给send_mail()函数，实现发邮件功能
    send_mail(new_report)  # 发送测试报告