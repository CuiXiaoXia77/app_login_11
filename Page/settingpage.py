# 设置页面

from Base.Base import Base
from Page.UIElements import UIElements


class SettingPage(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def logout(self, tag=1):
        """退出操作"""
        # 滑动
        self.scroll_screen()
        # 点击退出按钮
        self.click_element(UIElements.setting_logout_btn_id)
        if int(tag) == 1:
            # 点击确认退出
            self.click_element(UIElements.setting_acc_quit_btn_id)

        else:
            # 点击取消退出
            self.click_element(UIElements.setting_dis_quit_btn_id)
