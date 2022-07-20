"""
@author:maohui
@time:2022/7/19 10:33
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


class WeiXinPage(BasePage):
    #元素定位符
    search_loc=(AppiumBy.ID,'com.tencent.mm:id/j5t') #搜索按钮
    search_input_loc=(AppiumBy.ID,'com.tencent.mm:id/cd7') #搜索输入框
    hjkj_loc=(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("汇健科技")') #汇健科技

    #点击汇健科技
    def click_hjkj(self):
        self.wait_ele_presence(self.hjkj_loc)
        self.click(self.hjkj_loc)

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
#     time.sleep(5)