#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest
from appium import webdriver
import time,os,sys
import jietudemo
PATH = lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))
#login 验证登录是否正常
class ybgcaselogin(unittest.TestCase):
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

    def test_login(self):
        #初始化
        global time
        driver = self.driver
        #验证登录页元素是否可以找到，若找不到则fail
        jietudemo.take_screenShot(driver,u'login_page')
        usertext = driver.find_element_by_xpath("//android.widget.Button[@resource-id='com.istone.xdf:id/btn_login']").text
        #断言
        try:
            assert u'登录' in usertext
            print('open loginpage sucess!!!')
            # 定位用户框清空并输入密码
            driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.istone.xdf:id/et_login_user']").clear()
            driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.istone.xdf:id/et_login_user']").send_keys('zhenghuaining')
            # 定位输入密码框清空并输入密码
            driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.istone.xdf:id/et_login_psw']").clear()
            driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.istone.xdf:id/et_login_psw']").send_keys('Zhn594210')
            jietudemo.take_screenShot(driver,u'login_输入用户和密码')
            driver.find_element_by_xpath("//android.widget.Button[@resource-id='com.istone.xdf:id/btn_login']").click()  # 定位登录按钮并点击登录按钮
            jietudemo.take_screenShot(driver,u'login_登录成功')
        except AssertionError as e:
            # 直接截图成功
            '''
            img_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '//png//'
            time = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
            screen_save_path = img_folder + time + '.png'
            driver.get_screenshot_as_file(screen_save_path)
            #使用raise方法抛出异常并且终止运行， 同时输出exception
            raise Exception('open loginpage fail')
            '''
            jietudemo.take_screenShot(driver,u'打开登录页失败')
            raise  Exception('open loginpage fail')


if __name__ == '__main__':
    unittest.main()
