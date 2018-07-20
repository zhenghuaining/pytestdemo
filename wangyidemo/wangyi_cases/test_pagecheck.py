#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest
from appium import webdriver
import time,os,sys
from  common import jietudemo
PATH = lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))

class wangyi_pagecheck(unittest.TestCase):

    def setUp(self):
        "Hook method for setting up the test fixture before exercising it."
        self.verificationErrors = []  # 脚本运行时，错误的信息将被打印到这个列表中。
        self.accept_next_alert = True  # 是否继续接受下一下警告
        # 定义启动设备需要的参数
        desired_caps = {}
        # 设备系统
        desired_caps['platformName'] = 'Android'
        # 设备系统版本号
        desired_caps['platformVersion'] = '4.4'
        # 设备名称
        desired_caps['deviceName'] = '257d512d'
        # 要测试的应用的地址
        #desired_caps['app'] = PATH(r"D:\\appiumtestAPP\\student-debug.apk")
        # 应用的包名
        desired_caps['appPackage'] = 'com.netease.newsreader.activity'
        desired_caps['appActivity'] = 'com.netease.nr.biz.ad.AdActivity'
        # 屏蔽软键盘，直接绕过键盘输入
        # 是使用unicode编码方式发送字符串
        desired_caps['unicodeKeyboard'] = 'True'
        # 是将键盘隐藏起来
        desired_caps['resetKeyboard'] = 'True'
        # 启动 应用app
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.assertEqual([], self.verificationErrors)
        driver = self.driver
        #退出app 断开当前session连接
        driver.quit()

    def test_pagecheck(self):
        driver = self.driver
        #判断是否弹出广告页，若弹出则点击跳过，如果未弹出则正常操作；
        ele = driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.netease.newsreader.activity:id/nk']").text
        try:
            assert u'跳过' in ele
            # 点击跳过按钮，跳过首打开弹出的广告页
            driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.netease.newsreader.activity:id/nk']").click()
        except AssertionError as e:










if __name__ == '__main__':
    unittest.main()