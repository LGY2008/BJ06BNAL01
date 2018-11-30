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