"""
@author:maohui
@time:2022/7/19 9:55
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

# 定义一个类：描述每个页面相同的属性和行为

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class BasePage():
    def __init__(self, driver):
        self.driver = driver

    # 元素定位
    def locator(self, loc):
        return self.driver.find_element(*loc)

    # 输入
    def input(self, loc, value):
        self.locator(loc).send_keys(value)

    # 点击
    def click(self, loc):
        self.locator(loc).click()

    #等待
    def wait_ele_presence(self,loc):
        self.wait=WebDriverWait(self.driver,30)
        self.wait.until(expected_conditions.presence_of_element_located(loc))