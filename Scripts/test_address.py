import os,sys
sys.path.append(os.getcwd())

import allure
from Base.read_yaml import ReadYaml
import pytest
from Page.page_in import PageIn
def get_data(data_type):
    arrs = []
    if data_type=="add":
        for data in ReadYaml("address.yaml").read_yaml().get("add_address").values():
            arrs.append((data.get("name"),data.get("phone"),data.get("sheng"),data.get("shi"),data.get("qu"),data.get("info_address"),data.get("code")))
        return arrs
    elif data_type=="update":
        for data in ReadYaml("address.yaml").read_yaml().get("update_address").values():
            arrs.append((data.get("name"),data.get("phone"),data.get("sheng"),data.get("shi"),data.get("qu"),data.get("info_address"),data.get("code")))
        return arrs
def get_data1():
    return [("王五","18011112222","江苏","南京","白下","朝阳公园，天安门1号","100090")]
class TestAddress():
    def setup_class(self):
        # 实例化统一入口类
        page=PageIn()
        # 调用登录 方法
        page.page_get_pagelogin().page_login_and_setting()
        # 获取 PageAddress对象
        self.address=page.page_get_pageaddress()
    def teardown_class(self):
        # 关闭driver
        self.address.driver.quit()
    # 新增地址方法
    @allure.step("开始新增地址操作")
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("name,phone,sheng,shi,qu,info_address,code",get_data("add"))
    def test_add_address(self,name,phone,sheng,shi,qu,info_address,code):
        add=self.address
        # 点击 地址管理
        add.page_click_address_manage()
        # 点击 新增地址
        add.page_click_new_address()
        # 收件人
        add.page_input_receipt_name(name)
        # 手机号
        add.page_input_phone(phone)
        # 所在区域
        add.page_click_Area_sheng_shi_qu(sheng,shi,qu)
        # 详细地址
        add.page_input_info(info_address)
        # 邮编
        add.page_input_post_code(code)
        # 设为默认地址
        add.page_click_default_btn()
        # 保存
        add.page_click_save()
        # 断言
        try:
            # 拼接 收件+电话 格式："张三  18600001111"
            expect_result=name+"  "+phone
            assert expect_result in add.page_get_lit_name_and_phone()
        except:
            # 截图
            self.login.base_getImage()
            # 打开图片 并写入报告
            with open("./Image/faild.png", "rb")as f:
                allure.attach("失败原因请附件图：", f.read(), allure.attach_type.PNG)
            # 将捕获的异常 抛出
            raise
    @allure.step("开始更新地址操作")
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("name,phone,sheng,shi,qu,info_address,code", get_data("update"))
    def test_update_address(self,name,phone,sheng,shi,qu,info_address,code):
        add = self.address
        # 点击编辑
        add.page_click_edit_btn()
        # 点击修改
        add.page_click_list_elements("修改")
        # 输入收件人
        add.page_input_receipt_name(name)
        # 收入手机号
        add.page_input_phone(phone)
        # 所在地区
        add.page_click_Area_sheng_shi_qu(sheng,shi,qu)
        # 详细地址
        add.page_input_info(info_address)
        # 邮编
        add.page_input_post_code(code)
        # 保存
        add.page_click_save()
        # 断言
        try:
            # 拼接 收件+电话 格式："张三  18600001111"
            expect_result=name+"  "+phone
            assert expect_result in add.page_get_lit_name_and_phone()
        except:
            # 截图
            self.login.base_getImage()
            # 打开图片 并写入报告
            with open("./Image/faild.png", "rb")as f:
                allure.attach("失败原因请附件图：", f.read(), allure.attach_type.PNG)
            # 将捕获的异常 抛出
            raise

    # 删除地址方法
    @pytest.mark.run(order=3)
    @allure.step("开始删除地址操作")
    def test_delete_address(self):
        if self.address.page_address_manage_is_exist():
            # 点击地址管理
            self.address.page_click_address_manage()
        """删除单个方法"""
        # # 点击编辑
        # self.address.page_click_edit_btn()
        # # 点击删除
        # self.address.page_click_list_elements("删除")
        # # 确认删除
        # self.address.page_delete_ok()

        """删除多个方法"""
        # 调用所有删除所有地址方法
        self.address.page_delete_address_all()
        try:
            # 断言地列表是否还存在地址
            assert self.address.page_get_address_list_is_exist()
        except:
        # 截图
            self.login.base_getImage()
            # 打开图片 并写入报告
            with open("./Image/faild.png", "rb")as f:
                allure.attach("失败原因请附件图：", f.read(), allure.attach_type.PNG)
            # 将捕获的异常 抛出
            raise