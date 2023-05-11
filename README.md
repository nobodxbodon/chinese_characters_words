# 字

字典数据取自 [此库](https://github.com/pwxcoo/chinese-xinhua)。

## 接口

### 查单字()

参数为单字字符串，如：`查单字('好')`。如果查不到，返回 None；否则信息如下：
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
