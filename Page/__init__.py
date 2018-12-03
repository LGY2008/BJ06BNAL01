from selenium.webdriver.common.by import By
"""
    以下为百年奥莱 登录所需数据：
"""
# 点击 我
login_click_me=By.ID,"com.yunmall.lc:id/tab_me"
# 点击 已有账号，去登录
login_click_user_link=By.ID,"com.yunmall.lc:id/textView1"
# 输入 用户名
login_input_username=By.ID,"com.yunmall.lc:id/logon_account_textview"
# 输入 密码
login_input_pwd=By.ID,"com.yunmall.lc:id/logon_password_textview"
# 点击 登录
login_click_login_btn=By.ID,"com.yunmall.lc:id/logon_button"
# 获取登录后的昵称
login_get_nickname=By.ID,"com.yunmall.lc:id/tv_user_nikename"
# 点击设置
login_click_setting=By.ID,"com.yunmall.lc:id/ymtitlebar_left_btn_image"
# 拖拽 消息推送->修改密码
login_msg_send=By.ID,"com.yunmall.lc:id/setting_notification"
login_update_pwd=By.ID,"com.yunmall.lc:id/setting_modify_pwd"
# 点击 退出
login_click_logout=By.ID,"com.yunmall.lc:id/setting_logout"
# 确认 退出
login_click_logout_ok=By.ID,"com.yunmall.lc:id/ymdialog_right_button"

"""
    以下为百年奥莱 地址管理配置数据
"""
# 地址管理
address_manage=By.ID,"com.yunmall.lc:id/setting_address_manage"
# 添加地址
address_add_new_btn=By.ID,"com.yunmall.lc:id/address_add_new_btn"
# 收件人
address_receipt_name=By.ID,"com.yunmall.lc:id/address_receipt_name"
# 手机号
address_add_phone=By.ID,"com.yunmall.lc:id/address_add_phone"
# 所在区域
address_area=By.ID,"com.yunmall.lc:id/address_province"
    # 省

    # 市

    # 区
# 详细地址
address_detail_addr_info=By.ID,"com.yunmall.lc:id/address_detail_addr_info"
# 邮编
address_post_code=By.ID,"com.yunmall.lc:id/address_post_code"
# 是否设为默认地址
address_default=By.ID,"com.yunmall.lc:id/address_default"
# 收件人+电话
addresss_name_phone=By.ID,"com.yunmall.lc:id/receipt_name"
# 直辖市
address_shi=By.ID,"com.yunmall.lc:id/area_title"
# 市大框
address_shi_kuang=By.CLASS_NAME,"android.widget.RelativeLayout"
# 确认删除按钮
address_delete_ok=By.ID,"com.yunmall.lc:id/ymdialog_left_button"