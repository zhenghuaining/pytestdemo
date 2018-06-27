#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest
from appium import webdriver
import time,os,sys
import jietudemo
class ybgcasegongzuoliu(unittest.TestCase):

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

    def test_gongzuoliu(self):
        global time
        driver = self.driver
        #进入工作流页面

        try:
            driver.find_element_by_xpath("//android.widget.TextView[@text='工作流']").click()
            time.sleep(2)
            work1 = driver.find_element_by_xpath("//android.view.View[@content-desc='待办']").get_attribute('name')
        except Exception as e:
            jietudemo.take_screenShot(driver,u'未找到待办元素')
            raise Exception(u'未找到待办元素')

        #添加断言
        try:
            assert u'待办' in work1
            print(u'切换成功进入工作流页面')

            # 已办页和待力页面切换
            driver.find_element_by_xpath("//android.view.View[@content-desc='已办']").click()
            jietudemo.take_screenShot(driver,u'gongzuoliu_已办')
            driver.find_element_by_xpath("//android.view.View[@content-desc='待办']").click()
            jietudemo.take_screenShot(driver,u'gongzuoliu_待办')
            # 模拟点击手机回退按钮
            driver.keyevent(4)
            jietudemo.take_screenShot(driver,u'gongzuoliu_回退至主页')
            time.sleep(2)
        except AssertionError as msg:
            #直接截图成功
            '''
            img_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '//png//'
            time = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
            screen_save_path = img_folder + time + '.png'
            driver.get_screenshot_as_file(screen_save_path)
            raise Exception (u'进入工作流页面失败')
            '''
            #调用jietudemo方法进行截图
            jietudemo.take_screenShot(driver,u'进入工作流页面失败')
            raise Exception(u'进入工作流页面失败')

if __name__ == '__main__':
    unittest.main()