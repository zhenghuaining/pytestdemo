# -*- coding: UTF-8 -*-
# #!/usr/bin/python
import unittest
import unittest
from appium import webdriver
import time,os,sys
import jietudemo
class ybgcaseinstalldangjian(unittest.TestCase):
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


    def test_ybginstalldangjian(self):
        driver = self.driver
        #定位添加应用按钮并点击
        driver.find_element_by_xpath("//android.widget.TextView[@text='添加应用']").click()
        jietudemo.take_screenShot(driver,'installdangjia_addapppage')
        element1 = driver.find_element_by_xpath("//android.widget.TextView[@text='选择兴趣或职位,我们将为您推荐相关应用']").text
        try:
            assert u'选择兴趣或职位,我们将为您推荐相关应用' in element1
            print(u'跳转安装应用页成功')
            #定位搜索框并输入党建关键字搜索
            driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.istone.xdf:id/tv_search_apps']").click()
            jietudemo.take_screenShot(driver,u'installdangjian_定位搜索框')
            driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.istone.xdf:id/et_search_contacts']").send_keys(u'党建')
            jietudemo.take_screenShot(driver,u'installdangjian_输入关键字党建')
            #在搜索结果中点击立即体验
            driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.istone.xdf:id/tv_appstore_item_update']").click()
            jietudemo.take_screenShot(driver,u'installdangjian_安装')
            #点击回退按钮，回退至搜索页
            driver.find_element_by_xpath("//android.widget.RelativeLayout[@resource-id='com.istone.xdf:id/rl_back']").click()
            jietudemo.take_screenShot(driver,u'installdangjian_搜索页')
            #再点击回退按钮，回退至首页
            driver.find_element_by_xpath("//android.widget.RelativeLayout[@resource-id='com.istone.xdf:id/rl_back']").click()
            jietudemo.take_screenShot(driver,u'installdangjian_首页')
            # 元素text党建用于断言
            element2 = driver.find_element_by_xpath("//android.widget.TextView[@text='新东方党建']").text
            try:
                assert u'新东方党建' in element2
                print(u'党建模块安装成功')
            except AssertionError as e:
                #调用jietudemo方法截图
                jietudemo.take_screenShot(driver,u'安装党建应用失败')
                print(u'安装党建应用失败，未找到安装的党建模块')

        except AssertionError as e:
            #调用jietudemo方法进行截图
            jietudemo.take_screenShot(driver,u'跳转安装应用页失败，用例退出')
            print(u'跳转安装应用页失败，用例退出')



if __name__ == '__main__':
    unittest.main()