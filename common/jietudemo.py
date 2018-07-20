#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import time

def take_screenShot(driver ,name = "takeShot"):
    '''
    method explain:获取当前屏幕的截图
    parameter explain：【name】 截图的名称
    Usage:
        device.take_screenShot(u"个人主页")   #实际截图保存的结果为：2018-01-13_17_10_58_个人主页.png
    '''
    day = time.strftime("%Y-%m-%d" ,time.localtime(time.time()))
    #fq = "D:\\pytestdemo\\png" +day
    fq = "\\pytestdemo\\png" + day
    #fq = os.getcwd()[:-4] +'png\\'+day    #根据获取的路径，然后截取路径保存到自己想存放的目录下
    tm = time.strftime("%Y-%m-%d_%H_%M_%S",time.localtime(time.time()))
    filename = ""
    if os.path.exists(fq):
        filename = fq +"\\ " +tm +"_ " +name +'.png'
    else:
        os.makedirs(fq)
        filename = fq +"\\ " +tm +"_ " +name +'.png'
    # c = os.getcwd()
    # r"\\".join(c.split("\\"))     #此2行注销实现的功能为将路径中的\替换为\\
    driver.get_screenshot_as_file(filename)
    print fq