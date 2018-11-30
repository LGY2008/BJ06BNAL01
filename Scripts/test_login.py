import allure
import pytest,sys,os
sys.path.append(os.getcwd())

from Base.read_txt import read_txt
from Base.read_yaml import ReadYaml
from Page.page_in import PageIn

# 获取测试数据方法
def get_data():
    # 定义空数字组
    arrs=[]
    for data in ReadYaml("login.yaml").read_yaml().values():
        arrs.append((data.get("username"),data.get("password"),data.get("expect_result"),data.get("expect_toast")))
    return arrs

# 获取测试数据 TXT
def get_data_txt():
    return read_txt("login.txt")

class TestLogin():
    def setup_class(self):
        # 实例化 统一入口类
        self.login=PageIn().page_get_pagelogin()
        # 点击 我
        self.login.page_click_me()
        # 点击 已有账号，去登录
        self.login.page_click_user_link()
    def teardown_class(self):
        # 退出 driver
        self.login.driver.quit()
    # @pytest.mark.parametrize("username,password,expect_result,expect_toast",get_data())
    # 以txt形式去读取
    @allure.step("开始执行登录用例")
    @pytest.mark.parametrize("username,password,expect_result,expect_toast",get_data_txt())
    def test_login(self,username,password,expect_result,expect_toast):
        if expect_result:
            try:
                # 输入 用户名
                self.login.page_input_username(username)
                # 输入 密码
                self.login.page_input_password(password)
                # 点击 登录
                self.login.page_click_login_btn()
                # 获取 昵称 进行断言
                assert expect_result in self.login.page_get_nickname()
                # 点击 设置
                self.login.page_click_setting()
                # 拖拽  消息推送--》修改密码
                self.login.page_drag_and_drop()
                # 点击退出
                self.login.page_click_logout()
                # 确认退出
                self.login.page_click_logout_ok()
                # 点击 我
                self.login.page_click_me()
                # 点击 已有账号，去登录
                self.login.page_click_user_link()
            except:
                # 截图
                self.login.base_getImage()
                # 打开图片 并写入报告
                with open("./Image/faild.png","rb")as f:
                    allure.attach("失败原因请附件图：",f.read(),allure.attach_type.PNG)
                # 将捕获的异常 抛出
                raise
        else:
            try:
                # 输入 用户名
                self.login.page_input_username(username)
                # 输入 密码
                self.login.page_input_password(password)
                # 点击 登录
                self.login.page_click_login_btn()
                # 断言
                assert expect_toast == self.login.base_get_toast(expect_toast)
            except:
                # 截图
                self.login.base_getImage()
                # 打开图片 并写入报告
                with open("./Image/faild.png","rb")as f:
                    allure.attach("失败原因请附件图：",f.read(),allure.attach_type.PNG)
                # 将捕获的异常 抛出
                raise