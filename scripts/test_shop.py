# 导包
import unittest
from time import sleep

from page.page_login import PageLogin
from page.page_shop import PageShop
from parameterized import parameterized
from base.get_driver import GetDriver
from base.get_logger import GetLogger
from tools.read_json import read_json
log = GetLogger().get_logger()

def get_data():
    datas = read_json("shop_data.json")
    arrs = []
    for data in datas.values():
        arrs.append((data["commodity"]
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
            # 实例化 shop对象
            cls.shop = PageShop(GetDriver().get_driver())
            # 点击登录连接
            cls.login.page_click_login_link()
            cls.login.page_login('tb961682048', '159258wssb@')
            cls.login.page_is_login()
            cls.shop.page_search_click()
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
    def test_shop001(self, commodity):
        # 加入购物车行动
        self.shop.page_shop(commodity)
        # 返回搜索页面
        self.shop.page_to_search()

    def test_shop002(self):
        self.shop.page_cart_open()
        self.shop.page_cart_check()
        print(self.shop.page_cart_settle())
        # print(self.shop.page_submit())


