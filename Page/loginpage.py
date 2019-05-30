# 登录页面

from Base.Base import Base
from Page.UIElements import UIElements


class LoginPage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_login_btn(self, name, pwd):
        # 输入账号
        self.send_element(UIElements.login_account_id, name)
        # 输入密码
        self.send_element(UIElements.login_passwd_id, pwd)
        # 点击登录
        self.click_element(UIElements.login_btn_id)

    def login_close_Page(self):
        # 关闭登录页面
        # 点击登录按钮
        self.click_element(UIElements.login_close_page_btn_id)


    def if_login_btn(self):
        """判断登录按钮"""
        self.get_element(UIElements.login_close_page_btn_id)
