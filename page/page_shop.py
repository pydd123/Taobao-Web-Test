from time import sleep

import page
from base.base import Base
from base.get_driver import GetDriver
from page.page_login import PageLogin

class PageShop(Base):
    # 商品信息查找
    def page_shop_search(self, commodity):
        self.base_input(page.search_box, commodity)

    # 点击搜索按钮
    def page_search_click(self):
        self.base_click(page.search_btn)

    # 选择商品
    def page_commodity_confirm(self):
        self.base_click(page.commodity)

    # 打开购物车
    def page_cart_open(self):
        self.base_click(page.shopping_cart_page)

    # 切换到淘宝页面
    def page_taobao(self):
        self.base_click(page.taobao_page)

    # 切换到商店主页面
    def page_to_commodity(self):
        Main_Page = self.base_page_main()
        self.base_page_change(Main_Page)

    # 切换回搜索页面
    def page_to_search(self):
        Main_Page = self.base_page_main()
        self.base_to_main(Main_Page)

    # 选择商品子类
    def page_commodity_sub(self):
        self.base_click(page.commodity_sub)

    # 加入购物车
    def page_cart_joint(self):
        self.base_click(page.shopping_cart_button)

    # 购物车商品全选
    def page_cart_check(self):
        self.base_click(page.cart_checkbox)

    # 结算
    def page_cart_settle(self):
        return self.base_if_exist(page.shop_settlement)

    # 提交订单
    def page_submit(self):
        return self.base_if_exist(page.shop_submit)

    # 组合业务方法
    def page_shop(self, commodity):
        self.page_shop_search(commodity)
        self.page_search_click()
        self.page_taobao()
        self.page_commodity_confirm()
        self.page_to_commodity()
        self.page_commodity_sub()
        self.page_cart_joint()
        # self.page_cart_open()
        # self.page_cart_check()

if __name__ == "__main__":
    driver = GetDriver().get_driver()
    Page = PageLogin(driver)
    Page.page_click_login_link()
    Page.page_login('tb961682048', '159258wssb@')
    Page.page_is_login()
    Shop = PageShop(driver)
    Shop.page_shop("零食")
    Shop.page_cart_open()
    Shop.page_cart_check()
    print(Shop.page_cart_settle())




