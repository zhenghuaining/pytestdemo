# -*- coding: UTF-8 -*-
# #!/usr/bin/python
import unittest
import unittest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time,os,sys
import huadongdemo
import jietudemo
class ybgcasenewspageupdate(unittest.TestCase):
    def setUp(self):
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
        # desired_caps['app'] = PATH(r"D:\\appiumtestAPP\\student-debug.apk")
        # 应用的包名
        desired_caps['appPackage'] = 'com.istone.xdf'
        desired_caps['appActivity'] = 'com.xdf.aio.ui.SplashUI'
        #屏蔽软键盘，直接绕过键盘输入
        #是使用unicode编码方式发送字符串
        desired_caps['unicodeKeyboard'] = 'True'
        #是将键盘隐藏起来
        desired_caps['resetKeyboard'] = 'True'
        # 启动 应用app
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.assertEqual([], self.verificationErrors)
        driver = self.driver
        # 退出app 断开当前session连接
        driver.quit()

    def test_ybgnewspageupdate(self):
        driver = self.driver
        try:
            #切换至新闻资讯页面
            driver.find_element_by_xpath("//android.widget.RadioButton[@resource-id='com.istone.xdf:id/rb_appStore']").click()
            jietudemo.take_screenShot(driver,u'newspageupdate_切换至新闻资讯页')
            time.sleep(2)
            el = driver.find_element_by_xpath("//android.view.View[@content-desc='新闻资讯']").get_attribute('name')
            try:
                assert u'新闻资讯' in el
                print(u'跳转新闻资讯页成功')
                # 向下滑动屏幕刷新页面信息
                huadongdemo.swipeDown(driver, t=3000, n=1)
                jietudemo.take_screenShot(driver,u'newspageupdate_下接刷新')

            except AssertionError as e:
                #调用jietudemo进行截图
                jietudemo.take_screenShot(driver,u'跳转新闻资讯页失败')
                raise Exception(u'跳转新闻资讯页失败')
        except Exception as e:
            jietudemo.take_screenShot(driver,u'newspageupdate_加载失败')
            raise Exception(u'新闻资讯页加载失败')


if __name__ == '__main__':
    unittest.main()
