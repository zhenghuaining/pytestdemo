# -*- coding: UTF-8 -*-
# #!/usr/bin/python
import unittest
import unittest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time,os,sys
import huadongdemo
import jietudemo

class ybgcasequeryjiaqin(unittest.TestCase):
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

    def test_ybgqueryjiaqin(self):
        driver = self.driver
        #定位HR自助元素并点击进入HR自动页
        try:
            driver.find_element_by_xpath("//android.widget.TextView[@text='HR自助']").click()
            jietudemo.take_screenShot(driver,u'queryjiaqin_HR自助页')
            time.sleep(2)
            #添加断言，判断是否进入HR自助页
            el = driver.find_element_by_xpath("//android.view.View[@content-desc='HR自助']").get_attribute('name')
            #print(el)
            try:
                assert u'HR自助' in el
                print('open HRpage sucess')
                #定位假勤申请元素并点击进入假勤页
                driver.find_element_by_xpath("//android.view.View[@content-desc='假勤申请']").click()
                jietudemo.take_screenShot(driver,u'queryjiaqin_假勤页')
                #添加断言，判断是否进入假勤页
                el1 = driver.find_element_by_xpath("//android.view.View[@content-desc='假勤记录']").get_attribute('name')
                print(el1)
                try:
                    assert u'假勤记录' in el1
                    print(u'成功打开假勤页')
                    #定位假勤记录元素并点击，进入假勤查询页
                    driver.find_element_by_xpath("//android.view.View[@content-desc='假勤记录']").click()
                    jietudemo.take_screenShot(driver,u'queryjiaqin_假勤查询页')
                    #添加断言，判断是否进入假勤记录页
                    el2 = driver.find_element_by_xpath("//android.view.View[@content-desc='待审批']").get_attribute('name')
                    print(el2)
                    try:
                        assert u'待审批' in el2
                        #若断言成功，则定位已审批元素并点击查询已审批数据
                        driver.find_element_by_xpath("//android.view.View[@content-desc='已审批']").click()
                        jietudemo.take_screenShot(driver,u'queryjiaqin_已审批页')
                        #选择第一条申请记录打开详情
                        #通过指针坐标点击第一条申请记录
                        a = 486.0 / 1080
                        b = 470.0 / 1920
                        x = driver.get_window_size()['width']
                        y = driver.get_window_size()['height']
                        # 点击坐标打开详情
                        driver.tap([(a * x,b * y)])
                        jietudemo.take_screenShot(driver,u'queryjiaqin_打开假勤详情页')
                        time.sleep(3)
                        #添加断言，判断是否打开假勤详情
                        el3 = driver.find_element_by_xpath("//android.view.View[@content-desc='审批路径']").get_attribute('name')
                        print(el3)
                        try:
                            assert u'审批路径' in el3
                            print(u'打开详情页成功')
                            #模拟手机回退按钮，返回假勤记录页
                            driver.keyevent(4)
                            jietudemo.take_screenShot(driver,u'queryjiaqin_返回假勤记录页')
                            #模拟手机回退按钮，返回假勤申请页
                            driver.keyevent(4)
                            jietudemo.take_screenShot(driver,u'queryjiaqin_返回假勤申请页')
                            #模拟手机回退按钮，返回HR自助页
                            driver.keyevent(4)
                            jietudemo.take_screenShot(driver,u'queryjiaqin_返回HR自助页')
                            #模拟手机回退按钮，返回ybg首页
                            driver.keyevent(4)
                            jietudemo.take_screenShot(driver,u'queryjiaqin_返回云办公首页')
                            time.sleep(2)
                            print(u'已成功返回ybg首页')
                        except AssertionError as e:
                            jietudemo.take_screenShot(driver,u'打开假勤详情失败')
                            raise  Exception(u'打开假勤详情失败')
                    except AssertionError as e:
                        jietudemo.take_screenShot(driver,u'进入假勤记录页失败')
                        raise Exception(u'进入假勤记录页失败')
                except AssertionError as e:
                    jietudemo.take_screenShot(driver,u'打开假勤页失败')
                    raise Exception(u'打开假勤页失败')
            except AssertionError as e:
                jietudemo.take_screenShot(driver,u'打开HR自助页失败')
                raise Exception('open HRpage fail')
        except Exception as e:
            jietudemo.take_screenShot(driver, u'加载HR自助页失败')
            raise Exception(u'加载HR自助页失败')


if __name__ == '__main__':
    unittest.main()
