#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest
from appium import webdriver
import time,os,sys
import huadongdemo
import jietudemo
class ybgcaselogout(unittest.TestCase):
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
        #智能隐式等待
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.assertEqual([], self.verificationErrors)
        driver = self.driver
        #退出app 断开当前session连接
        driver.quit()
    def test_logout(self):
        driver = self.driver
        time.sleep(2)
        try:
            driver.find_element_by_xpath("//android.widget.RadioButton[@resource-id='com.istone.xdf:id/rb_me']").click()
            time.sleep(1)
            jietudemo.take_screenShot(driver,u'logout_我的页面')
            #向上滑动找到退出按钮元素
            huadongdemo.swipeUp(driver,n=1)
            time.sleep(1)
            jietudemo.take_screenShot(driver,u'logout_向上滑动显示退出按钮')
            work = driver.find_element_by_xpath("//android.widget.Button[@resource-id='com.istone.xdf:id/btn_exit_me']").text
            try:
                assert u'退出' in work
                driver.find_element_by_xpath("//android.widget.Button[@resource-id='com.istone.xdf:id/btn_exit_me']").click()
                print(u'成功退出并返回登录页')
                time.sleep(1)
                jietudemo.take_screenShot(driver,u'成功退出返回登录页')
            except AssertionError as msg:
                # 直接截图成功
                '''
                img_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '//png//'
                time = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
                screen_save_path = img_folder + time + '.png'
                driver.get_screenshot_as_file(screen_save_path)
                raise Exception (u'模拟向上滚动失败，未找到退出按钮，退出操作失败')
                '''
                #调用jietudemo进行截图
                time.sleep(1)
                jietudemo.take_screenShot(driver,u'未找到退出按钮')
                raise Exception(u'模拟向上滚动失败，未找到退出按钮，退出操作失败')
        except Exception as e:
            time.sleep(2)
            jietudemo.take_screenShot(driver,u'logout_我的页面失败')
            raise Exception(u'logout_我的页面失败')


if __name__ == '__main__':
    unittest.main()