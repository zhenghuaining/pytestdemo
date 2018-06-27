#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest
from appium import webdriver
import time,os,sys

class ybgcasepagecheck(unittest.TestCase):
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
        desired_caps['appPackage'] = 'com.istone.xdf'
        desired_caps['appActivity'] = 'com.xdf.aio.ui.SplashUI'
        # 启动 应用app
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.assertEqual([], self.verificationErrors)
        driver = self.driver
        #退出app 断开当前session连接
        driver.quit()

    def test_pagecheck(self):
        driver = self.driver
        time.sleep(8)
        #切换至ilink页面
        driver.find_element_by_xpath("//android.widget.RadioButton[@resource-id='com.istone.xdf:id/rb_interact']").click()
        #获取页面某一个元素进行判断
        usrtext = driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.istone.xdf:id/tv_me_mission']").text
        print(usrtext)
        #若usrtext==我的待办，则成功，否则输出msg
        driver.assertEqual(usrtext,u'我的待办',msg=u'切换ilink页失败')
        time.sleep(1)
        #切换至新闻资讯页
        driver.find_element_by_xpath("//android.widget.RadioButton[@resource-id='com.istone.xdf:id/rb_appStore']").click()
        usrname = driver.find_element_by_xpath("//android.widget.RadioButton[@resource-id='com.istone.xdf:id/rb_appStore']").get_attribute('name')
        print(usrname)
        driver.assertEqual(usrname,u'新闻资讯',msg=u'切换新闻资讯页失败')
        time.sleep(1)
        #切换至我的页面
        driver.find_element_by_xpath("//android.widget.RadioButton[@resource-id='com.istone.xdf:id/rb_me']").click()
        usrname1 = driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.istone.xdf:id/tv_me']").text
        print(usrname1)
        driver.assertEqual(usrname1,u'我',msg=u'切换我的页面失败')
        time.sleep(1)
        #返回首页页面
        driver.find_element_by_xpath("//android.widget.RadioButton[@resource-id='com.istone.xdf:id/rb_home']").click()
        usrname2 = driver.find_element_by_xpath("//android.widget.TextView[@text='工作流']").text
        print(usrname2)
        driver.assertEqual(usrname2,u'工作流',msg=u'切换首页面失败')
        time.sleep(5)


if __name__ == '__main__':
    unittest.main()
