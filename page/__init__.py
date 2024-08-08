from selenium.webdriver.common.by import By

"""以下为登录页面元素配置信息"""
# 登录链接
url = "https://www.taobao.com/"
# 登录链接
login_link = By.PARTIAL_LINK_TEXT, "亲，请登录"
# login_link = By.CSS_SELECTOR, ".cbtn_lg"
# 用户名
login_username = By.ID, "fm-login-id"
# 密码
login_pwd = By.ID, "fm-login-password"
# 验证码
login_verify_code = By.ID, "nc_1_n1z"
# 登录按钮
login_btn = By.CSS_SELECTOR, ".fm-button.fm-submit.password-login"
# 获取异常文本信息
login_err_info = By.CSS_SELECTOR, ".login-error-msg"
# 点击异常提示框 按钮
login_err_btn_ok = By.CSS_SELECTOR, ".layui-layer-btn0"
# 安全退出
login_button = By.PARTIAL_LINK_TEXT, "退出"
# 进入验证环境
# login_logout = By.PARTIAL_LINK_TEXT, "手机扫码安全登录"
login_logout = By.CSS_SELECTOR, ".fm-button.fm-submit.password-login"
# 确定按钮
login_is = By.CSS_SELECTOR, ".dialog-btn.dialog-btn-feedback.primary"
# 登录成功账户
login_success = By.CSS_SELECTOR, ".site-nav-login-info-nick"
# 下拉框
select_line = By.CSS_SELECTOR, ".site-nav-icon"

"""以下为订单页面配置数据"""
# 商品搜索框
search_box = By.ID, "q"
# 搜索按钮
search_btn = By.CSS_SELECTOR, ".btn-search"
# 商品条目
commodity = By.CSS_SELECTOR, ".MainPic--mainPic--rcLNaCv"
# 购物车页面
shopping_cart_page = By.PARTIAL_LINK_TEXT, "购物车"
# 淘宝页面
taobao_page = By.CSS_SELECTOR, "[data-spm-click='gostr=/newpcsearch.item_search.pc_taobao_tab_cli;locaid=dpc_taobao;']"
# 加入购物车
# shopping_cart_button = By.CSS_SELECTOR, "style=[background
# ='background: linear-gradient(90deg, rgb(255, 203, 0), rgb(255, 148, 2)); vertical-align: top;']"
shopping_cart_button = By.XPATH, "//div[@class='Actions--leftButtons--2fasaTH']/button[2]"
# 商品子类
commodity_sub = By.CSS_SELECTOR, ".SkuContent--valueItem--1Q1b8S3"
# 全选购物车商品
cart_checkbox = By.CSS_SELECTOR, ".ant-checkbox-input"
# 结算按钮
shop_settlement = By.CSS_SELECTOR, ".btn--QDjHtErD"
# 提交订单按钮
shop_submit = By.CSS_SELECTOR, ".go-btn"
