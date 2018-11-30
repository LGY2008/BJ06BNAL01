from appium import webdriver
def get_driver():
    # server 启动参数
    desired_caps = {}
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    #mumu
    # desired_caps['platformVersion'] = '6.0.1'
    desired_caps['deviceName'] = '192.168.56.101:5555'
    # 雷电模拟器
    # desired_caps['deviceName'] = 'emulator-5554'
    # mumu
    # desired_caps['deviceName'] = '127.0.0.1:7555'
    # 设置中文
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True

    # 获取toast消息
    desired_caps['automationName'] = 'Uiautomator2'

    # app的信息 /
    desired_caps['appPackage'] = 'com.yunmall.lc'
    desired_caps['appActivity'] = 'com.yunmall.ymctoc.ui.activity.MainActivity'
    # 声明我们的driver对象
    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    """以下测试driver方法使用"""
