import os
def read_txt(filename):
    with open(os.getcwd()+os.sep+"Data"+os.sep+filename,"r",encoding="utf-8")as f:
        arrs=[]
        for i in f.readlines():
            arrs.append(tuple(i.strip().split(",")))
        return arrs

def read_txt_1():
    with open("../Data/login.txt","r",encoding="utf-8")as f:
        arrs=[]
        for i in f.readlines():
            arrs.append(tuple(i.strip().split(",")))
        return arrs

if __name__ == '__main__':

    print(read_txt_1())

"""
    1. f.readlines() 返回列表
    2. i.strip() 去除字符串前后空格、换行符，返回结果为字符串
    3. split(",") 以逗号去拆分字符串，并以列表形式返回
    4. 由于是遍历每行，所需必须将每行存储到列表中 返回结果为[[],[]]
    5. 预期结果：[(),()],必须将tuple([[],[]])强转元组
"""