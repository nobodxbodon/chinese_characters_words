from rply import 分词器母机, 语法分析器母机
import 字典

分词母机 = 分词器母机()
分词母机.添了('上面', '上面')
分词母机.添了('下面', '下面')
分词母机.添了('逗号', '，')
分词母机.添了('部分', r'[\u4e00-\u9fa5]')

分析器母机 = 语法分析器母机(['上面', '下面', '逗号', '部分'])

@分析器母机.语法规则("字描述 : 字部分描述")
@分析器母机.语法规则("字描述 : 字描述 逗号 字部分描述")
def 字描述(片段):
    if len(片段) == 1:
        return 片段[0]
    else:
        原范围 = 片段[0]
        另外条件 = 片段[2]
        return list(set(原范围).intersection(set(另外条件)))

    
@分析器母机.语法规则("字部分描述 : 上面 部分")
@分析器母机.语法规则("字部分描述 : 下面 部分")
def 字部分描述(片段):
    if 片段[0].getstr() == '上面':
      return 字典.上面(片段[1].getstr())
    elif 片段[0].getstr() == '下面':
      return 字典.下面(片段[1].getstr())

分词器 = 分词母机.产出()
分析器 = 分析器母机.产出()

print(分析器.按语法分词(分词器.分词('上面口')))
print(分析器.按语法分词(分词器.分词('下面天')))
print(分析器.按语法分词(分词器.分词('上面口，下面天')))