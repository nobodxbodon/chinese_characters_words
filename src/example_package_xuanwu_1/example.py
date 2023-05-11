from json import load as json_load
import importlib.resources

def 初始化():
    with importlib.resources.open_text("example_package_xuanwu_1.data", "word.json") as 文件:
        return json_load(文件)

原始数据 = None

# API
def 查(字):
    global 原始数据
    if 原始数据 == None:
        原始数据 = 初始化()
    符合条件 = []
    for 字数据 in 原始数据:
        if 字 == 字数据['word']:
            return 字数据
