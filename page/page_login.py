from time import sleep

import page
from base.base import Base
from base.get_driver import GetDriver


class PageLogin(Base):
    # 点击登录链接
    def page_click_login_link(self):
        self.base_click(page.login_link)

    # 输入用户名
    def page_input_username(self, username):
        self.base_input(page.login_username, username)

    # 输入密码
    def page_input_password(self, pwd):
        self.base_input(page.login_pwd, pwd)

    # 输入验证
    def page_input_verify_code(self, code):
        self.base_input(page.login_verify_code, code)

    # 点击登录按钮
    def page_click_login_btn(self):
        self.base_click(page.login_btn)

    # 获取异常提示信息
    def page_get_error_info(self):
        return self.base_get_text(page.login_err_info)

    # 点击异常信息框 确定
    def page_click_err_btn_ok(self):
        self.base_click(page.login_err_btn_ok)

    # 截图
    def page_get_img(self):
        self.base_get_image()

    # 点击 安全退出 --》退出使用
    def page_click_logout(self):
        self.base_click(page.login_button)

    # 判断是否登录成功
    def page_is_login_success(self):
        return self.base_if_exist(page.login_success)

    # 判断是否退出成功
    def page_is_logout_success(self):
        return self.base_if_exist(page.login_link)

    # 点击确定
    def page_is_login(self):
        self.base_click(page.login_is)

    # 点击下拉框
    def page_select_click(self):
        self.base_click(page.select_line)

    # 悬停鼠标至用户名
    def page_user_hover(self):
        self.base_hover(page.login_success)

    # 是否存在验证条
    def page_code_exist(self):
        return self.base_if_exist(page.login_verify_code)

    # 拖拽验证条
    def page_code_move(self):
        self.base_move(page.login_verify_code)

    # 组合业务方法
    def page_login(self, username, pwd):
        self.page_input_username(username)
        self.page_input_password(pwd)
        # self.page_input_verify_code(code)
        self.page_click_login_btn()

if __name__ == "__main__":
    Page = PageLogin(GetDriver().get_driver())
    Page.page_click_login_link()
    Page.page_login('tb961682048', '159258wssb@')
    if Page.page_code_exist():
        Page.page_code_move()
    print(Page.page_code_exist())
    Page.page_is_login()


    # sleep(3)
    # if Page.page_is_login_success():
    #     Page.page_click_logout()
    #     Page.page_click_login_link()
    # print(Page.page_is_logout_success())



