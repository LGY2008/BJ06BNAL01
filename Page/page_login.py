import allure

import Page
from Base.base import Base
class PageLogin(Base):
    # 点击 我
    @allure.step("点击我")
    def page_click_me(self):
        self.base_click(Page.login_click_me)
    # 点击 已有账号，去登录
    @allure.step("点击 已有账号，去登录")
    def page_click_user_link(self):
        self.base_click(Page.login_click_user_link)
    # 输入 用户名
    @allure.step("输入 用户名")
    def page_input_username(self,username):
        self.base_input(Page.login_input_username,username)
    # 输入 密码
    @allure.step("输入 密码")
    def page_input_password(self, password):
        self.base_input(Page.login_input_pwd, password)
    # 点击 登录
    @allure.step("点击登录")
    def page_click_login_btn(self):
        self.base_click(Page.login_click_login_btn)
    # 获取登_录后的昵称
    @allure.step("获取登录昵称")
    def page_get_nickname(self):
        # 注意：必须要有return 否则断言获取不到结果
        return self.base_get_text(Page.login_get_nickname)
    # 点击设置
    @allure.step("点击 设置")
    def page_click_setting(self):
        self.base_click(Page.login_click_setting)
    # 拖拽 消息推送->修改密码
    @allure.step("拖拽 消息推送->修改密码")
    def page_drag_and_drop(self):
        # 消息推送
        el1=self.base_find_element(Page.login_msg_send)
        # 修改密码
        el2=self.base_find_element(Page.login_update_pwd)
        # 调用 拖拽方法
        self.base_drag_and_drop(el1,el2)
    # 点击 退出
    @allure.step("点击 退出")
    def page_click_logout(self):
        self.base_click(Page.login_click_logout)
    # 确认 退出
    @allure.step("确认 退出")
    def page_click_logout_ok(self):
        self.base_click(Page.login_click_logout_ok)
