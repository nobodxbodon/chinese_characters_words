from rply import 分词器母机, 语法分析器母机

分词母机 = 分词器母机()
分词母机.添了('左右', '⿰')
分词母机.添了('上下', '⿱')
分词母机.添了('全包围', '⿴')
分词母机.添了('左右上包围', '⿵')
分词母机.添了('左右下包围', '⿶')
分词母机.添了('左上下包围', '⿷')
分词母机.添了('左上包围', '⿸')
分词母机.添了('左下包围', '⿺')
分词母机.添了('右上包围', '⿹')
分词母机.添了('交叉', '⿻')
分词母机.添了('上中下', '⿳')
分词母机.添了('左中右', '⿲')
分词母机.添了('编码', '&\w+-\w+[\+\-]?\w+;')
分词母机.添了('部分', '.') # r'[\u4e00-\u9fa5刃䒑𠆢𰀁⺄𰀢𫩏]') # 添加 U+2F81E

分析器母机 = 语法分析器母机(['左右', '上下', '全包围', '左右上包围', '左右下包围', '左上下包围', '左上包围', '左下包围', '右上包围', '交叉', '上中下', '左中右', '部分', '编码'])

@分析器母机.语法规则("结构数据 : 两种部分")
@分析器母机.语法规则("结构数据 : 两元结构 结构数据 结构数据")
@分析器母机.语法规则("结构数据 : 三元结构 结构数据 结构数据 结构数据")
def 结构数据(片段):
    if len(片段) == 1:
        return 片段[0]
    elif len(片段) == 3:
        return {'字型': 片段[0], '部分': [片段[1], 片段[2]]}
    elif len(片段) == 4:
        return {'字型': 片段[0], '部分': [片段[1], 片段[2], 片段[3]]}

@分析器母机.语法规则("两元结构 : 左右 | 上下 | 全包围 | 左右上包围 | 左右下包围 | 左上下包围 | 左上包围 | 左下包围 | 右上包围 | 交叉")
def 两元结构(片段):
    return 片段[0].getstr()

@分析器母机.语法规则("三元结构 : 上中下 | 左中右")
def 三元结构(片段):
    return 片段[0].getstr()

@分析器母机.语法规则("两种部分 : 部分 | 编码")
def 两种部分(片段):
    return 片段[0].getstr()

分词器 = 分词母机.产出()
分析器 = 分析器母机.产出()

def 结构数据解析(源数据):
    return 分析器.按语法分词(分词器.分词(源数据))


#print(结构数据解析('⿹&CDP-8964;山'))
#print(结构数据解析('⿵冂&CDP-8CC7;'))
#print(结构数据解析('⿳廿&CDP-8D76;女'))
#print(结构数据解析('⿱&U-i001+81E4;土'))
#print(结构数据解析('⿱&CDP-v002-8D7C;大'))

# 嵌套
#print(结构数据解析('⿱⿰&CDP-895C;&CDP-895C;一'))
#print(结构数据解析('⿱⿳亠口冖几'))
#print(结构数据解析('⿱&CDP-8A65;&CDP-8CC6;'))
#print(结构数据解析('⿱一⿰⿵冂丶⿵冂丶'))

# 下面第一字符超出unicode编码范围 \u4e00-\u9fa5
#print(结构数据解析('⿱刃一'))
#print(结构数据解析('⿱䒑业'))
#print(结构数据解析('⿱𠆢丨'))
#print(结构数据解析('⿹⺄𰀁'))

# 待做

