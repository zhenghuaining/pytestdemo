#!/usr/bin/python
# -*- coding: UTF-8 -*-
import HTMLTestRunner
import unittest
import time, os, sys
import gongzuoliu
import login
import pagecheck
import installdangjian
import uninstalldangjian
import newspageupdate
import queryjiaqin
import logout
'''
reload(sys)
sys.setdefaultencoding('utf-8')
'''
# 创建一个测试容器套件
testunit = unittest.TestSuite()
# 将测试用例加入到测试容器(套件)中,其中baidu..Test为：baidu.py中Test类
# 执行顺序为顺序执行：先执行1、再执行2，最后执行3
# 添加login到测试套件中
testunit.addTest(unittest.makeSuite(login.ybgcaselogin))
# 添加gongzuioliu到测试套件中
testunit.addTest(unittest.makeSuite(gongzuoliu.ybgcasegongzuoliu))
#添加安装党建到测试套件中
testunit.addTest(unittest.makeSuite(installdangjian.ybgcaseinstalldangjian))
#添加删除党建到测试套件中
testunit.addTest(unittest.makeSuite(uninstalldangjian.ybgcaseuninstalldangjian))
#添加新闻资讯页刷新至测试套件中
testunit.addTest(unittest.makeSuite(newspageupdate.ybgcasenewspageupdate))
#添加查询假勤至测试套件中
testunit.addTest((unittest.makeSuite(queryjiaqin.ybgcasequeryjiaqin)))
# 添加logout到测试套件中
testunit.addTest(unittest.makeSuite(logout.ybgcaselogout))
'''
#执行测试套件
runner = unittest.TextTestRunner()
runner.run(testunit)
'''
# 定义测试报告存放路径
time = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
filename = "D:\\appium_pycharm_demo\\xdf_ybgAPP\\report\\ybgAPP" + time + '.html'
# noinspection PyArgumentList
fp = file(filename, "wb")
# 定义测试报告
runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'ybgAPP回归测试报告',
    description=u'用例执行情况:')
# 运行测试用例
runner.run(testunit)
