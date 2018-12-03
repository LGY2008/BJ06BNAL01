from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
class Base():
    def __init__(self,driver):
        self.driver=driver
    # 下面的方法
    def base_find_element(self,loc,timeout=30,poll=0.5):
        return WebDriverWait(self.driver,timeout=timeout,poll_frequency=poll).until(lambda x:x.find_element(*loc))
    # 查找一组元素
    def base_find_elements(self,loc,timeout=30,poll=0.5):
        return WebDriverWait(self.driver,timeout=timeout,poll_frequency=poll).until(lambda x:x.find_elements(*loc))
    # 点击
    def base_click(self,loc):
        # 调用自己封装查找元素类
        self.base_find_element(loc).click()
    # 输入
    def base_input(self,loc,text):
        el=self.base_find_element(loc)
        # 输入内容之前先清除操作  不会影响整体输入效果
        el.clear()
        # 输入内容
        el.send_keys(text)
    # 截屏
    def base_getImage(self):
        Path="./Image/faild.png"
        self.driver.get_screenshot_as_file(Path)

    # 获取toast消息方法
    def base_get_toast(self,message):
        loc=(By.XPATH,"//*[contains(@text,'"+message+"')]")
        # loc=By.XPATH,"//*[contains(@text,'%s')]"%message
        # 调用查找元素方法 注意：要return
        return self.base_find_element(loc,poll=0.1).text

    # 获取元素文本 封装
    def base_get_text(self,loc):
        # 注意：一定要将获取的文本return，否则调用的时候获取不到结果
        return self.base_find_element(loc).text

    # 拖拽元素 封装
    def base_drag_and_drop(self,el1,el2):
        # 从el1元素拖拽到el2元素的位置
        self.driver.drag_and_drop(el1,el2)

    # 封装 根据文本查找元素并点击操作
    def base_text_click(self,text):
        loc=By.XPATH,"//*[contains(@text,'"+text+"')]"
        # 调用查找元素方法 并点击
        self.base_find_element(loc).click()

    # 封装 获取一组元素指定文本
    def base_get_list_text(self,loc):
        # 以列表的形式返回元素文本
        return [i.text for i in self.base_find_elements(loc)]

    # 封装 根据文本查找一组元素并根据下标点击指定元素 默认点击第一个元素
    def base_text_get_elements_and_click(self,text,num=0):
        loc=By.XPATH,"//*[contains(@text,'"+text+"')]"
        # 调用查找元素方法 并点击
        self.base_find_elements(loc)[num].click()

