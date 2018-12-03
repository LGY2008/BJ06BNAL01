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
        with open("../Data/address.yaml","r",encoding="utf-8")as f:
            return yaml.load(f)

if __name__ == '__main__':
    # login.yaml其实对于右键方法不起任何作用，只是个占位符
    datas=ReadYaml("address.yaml").read_yaml_1()
    arrs=[]
    for data in datas.get("add_address").values():
        arrs.append((data.get("name"),data.get("phone"),data.get("sheng"),data.get("shi"),data.get("qu"),data.get("info_address"),data.get("code")))
    print(arrs)
    """
        预期格式：[("username","password","expect_toast"),()...]
    """
