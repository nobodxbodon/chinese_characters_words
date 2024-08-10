from rply import 分词器母机, 语法分析器母机
from chinese_characters_words import 字典

# 逐渐提取通用查询语言：https://www.zhihu.com/question/23719632/answer/3585430432
分词母机 = 分词器母机()
分词母机.添了('上面', '上面')
分词母机.添了('下面', '下面')
分词母机.添了('左边', '左边')
分词母机.添了('右边', '右边')
分词母机.添了('逗号', '[，,]')
分词母机.添了('的结构', '的结构')
分词母机.添了('部分', r'[\u4e00-\u9fa5]')

分析器母机 = 语法分析器母机(['上面', '下面', '左边', '右边', '逗号', '部分', '的结构'])

@分析器母机.语法规则("输入 : 字描述 | 查结构")
def 输入(片段):
    return 片段[0]

@分析器母机.语法规则("字描述 : 字部分描述")
@分析器母机.语法规则("字描述 : 字描述 逗号 字部分描述")
def 字描述(片段):
    字范围 = []
    if len(片段) == 1:
        字范围 = 片段[0]
    else:
        原范围 = 片段[0]
        另外条件 = 片段[2]
        字范围 = list(set(原范围).intersection(set(另外条件)))
    return "，".join(字范围)
    
@分析器母机.语法规则("字部分描述 : 上面 部分")
@分析器母机.语法规则("字部分描述 : 下面 部分")
@分析器母机.语法规则("字部分描述 : 左边 部分")
@分析器母机.语法规则("字部分描述 : 右边 部分")
def 字部分描述(片段):
    位置 = 片段[0].getstr()
    部分 = 片段[1].getstr()

    处理函数字典 = {
        '上面': 字典.上面,
        '下面': 字典.下面,
        '左边': 字典.左边,
        '右边': 字典.右边
    }

    处理函数 = 处理函数字典.get(位置, None)

    if 处理函数:
        return 处理函数(部分)

@分析器母机.语法规则("查结构 : 部分 的结构")
def 字的结构(片段):
    结构 = 字典.的结构(片段[0].getstr())
    字型 = 结构['字型']
    各部分 = 结构['部分']
    if (字型 == '⿱'):
        return f"上面{各部分[0]}，下面{各部分[1]}"
    elif (字型 == '⿰'):
        return f"左边{各部分[0]}，右边{各部分[1]}"
    else:
        return f"待完善：字型为{字型}，各部分：{各部分}"


分词器 = 分词母机.产出()
分析器 = 分析器母机.产出()
