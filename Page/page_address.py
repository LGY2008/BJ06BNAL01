import allure

import Page
from Base.base import Base
class PageAddress(Base):
    # 地址管理
    @allure.step("点击地管理")
    def page_click_address_manage(self):
        self.base_click(Page.address_manage)
    # 点击新增地址
    @allure.step("点击新增地址")
    def page_click_new_address(self):
        self.base_click(Page.address_add_new_btn)
    # 收件人
    @allure.step("输入收件人")
    def page_input_receipt_name(self,name):
        self.base_input(Page.address_receipt_name,name)
    # 电话
    @allure.step("输入电话")
    def page_input_phone(self,phone):
        self.base_input(Page.address_add_phone,phone)
    # 点击 所在区域
    @allure.step("点击所在区域")
    def page_click_Area(self):
        self.base_click(Page.address_area)
    # 省
    @allure.step("选择省")
    def page_click_sheng(self,sheng):
        self.base_text_click(sheng)
    # 市
    @allure.step("选择市")
    def page_click_shi(self,shi):
        self.base_text_click(shi)
    # 区
    @allure.step("选择区")
    def page_click_qu(self,qu):
        self.base_text_click(qu)
    # 点击地址封装
    def page_click_Area_sheng_shi_qu(self,sheng,shi,qu):
        # 点击所在区域
        self.page_click_Area()
        # 省
        self.page_click_sheng(sheng)
        # 市 非直辖市
        self.page_click_shi(shi)

        # # 点击市 大框
        # self.base_click(Page.address_shi_kuang)

        # # 市 直辖市
        # self.base_click(Page.address_shi)

        # 区
        self.page_click_qu(qu)
    # 输入详细地址
    @allure.step("输入详细地址")
    def page_input_info(self,info_address):
        self.base_input(Page.address_detail_addr_info,info_address)
    # 输入 邮编
    @allure.step("输入邮编")
    def page_input_post_code(self,code):
        self.base_input(Page.address_post_code,code)
    # 设为默认按钮
    @allure.step("设为默认按钮")
    def page_click_default_btn(self):
        self.base_click(Page.address_default)
    # 点击 保存
    @allure.step("点击 保存")
    def page_click_save(self,text="保存"):
        self.base_text_click(text)

    # 返回地址管理列表 收件人+电话
    @allure.step("获取 地址管理列表 收件人+电话")
    def page_get_lit_name_and_phone(self):
        # 获取的结果 如：["张三  18611110000","李四  18600002222"]
        return self.base_get_list_text(Page.addresss_name_phone)

    # 点击编辑
    @allure.step("点击 编辑")
    def page_click_edit_btn(self,text="编辑"):
        self.base_text_click(text)

    # 获取所有元素列表 并 进行点击元素操作
    @allure.step("获取所有元素列表 并 进行点击元素操作")
    def page_click_list_elements(self,text):
        self.base_text_get_elements_and_click(text)

    # 确认删除
    @allure.step("确认删除")
    def page_delete_ok(self):
        self.base_click(Page.address_delete_ok)

    # 判断是否有地址管理-
    @allure.step("判断是否有地址管理")
    def page_address_manage_is_exist(self):
        try:
            self.base_find_element(Page.address_manage,timeout=2)
            return True # 找到到地址管理
        except:
            return False # 未找到地址管理

    # 删除所有地址方法 封装
    @allure.step("删除所有地址方法")
    def page_delete_address_all(self):
        # 获取当前所有地址列表
        address_list=self.page_get_lit_name_and_phone()
        # for 循环遍历
        for i in range(len(address_list)):
            # 获取第一个地址列表 中第一个地址收件人+电话 (断言使用)
            first_text=self.page_get_address_list_text()
            # 点击编辑
            self.page_click_edit_btn()
            # 获取删除列表并点击第一个删除
            self.page_click_list_elements("删除")
            # 确定删除
            self.page_delete_ok()

            try:
                # 如果还有地址列表，那么就行断言（解决：最后一条删除后，断言又重新获取最新地址列表，而报错）
                # not: 因为def page_get_address_list_is_exist()方法，返回False为还有地址列表。
                if not self.page_get_address_list_is_exist():
                    # 获取删除后的地址列表 收件人+电话
                    print("删除的文本fist_text:",first_text)
                    print("删除后的所有列表值：",self.page_get_lit_name_and_phone())
                    assert first_text not in self.page_get_lit_name_and_phone()
            except:
                raise


    # 查找地址列表收件人和电话
    @allure.step("查找地址列表收件人和电话")
    def page_get_address_list_is_exist(self):
        try:
            self.base_find_elements(Page.addresss_name_phone,timeout=2)
            return False # 说明地址列表未删除干净
        except:
            return True # 报错说明地址列表删除干净

    # 封装获取 地址列表第一个收件人和电话
    @allure.step("地址列表第一个收件人和电话")
    def page_get_address_list_text(self):
        return self.base_find_elements(Page.addresss_name_phone)[0].text