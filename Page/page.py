# 统一入口类

from Page.homepage import HomePage
from Page.signpage import SignPage
from Page.personpage import PersonPage
from Page.loginpage import LoginPage
from Page.settingpage import SettingPage


class Page(object):

    def __init__(self, driver):
        self.driver = driver

    def get_home_page(self):
        # 返回首页实例化对象
        return HomePage(self.driver)

    def get_sign_page(self):
        # 返回注册页对象
        return SignPage(self.driver)

    def get_login_page(self):
        # 返回注册页面对象
        return LoginPage(self.driver)

    def get_person_page(self):
        # 返回个人执行页面对象
        return PersonPage(self.driver)

    def get_setting_page(self):
        # 返回设置页面对象
        return SettingPage(self.driver)
