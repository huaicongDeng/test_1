"""
1.封装业务层
2.调用page类中操作方法
需求:对ECshop登录页面进行script封装
"""
from ECShop.comon.base import open_browser
from ECShop.page.login_page import LoginPage
from ECShop.page.login_page import get_url


class LoginScript:
    def __init__(self,driver):
        """导入浏览器和实例化page类"""
        self.login_page = LoginPage(driver)
        self.login_page.open_url(get_url)
    def login_flow(self,username,password):
        """登录,不点击记住密码"""
        self.login_page.input_username(username)
        self.login_page.input_password(password)
        self.login_page.click_submit()
    def login_flow_remember(self,username,password):
        """登录,点击记住密码"""
        self.login_page.input_username(username)
        self.login_page.input_password(password)
        self.login_page.click_remember()
        self.login_page.click_submit()
    def is_login_success(self,username):
        """判断是否登录成功"""
        login_success_loc = ("class name","f4_b")
        result = self.login_page.is_text_in_element(login_success_loc,username)
        return result
if __name__ == '__main__':
    driver  =open_browser()
    login = LoginScript(driver)
    username = "诸葛亮"
    password = "Test123456"
    login.login_flow(username,password)