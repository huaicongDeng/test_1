import time
import unittest
import HTMLTestRunnerPlugins

case_dir ='./case'
report_dir = './report'
now = time.strftime("%Y-%m-%d %H-%M-%S")
report_file = open(report_dir + '\\' + now + 'report.html', 'wb')
discover = unittest.defaultTestLoader.discover(case_dir, pattern='test*.py')
runner = HTMLTestRunnerPlugins.HTMLTestRunner(
    title='ECShop登录测试',
    description='不记住密码登录',
    verbosity=2,
    stream=report_file,
    retry=0
)
runner.run(discover)
report_file.close()
