import unittest
from tools.HTMLTestRunner import HTMLTestRunner
import time

suite = unittest.TestLoader().discover('D:/WebTest/scripts', pattern="test*.py")

report_dir = "../report/{}.html".format(time.strftime("%Y_%m_%d %H_%M_%S"))
with open(report_dir, "wb") as f:
    HTMLTestRunner(stream=f, title="淘宝登录购物测试报告", verbosity=2).run(suite)

