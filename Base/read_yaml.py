import os
import yaml


class ReadYaml():
    def __init__(self,filename):
        self.filepath=os.getcwd()+os.sep+"Data"+os.sep+filename
    def read_yaml(self):
        with open(self.filepath,"r",encoding="utf-8")as f:
            return yaml.load(f)

    # 以下方法 右键调试所使用
    def read_yaml_1(self):
        with open("../Data/login.yaml","r",encoding="utf-8")as f:
            return yaml.load(f)

if __name__ == '__main__':
    # login.yaml其实对于右键方法不起任何左右，只是个占位符
    datas=ReadYaml("login.yaml").read_yaml_1().values()
    arrs=[]
    for data in datas:
        arrs.append((data.get("username"),data.get("password"),data.get("expect_result"),data.get("expect_toast")))
    print(arrs)
    """
        预期格式：[("username","password","expect_toast"),()...]
    """
