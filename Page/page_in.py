from Base.get_driver import get_driver
from Page.page_address import PageAddress
from Page.page_login import PageLogin
# 获取driver
driver=get_driver()
class PageIn():
    # 获取 PageLogin对象
    def page_get_pagelogin(self):
        return PageLogin(driver)

    # 获取 PageAddress对象
    def page_get_pageaddress(self):
        return PageAddress(driver)