"""
1.page.py文件继承Base类
2.封装表现层
3.封装操作层
需求:对ECshop登录页面进行封装
"""
from ECShop.comon.base import Base

get_url = "http://ecshop.itsoso.cn/user.php"
class LoginPage(Base):
    """封装表现层,制作定位器"""
    username_loc = ("name","username") # 用户名输入框
    password_loc = ("name","password") # 密码输入框
    remember_loc = ("id","remember") # 记住密码
    submit_loc = ("name","submit") # 立即登录按钮
    password_question_loc = ("link text","密码问题") # 密码问题链接---找回密码
    email_loc = ("link text","邮件")  # 找回密码---邮件
    message_loc = ("link text","短信验证") # 找回密码---短信验证
    register_loc = ("css selector","a>img") # 立即注册按钮
    home_page_loc = ("link text","首页") # 首页链接
    """封装操作层:每一个元素的操作方法都写成一个方法"""
    def input_username(self,text):
        """输入用户名"""
        self.send_keys(self.username_loc,text)
    def input_password(self,text):
        """输入密码"""
        self.send_keys(self.password_loc,text)
    def click_submit(self):
        """点击登录"""
        self.click(self.submit_loc)
    def click_remember(self):
        self.click(self.remember_loc)
if __name__ == '__main__':
    from ECShop.comon.base import open_browser
    driver = open_browser()
    login = LoginPage(driver)
    login.open_url(get_url)
    login.input_username("诸葛亮")
    login.input_password("Test123456")
    login.click_submit()
    login.close_browser()