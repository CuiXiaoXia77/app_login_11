#测试脚本
from selenium.webdriver.common.by import By

from Page.page import Page
from Base.get_driver import get_driver

#实例化driver
driver = get_driver("com.yunmall.lc","com.yunmall.ymctoc.ui.activity.MainActivity")
#实例化统一入口类
page_obj = Page(driver)

#点击首页我
page_obj.get_home_page().click_my_btn()
#点击注册页已有账号去登陆
page_obj.get_sign_page().click_sign_exits_acc_btn()
#点击登录页面
page_obj.get_login_page().click_login_btn("13937631003","12345")

#获取提示信息
#获取错误提示信息xpath
error_message = (By.XPATH,"//*[contains(@text,'登录密码错误')]")
message = page_obj.get_setting_page().get_element(error_message,timeout=5,poll_frequency=0.5).text
print(message)
#获取我的优惠券
# print("信息:{}".format(page_obj.get_person_page().person_shop_card()))
#点击设置
# page_obj.get_person_page().click_setting_btn()
#点击退出按钮
# page_obj.get_setting_page().logout()