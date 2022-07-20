"""
@author:maohui
@time:2022/7/20 14:38
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

@pytest.mark.flaky(reruns=3, reruns_delay=5)
class TestKeFuGO():
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
        desired_caps['chromeOptions'] = {'androidProcess': 'com.tencent.mm:appbrand0'
                                                           ''}

        # 连接appium server，告诉appium，代码要操作哪个设备上的哪个APP
        # 启动手机上App
        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    @classmethod
    def teardown_class(cls):
        """关闭微信界面"""
        # cls.driver.quit()
        pass

    def test_kefu_go_13(self):
        """客服的跳转"""
        WeiXinPage(self.driver).click_hjkj()
        HjKjPage(self.driver).click_servercenter()
        HjKjPage(self.driver).click_kefu()
        time.sleep(5)
        print(self.driver.contexts)
        self.driver.switch_to.context('WEBVIEW_com.tencent.mm:appbrand0')
        print(self.driver.window_handles)
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            url = self.driver.current_url
            print(url)
            if url != "https://servicewechat.com/wxa15762d564231c76/41/page-frame.html":
                assert "联系客服"==self.driver.find_element(By.XPATH,'/html/body/wx-view/wx-view[2]/wx-button/text()').text
    def test_14(self):
        pass