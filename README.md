# 字

字典数据是 [此库](https://github.com/pwxcoo/chinese-xinhua) 中的 `data/word.json`，成语数据是 `idiom.json`。

字形数据来自 [这里](http://git.chise.org/gitweb/?p=chise/ids.git;a=blob_plain;f=IDS-UCS-Basic.txt;hb=HEAD)。

## 接口

### 查成语

```
from chinese_characters_words import 词典
词典.查成语('一石二鸟')
```

如果查不到，返回 None；否则信息如下：
```
{
  '词'
  '释义'
  '例句'
  '渊源'
  '拼音'
  '缩写'
}
```
如：
```
{'词': '一石二鸟', '释义': '扔一颗石子打到两只鸟。比喻做一件事情得到两样好处。', '例句': '无', '渊源': '无', '拼音': 'yī shí èr niǎo', '缩写': 'ysen'}
```

### 找包含某字的成语

```
> print(包含('精神'))

['抖搂精神', '抖擞精神', '精神百倍', '精神抖擞', '精神焕发', '精神恍惚', '精神满腹', '龙马精神', '人逢喜事精神爽', '桃李精神', '颐养精神']
```

### 查单字

```
from chinese_characters_words import 字典
字典.查单字('好')
```

如果查不到，返回 None；否则信息如下：
```
{
  '字'
  '旧体'
  '笔画数'
  '拼音'
  '部首'
  '释义'
  '其他'
}
```

### 找包含某部分的字

```
> print(包含('吴'))

['俣', '娱', '悮', '洖', '祦', '筽', '脵', '茣', '虞', '蜈', '誤', '误', '鋘', '麌']

> print(左边('甘'))

['甛', '邯']

> print(上面('口'))

['兄', '另', '叧', '只', '号', '叾', '吊', '吕', '吴', '呆', '呈', '员', '呙', '咠', '品', '員', '啚', '肙', '虽', '足', '黾']

> print(下面('天'))

['关', '吴', '昊', '癸', '龑']
```
## 参与开发

依赖的第三方 Python 包：

- [rply-ulang](https://pypi.org/project/rply-ulang/)
