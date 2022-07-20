"""
@author:maohui
@time:2022/7/20 14:08
  　　　　　　　 ┏┓    ┏┓+ +
  　　　　　　　┏┛┻━━━━┛┻┓ + +
  　　　　　　　┃        ┃ 　 
  　　　　　　　┃     ━  ┃ ++ + + +
  　　　　　 　████━████ ┃+
  　　　　　　　┃        ┃ +
  　　　　　　　┃   ┻    ┃
  　　　　　　　┃        ┃ + +
  　　　　　　　┗━┓   ┏━━┛
  　　　　　　　  ┃   ┃
  　　　　　　　  ┃   ┃ + + + +
  　　　　　　　  ┃   ┃　　　Code is far away from bug with the animal protecting
  　　　　　　　  ┃   ┃+ 　　　　神兽保佑,代码无bug
  　　　　　　　  ┃   ┃
  　　　　　　　  ┃   ┃　　+
  　　　　　　　  ┃   ┗━━━━━━━┓ + +     
  　　　　　　　  ┃           ┣┓
  　　　　　　　  ┃           ┏┛
  　　　　　　　  ┗┓┓┏━━━━━┳┓┏┛ + + + +
  　　　　　　　   ┃┫┫     ┃┫┫
  　　　　　　　   ┗┻┛     ┗┻┛+ + + +
"""

import time

import pytest
from appium import webdriver
from selenium.webdriver.common.by import By

from page.hjkjpage import HjKjPage
from page.weixinpage import WeiXinPage

@pytest.mark.flaky(reruns=3, reruns_delay=10)
class TestSampleGO():
    @classmethod
    def setup_class(cls):
        """初始化打开微信界面"""
        desired_caps = {}  # 包装
        desired_caps['platformName'] = 'Android'  # 系统名称
        desired_caps['platformVersion'] = '10'  # 系统的版本号
        desired_caps['deviceName'] = 'Redmi_7A'  # 设备名称,这个没有严格的规定,但是一定要有
        desired_caps['appPackage'] = 'com.tencent.mm'  # APP包名
        desired_caps['appActivity'] = '.ui.LauncherUI'  # APP入口的activity
        desired_caps['noReset'] = True  # 不重置app的缓存文件
        # desired_caps['fullReset'] = False  # 不重置app的缓存文件
        desired_caps['unicodeKeyboard'] = True  # 设置键盘支持中文输入
        desired_caps['resetKeyboard'] = True  # 重置键盘
        desired_caps['chromeOptions'] = {'androidProcess': 'com.tencent.mm:tools'}

        # 连接appium server，告诉appium，代码要操作哪个设备上的哪个APP
        # 启动手机上App
        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    @classmethod
    def teardown_class(cls):
        """关闭微信界面"""
        # cls.driver.quit()
        pass

    def test_sample_go_07(self):
        """样本寄回的跳转"""
        WeiXinPage(self.driver).click_hjkj()
        HjKjPage(self.driver).click_servercenter()
        HjKjPage(self.driver).click_sample()
        time.sleep(5)
        print(self.driver.contexts)
        self.driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')
        print(self.driver.window_handles)
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            url = self.driver.current_url
            if url == "http://gzh.well-healthcare.com/deliverpage":
                assert "寄回的样本条码"==self.driver.find_element(By.XPATH,'//*[@id="postForm"]/h3[1]').text
    def test_08(self):
        pass