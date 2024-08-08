import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from tools.get_log import get_loging
from base.get_logger import GetLogger
# log = get_loging()
log = GetLogger().get_logger()

class Base:
    # 初始化
    def __init__(self, driver):
        log.info("初始化driver")
        self.driver = driver
        # 临时代替driver
        # option = webdriver.ChromeOptions()
        # option.add_experimental_option('excludeSwitches', ['enable-automation'])
        # option.add_argument("disable-blink-features=AutomationControlled")
        # self.driver = webdriver.Chrome(chrome_options=option)
        # self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument",{
        #     "source": """
        #     Object.defineProperty(navigator, 'webdriver', {
        #         get: () => undefined
        #     })
        #     """
        # })
        # self.driver.maximize_window()
        # self.driver.get('https://www.taobao.com/')

    # 查找元素方法 (提供：点击、输入、获取文本)使用
    def base_find_element(self, loc, timeout=30, poll=0.5):
        log.info("正在查找元素：{}".format(loc))
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 点击方法
    def base_click(self, loc):
        log.info("正在点击元素：{}".format(loc))
        self.base_find_element(loc).click()

    # 悬停鼠标
    def base_hover(self, loc):
        ActionChains(self.driver).move_to_element(self.base_find_element(loc)).perform()

    # 拖拽鼠标
    def base_move(self, loc):
        ActionChains(self.driver).click_and_hold(self.base_hover(loc)).perform()
        ActionChains(self.driver).move_by_offset(xoffset=1000, yoffset=0).perform()

    # 输入方法
    def base_input(self, loc, value):
        log.info("正在查找元素：{}".format(loc))
        el = self.base_find_element(loc)
        # 清空
        log.info("正在清空元素{}内容".format(loc))
        el.clear()
        # 输入
        log.info("元素{}正在输入内容：{}".format(loc, value))
        el.send_keys(value)

    # 获取文本方法
    def base_get_text(self, loc):
        # 注意：一定要返回元素的文本信息
        return self.base_find_element(loc).text

    # 截图方法
    def base_get_image(self):
        self.driver.get_screenshot_as_file("D:/WebTest/image/{}.png"
                                           .format(time.strftime("%Y_%m_%d %H_%M_%S")))

    # 封装判断元素是否存在
    def base_if_exist(self, loc):
        try:
            self.base_find_element(loc, timeout=2)
            log.info("是否存在元素：{}".format(loc))
            # 找到元素  aseertTrue
            return True
        except:
            # 没找到元素
            return False

    # 主页面句柄
    def base_page_main(self):
        return self.driver.current_window_handle

    def base_page_change(self, Main_Page):
        for Page in self.driver.window_handles:
            if Page != Main_Page:
                self.driver.switch_to.window(Page)

    def base_to_main(self, Main_Page):
        self.driver.switch_to.window(Main_Page)
