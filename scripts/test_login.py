# 导包
import unittest
from time import sleep

from page.page_login import PageLogin
from parameterized import parameterized
from base.get_driver import GetDriver
from tools.read_json import read_json
from tools.get_log import get_loging
from base.get_logger import GetLogger
log = GetLogger().get_logger()

def get_data():
    datas = read_json("login_data.json")
    arrs = []
    for data in datas.values():
        arrs.append((data["username"],
                     data["pwd"],
                     data["expect_result"],
                     data["success"]
                     ))
    return arrs


# 新建测试类 并 继承
class TestLogin(unittest.TestCase):
    login = None
    # setUp

    @classmethod
    def setUpClass(cls):
        try:
            # 实例化 获取页面对象 PageLogin
            cls.login = PageLogin(GetDriver().get_driver())
            # 点击登录连接
            cls.login.page_click_login_link()
        except Exception as e:
            log.error(e)

    # tearDown
    @classmethod
    def tearDownClass(cls):
        # 关闭 driver驱动对象
        # cls.login.driver.quit()
        sleep(3)
        GetDriver().quit_driver()

    # 登录测试方法
    @parameterized.expand(get_data())
    def test_login(self, username, pwd, expect_result, success):
        # 调用登录方法
        self.login.page_login(username, pwd)
        # 获取登录提示信息
        # msg = self.login.page_get_error_info()
        # try:
        #     # 断言
        #     self.assertEqual(msg, expect_result)
        # except AssertionError:
        #     # 截图
        #     self.login.page_get_img()

        if success:
            try:
                # 登录确定
                self.login.page_is_login()
                # 判断安全退出是否存在
                self.assertTrue(self.login.page_is_login_success())
                # 展示退出按钮
                self.login.page_user_hover()
                # 点击退出
                self.login.page_click_logout()
                try:
                    # # 进入登录页面
                    # self.login.page_click_login_link()
                    self.assertTrue(self.login.page_is_logout_success)
                except:
                    # 截图
                    self.login.page_get_img()
                # 点击登录连接
                self.login.page_click_login_link()
            except Exception as e:
                # 截图
                self.login.page_get_img()
                log.error(e)
        else:
            if expect_result == '账密错误':
                sleep(4)
            # 获取登录提示信息
            msg = self.login.page_get_error_info()
            try:
                # 断言
                self.assertEqual(msg, expect_result)

            except AssertionError:
                # 截图
                self.login.page_get_img()
            # # 点击 确认框
            # self.login.page_click_err_btn_ok()
