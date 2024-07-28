from json import load as json_load
import importlib.resources
from chinese_characters_words import 字典

成语数据 = None

def 初始化():
    global 成语数据
    with importlib.resources.open_text("chinese_characters_words.数据", "成语.json") as 文件:
        成语数据 = json_load(文件)


# API
def 查成语(词):
    if 成语数据 == None:
        初始化()

    for 词数据 in 成语数据:
        if 词 == 词数据['word']:
            信息 = {}
            信息['词'] = 词数据['word']
            信息['释义'] = 词数据['explanation']
            信息['例句'] = 词数据['example']
            信息['渊源'] = 词数据['derivation']
            信息['拼音'] = 词数据['pinyin']
            信息['缩写'] = 词数据['abbreviation']
            return 信息


def 包含(部分):
    if 成语数据 == None:
        初始化()

    所有成语 = []
    for 成语 in 成语数据:
        if (成语['word'].__contains__(部分)):
            所有成语.append(成语['word'])
    return 所有成语


def 末尾为字(字):
    if 成语数据 == None:
        初始化()

    所有成语 = []
    for 成语 in 成语数据:
        if (成语['word'][-1] == 字):
            所有成语.append(成语['word'])
    return 所有成语


def 末尾为音(音):
    if 成语数据 == None:
        初始化()

    同音字 = 字典.音为(音)
    所有成语 = []
    for 成语 in 成语数据:
        if (同音字.__contains__(成语['word'][-1])):
            所有成语.append(成语['word'])
    return 所有成语

# print(查成语('一石二鸟'))
# print(包含('精神'))
# print(末尾为字('十'))
# print(末尾为音('shí'))