import os, sys, pytest

sys.path.append(os.getcwd())
from Page.page import Page

from Base.getfiledata import GetFileDate
from Base.get_driver import get_driver


def get_login_data():
    # 预期失败列表
    fail_list = []
    # 预期成功列表
    suc_list = []
    # 读取yaml数据
    login_data = GetFileDate().get_yaml_data("logindata.yml")
    for i in login_data:

        if login_data.get(i).get("toast"):
            # 预期失败测试用例
            fail_list.append((i, login_data.get(i).get("account"), login_data.get(i).get("passwd")
                              , login_data.get(i).get("toast"), login_data.get(i).get("expect_data")))

        else:
            # 预期失败的测试用例
            suc_list.append((i, login_data.get(i).get("account")
                             , login_data.get(i).get("passwd"), login_data.get(i).get("expect_data")))
    return {"suc": suc_list, "fail": fail_list}


# print(get_login_data())

class TestLogin(object):

    def setup_class(self):
        self.driver = get_driver("com.yunmall.lc", "com.yunmall.ymctoc.ui.activity.MainActivity")
        self.page_obj = Page(self.driver)

    def teardown_class(self):
        self.driver.quit()

    @pytest.fixture(autouse=True)
    def auto_in_login(self):
        # 自动进入登录页面
        # 点击首页我
        self.page_obj.get_home_page().click_my_btn()
        # 点击注册页已有账号去登录
        self.page_obj.get_sign_page().click_sign_exits_acc_btn()

    @pytest.mark.parametrize("case_num, account, passwd, exp_data", get_login_data().get("suc"))
    def test_login_suc(self, case_num, account, passwd, exp_data):

        # # 点击首页我
        # self.page_obj.get_home_page().click_my_btn()
        # # 点击注册页已有账号去登陆
        # self.page_obj.get_sign_page().click_sign_exits_acc_btn()
        # 输入用户名,密码,点击登录--进入个人中心页面
        self.page_obj.get_login_page().click_login_btn(account, passwd)
        try:
            # 获取我的优惠券
            shop_card = self.page_obj.get_person_page().person_shop_card()

            try:
                account == shop_card

            except AssertionError:
                """停留在个人中心页,需要执行退出操作"""
                # 截图
                self.page_obj.get_login_page().screen_page()
                assert False
            finally:
                # 点击设置
                self.page_obj.get_person_page().click_setting_btn()
                # 点击退出
                self.page_obj.get_setting_page().logout()

        except TimeoutError:
            # 截图
            self.page_obj.get_login_page().screen_page()
            # 关闭页面
            self.page_obj.get_login_page().login_close_Page()
            assert False

    @pytest.mark.parametrize("case_num, account, passwd, toast,exp_data", get_login_data().get("fail"))
    def test_login_fail(self, case_num, account, passwd, toast, exp_data):
        # # 点击首页我
        # self.page_obj.get_home_page().click_my_btn()
        # # 点击注册页已有账号去登陆
        # self.page_obj.get_sign_page().click_sign_exits_acc_btn()
        # 输入用户名,密码,点击登录---进入个人中心
        self.page_obj.get_login_page().click_login_btn(account, passwd)
        try:
            # 获取toast消息
            toast_data = self.page_obj.get_login_page().get_toast(toast)
            try:
                # 判断登录按钮是否存在
                self.page_obj.get_login_page().if_login_btn()
                # 断言
                assert toast_data == exp_data
                # 关闭登录按钮
                self.page_obj.get_login_page().login_close_Page()

            except TimeoutError:
                """获取到toast错误提示,但是登录成功"""
                # 截图
                self.page_obj.get_login_page().screen_page()
                # 点击设置
                self.page_obj.get_person_page().click_setting_btn()
                # 点击退出
                self.page_obj.get_setting_page().logout()
                assert False

            except AssertionError:
                """登录页面"""
                # 截图
                self.page_obj.get_setting_page().screen_page()
                # 关闭登录按钮
                self.page_obj.get_login_page().login_close_Page()
                assert False


        except TimeoutError:
            # 找不到toast
            # 截图
            self.page_obj.get_setting_page().screen_page()
            try:
                """登录页面"""
                # 登录按钮
                self.page_obj.get_login_page().if_login_btn()
                # 关闭登录页面
                self.page_obj.get_login_page().login_close_Page()

            except TimeoutError:
                """个人中心页面"""
                # 点击设置
                self.page_obj.get_person_page().click_setting_btn()
                # 点击退出
                self.page_obj.get_setting_page().logout()
            assert False
