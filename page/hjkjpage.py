"""
@author:maohui
@time:2022/7/19 13:47
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

from base.basepage import BasePage
from appium.webdriver.common.appiumby import AppiumBy

from page.weixinpage import WeiXinPage


class HjKjPage(BasePage):
    #元素定位符
    aboutus_loc = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("关于我们")')
    productcenter_loc=(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("产品中心")')
    productlist_loc=(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("产品列表")')
    hjstore_loc=(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("汇健商城")')
    servercenter_loc=(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("服务中心")')
    wenjuan_loc=(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("问卷登记")')
    sample_loc=(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("样本寄回")')
    logistics_loc=(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("物流查询")')
    report_loc=(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("报告查询")')
    kefu_loc=(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("在线客服")')

    #点击关于我们
    def click_aboutus(self):
        self.wait_ele_presence(self.aboutus_loc)
        self.click(self.aboutus_loc)
    #点击产品中心
    def click_productcenter(self):
        self.wait_ele_presence(self.productcenter_loc)
        self.click(self.productcenter_loc)
    #点击汇健商城
    def click_hjstore(self):
        self.wait_ele_presence(self.hjstore_loc)
        self.click(self.hjstore_loc)
    #点击产品列表
    def click_productlist(self):
        self.wait_ele_presence(self.productlist_loc)
        self.click(self.productlist_loc)
        # 点击服务中心
    def click_servercenter(self):
        self.wait_ele_presence(self.servercenter_loc)
        self.click(self.servercenter_loc)
        # 点击问卷登记
    def click_wenjuan(self):
        self.wait_ele_presence(self.wenjuan_loc)
        self.click(self.wenjuan_loc)
        # 点击样本寄回
    def click_sample(self):
        self.wait_ele_presence(self.sample_loc)
        self.click(self.sample_loc)
        # 点击物流查询
    def click_logistics(self):
        self.wait_ele_presence(self.logistics_loc)
        self.click(self.logistics_loc)
        # 点击报告查询
    def click_report(self):
        self.wait_ele_presence(self.report_loc)
        self.click(self.report_loc)
        # 点击在线客服
    def click_kefu(self):
        self.wait_ele_presence(self.kefu_loc)
        self.click(self.kefu_loc)

# if __name__ == '__main__':
#     desired_caps = {}  # 包装
#     desired_caps['platformName'] = 'Android'  # 系统名称
#     desired_caps['platformVersion'] = '10'  # 系统的版本号
#     desired_caps['deviceName'] = 'Redmi_7A'  # 设备名称,这个没有严格的规定,但是一定要有
#     desired_caps['appPackage'] = 'com.tencent.mm'  # APP包名
#     desired_caps['appActivity'] = '.ui.LauncherUI'  # APP入口的activity
#     desired_caps['noReset'] = True  # 不重置app的缓存文件
#     # desired_caps['fullReset'] = False  # 不重置app的缓存文件
#     desired_caps['unicodeKeyboard'] = True  # 设置键盘支持中文输入
#     desired_caps['resetKeyboard'] = True  # 重置键盘
#
#     # 连接appium server，告诉appium，代码要操作哪个设备上的哪个APP
#     # 启动手机上App
#
#     driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
#     WeiXinPage(driver).click_hjkj()
#     HjKjPage(driver).click_productcenter()
#     HjKjPage(driver).click_productlist()
#     time.sleep(5)