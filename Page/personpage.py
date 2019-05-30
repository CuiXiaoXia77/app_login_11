# 个人中心页面

from Base.Base import Base
from Page.UIElements import UIElements


class PersonPage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def person_shop_card(self):
        # 获取我的优惠券
        return self.get_element(UIElements.person_shop_cart_id).text

    def click_setting_btn(self):
        # 点击设置
        self.click_element(UIElements.person_setting_btn_id)
