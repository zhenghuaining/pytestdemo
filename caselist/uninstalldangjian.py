# -*- coding: UTF-8 -*-
# #!/usr/bin/python
import unittest
import unittest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time,os,sys
import jietudemo

class ybgcaseuninstalldangjian(unittest.TestCase):
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

    def test_uninstalldangjian(self):
        driver = self.driver
        try:
            # 长按党建元素并拖动
            antion = TouchAction(driver)
            el = driver.find_element_by_xpath("//android.widget.TextView[@text='新东方党建']")
            #定位元素并根据坐标进行移动释放
            antion.long_press(el,duration=5000).move_to(x=320,y=1300).release().perform()
            jietudemo.take_screenShot(driver,u'uninstalldangjian_移动')
            #定位党建删除按钮并点击删除党建模块
            #使用xpath定位不到删除按钮
            #driver.find_element_by_xpath("//android.view.View[@resource-id='com.istone.xdf:id/drag_grid_vp_appcontainer']/android.widget.ImageView[4]").click()
            #改用坐标
            # 设定系数(以便获取元素相对路径)
            a = 365.0 / 1080
            b = 1168.0 / 1920
            x = driver.get_window_size()['width']
            y = driver.get_window_size()['height']
            #点击删除按钮（利用坐标进行定位）
            driver.tap([(a * x,b * y)])
            jietudemo.take_screenShot(driver,u'uninstalldangjian_点击删除')
            #弹出是否删除模块
            el1 = driver.find_element_by_xpath("//android.widget.Button[@resource-id='com.istone.xdf:id/btn_confirm_dialog']").text
            #断言是否弹出消息框
            try:
                assert u'确定' in el1
                print(u'成点击删除按钮弹出提示框')
                driver.find_element_by_xpath("//android.widget.Button[@resource-id='com.istone.xdf:id/btn_confirm_dialog']").click()
                time.sleep(2)
                jietudemo.take_screenShot(driver,u'uninstalldangjian_删除党建')
            except AssertionError as msg:
                #调用jietudemo方法进行截图
                jietudemo.take_screenShot(driver,u'未弹出删除框删除模块操作失败')
                raise Exception (u'未弹出删除框删除模块操作失败')
        except Exception as e:
            jietudemo.take_screenShot(driver,u'uninstalldangjian_移动失败')
            raise Exception(u'移动失败')

if __name__ == '__main__':
    unittest.main()