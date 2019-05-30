# 公共方法类
import os, time, allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Base(object):
    def __init__(self, driver):
        self.driver = driver

    # 定位单个元素
    def get_element(self, loc, timeout=30, poll_frequency=1.0):
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*loc))

    # 定位一组元素
    def get_elements(self, loc, timeout=30, poll_frequency=1.0):
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(*loc))

    # 点击元素
    def click_element(self, loc, timeout=30, poll_frequency=1.0):
        self.get_element(loc, timeout, poll_frequency).click()

    # 输入内容
    def send_element(self, loc, text, timeout=30, poll_frequency=1.0):
        # 定位元素
        input_data = self.get_element(loc, timeout, poll_frequency)
        # 清空输入框
        input_data.clear()
        # 输入元素
        input_data.send_keys(text)

    def scroll_screen(self, sc=1):
        """
        滑动屏幕方法
        :param sc: 1向上;2向下;3向左;4向右
        :return:
        """
        # 获取屏幕分辨率
        time.sleep(2)
        screen_size = self.driver.get_window_size()
        # 获取宽
        width = screen_size.get("width")
        # 获取高
        height = screen_size.get("height")
        # 根据宽高判断滑动 80% -- > 20%
        if sc == 1:
            self.driver.swipe(width * 0.5, height * 0.8, width * 0.5, height * 0.2, 2000)

        if sc == 2:
            self.driver.swipe(width * 0.5, height * 0.2, width * 0.5, height * 0.8, 2000)

        if sc == 3:
            self.driver.swipe(width * 0.8, height * 0.5, width * 0.2, height * 0.5, 2000)

        if sc == 4:
            self.driver.swipe(width * 0.2, height * 0.5, width * 0.8, height * 0.5, 2000)

    def screen_page(self, name="截图"):
        """
        报告添加截图
        :param name: 截图名字
        :return:
        """
        # 定义图片名字
        png_name = "./image" + os.sep + "{}.png".format(int(time.time()))
        # 截图
        self.driver.get_screenshot_as_file(png_name)
        # 二进制打开文件
        with open(png_name, "rb") as f:
            # 使用添加附件 添加到allure报告
            allure.attach(name, f.read(), allure.attach_type.PNG)

    def get_toast(self, toast):
        """获取toast消息"""
        # 找toast
        toast_xpath = (By.XPATH, "//*[contains(@text,'{}')]".format(toast))
        return self.get_element(toast_xpath).text
