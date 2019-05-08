#导包
import ddt
import unittest
from ECShop.comon.base import open_browser
from ECShop.sricept.login_script import LoginScript
from ECShop.comon.base import Base
from ECShop.comon.operation_excel import OperationExcel
#准备测试数据
open_excel=OperationExcel(r"F:\pycharm\PyCharm 2018.3.5\ECShop\data\test_data.xlsx")
test_data=open_excel.get_data_info()
@ddt.ddt
class Testlogin(unittest.TestCase):
    def setUp(self):
        self.driver=open_browser()
        self.login=LoginScript(self.driver)
        self.base=Base(self.driver)
    @ddt.data(*test_data)
    def test_login(self,data):
        """登录不记住密码"""
        #登录流程
        self.login.login_flow(data['username'],data['password'])
        #验证是否登录成功
        result=self.login.is_login_success(data['username'])
        self.assertEqual(result,data['expect'])
    def tearDown(self):
        self.base.close_browser()
