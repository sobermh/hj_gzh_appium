"""
@author:maohui
@time:2022/7/20 14:30
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

from base.basepage import BasePage
from page.hjkjpage import HjKjPage
from page.reportpage import ReportPage
from page.weixinpage import WeiXinPage

# @pytest.mark.flaky(reruns=3, reruns_delay=5)
class TestReportGO():
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
        # desired_caps['resetKeyboard'] = True  # 重置键盘
        desired_caps['chromeOptions'] = {'androidProcess': 'com.tencent.mm:tools'}

        # 连接appium server，告诉appium，代码要操作哪个设备上的哪个APP
        # 启动手机上App
        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    @classmethod
    def teardown_class(cls):
        """关闭微信界面"""
        cls.driver.quit()
    def test_report_go_1(self):
        """报告查询的跳转"""
        WeiXinPage(self.driver).click_hjkj()
        HjKjPage(self.driver).click_servercenter()
        HjKjPage(self.driver).click_report()
        time.sleep(5)
        print(self.driver.contexts)
        self.driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')
        print(self.driver.window_handles)
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            url = self.driver.current_url
            if url == "http://gzh.well-healthcare.com/searchreport":
                assert "查询"==self.driver.find_element(By.XPATH,'//*[@id="submit_btn"]').text
    def test_user_error_inquire_2(self):
        """用户不存在查询"""
        BasePage(self.driver).input(ReportPage.name_input_loc,1)
        ReportPage(self.driver).phone_input()
        ReportPage(self.driver).verifyCode_input()
        ReportPage(self.driver).click_submit_btn()
        BasePage(self.driver).wait_ele_presence((By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/button'))
        actual_text=BasePage(self.driver).get_text((By.XPATH,'/html/body/div[1]/div/div[1]/div'))
        BasePage(self.driver).click((By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/button'))
        assert actual_text=='×\n该用户不存在，请确认重输'
    def test_verifycode_error_inquire_3(self):
        """验证码错误查询"""
        ReportPage(self.driver).name_input()
        ReportPage(self.driver).phone_input()
        BasePage(self.driver).input(ReportPage.verifyCode_input_loc, 1)
        ReportPage(self.driver).click_submit_btn()
        BasePage(self.driver).wait_ele_presence((By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/button'))
        actual_text = BasePage(self.driver).get_text((By.XPATH, '/html/body/div[1]/div/div[1]/div'))
        BasePage(self.driver).click((By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/button'))
        assert actual_text == '×\n验证码输入不正确'
    def test_inquire_report_4(self):
        """报告查询功能"""
        ReportPage(self.driver).name_input()
        ReportPage(self.driver).phone_input()
        ReportPage(self.driver).verifyCode_input()
        ReportPage(self.driver).click_submit_btn()
        BasePage(self.driver).wait_ele_presence((By.XPATH, '//*[@id="customerListZone"]/ul'))
        self.driver.find_element(By.XPATH, '//*[@id="customerListZone"]/ul').click()
        BasePage(self.driver).wait_ele_presence((By.XPATH, '//*[@id="sampleListZone"]/section/ul/li[2]/a'))
        assert BasePage(self.driver).get_text((By.XPATH, '//*[@id="sampleListZone"]/section/ul/li[2]/a')) == '查看报告'