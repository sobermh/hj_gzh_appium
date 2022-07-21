"""
@author:maohui
@time:2022/7/21 10:16
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
from appium import webdriver
from page.weixinpage import WeiXinPage
from page.hjkjpage import HjKjPage

from base.basepage import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By




class ReportPage(BasePage):
    #元素定位符
    name_input_loc = (By.XPATH,'//*[@id="name"]')
    phone_input_loc=(By.XPATH,'//*[@id="mobile"]')
    verifyCode_input_loc=(By.XPATH,'//*[@id="verifyCode"]')
    submit_btn_loc=(By.XPATH,'//*[@id="submit_btn"]')
    # servercenter_loc=(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("服务中心")')
    # wenjuan_loc=(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("问卷登记")')

    #输入姓名
    def name_input(self):
        self.wait_ele_presence(self.name_input_loc)
        self.input(self.name_input_loc,'毛辉')
    #输入手机号
    def phone_input(self):
        self.wait_ele_presence(self.phone_input_loc)
        self.input(self.phone_input_loc,'19357665827')
    #输入验证码
    def verifyCode_input(self):
        self.wait_ele_presence(self.verifyCode_input_loc)
        self.input(self.verifyCode_input_loc,'1234')
    #点击查询
    def click_submit_btn(self):
        self.wait_ele_presence(self.submit_btn_loc)
        self.click(self.submit_btn_loc)


if __name__ == '__main__':
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

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    WeiXinPage(driver).click_hjkj()
    HjKjPage(driver).click_servercenter()
    HjKjPage(driver).click_report()
    time.sleep(5)
    print(driver.contexts)
    driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        url = driver.current_url
        if url == "http://gzh.well-healthcare.com/searchreport":
            ReportPage(driver).name_input()

            ReportPage(driver).phone_input()
            ReportPage(driver).verifyCode_input()
            ReportPage(driver).click_submit_btn()
            BasePage(driver).wait_ele_presence((By.XPATH,'//*[@id="customerListZone"]/ul'))
            driver.find_element(By.XPATH,'//*[@id="customerListZone"]/ul').click()
            BasePage(driver).wait_ele_presence((By.XPATH, '//*[@id="sampleListZone"]/section/ul/li[2]/a'))
            assert BasePage(driver).get_text((By.XPATH, '//*[@id="sampleListZone"]/section/ul/li[2]/a'))=='查看报告'