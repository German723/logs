<!-- vscode-markdown-toc -->
* 1. [展示更多行](#)
* 2. [展示更多列-->默认值20](#-1)
* 3. [改变列宽-->默认值50](#-1)
* 4. [设置float列的精度](#float)
* 5. [数字格式化显示](#-1)
	* 5.1. [用逗号格式化大值数字](#-1)
	* 5.2. [设置数字精度](#-1)
	* 5.3. [百分号格式化](#-1)
* 6. [更改绘图方法](#-1)
* 7. [配置info()](#info)
* 8. [打印出当前设置并重置上面的设置](#-1)

<!-- vscode-markdown-toc-config
	numbering=true
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->
# pandas中优化表格展示



## <a name=''></a>展示更多行

同一页展示更多行-->下面两行代码等同</br>
```python
pd.set_option('display.max_rows', 200)
pd.options.display.max_rows = 200
```
同一页展示行-->下面两行代码等同-->默认最小值为5
```python
pd.set_option('display.min_rows', 10)
pd.options.display.min_rows = 10
```
还可以直接重置
```python
pd.reset_option('display.max_rows')
```

## <a name='-1'></a>展示更多列-->默认值20
```python
pd.get_option('display.max_columns')
pd.options.display.max_columns = 20
```
## <a name='-1'></a>改变列宽-->默认值50
```python
pd.set_option('display.max_colwidth', 500)
pd.options.display.max_colwidth = 500
```
## <a name='float'></a>设置float列的精度
float类型的数据默认显示小数点后6位
这个设置不影响底层数据,只是影响展示。
```python
pd.set_option('display.precision', 2)
pd.options.display.precision = 2
```
## <a name='-1'></a>数字格式化显示
### <a name='-1'></a>用逗号格式化大值数字
pd.set_option('display.float_format', '{:,}'.format)
### <a name='-1'></a>设置数字精度
pd.set_option('display.float_format', '{:2f}'.foramt)
### <a name='-1'></a>百分号格式化
pd.set_option('display.float_format', '{:2f}%'.format)

## <a name='-1'></a>更改绘图方法
默认情况下,pandas使用matplotlib作为绘图后端,但从0.25开始可以使用plotly、bokeh等第三方库。
```python
import numpy as np
import pandas as pd
pd.set_option('plotting.backend', 'ploty')
data = pd.Series(np.random.randn(100).cumsum())
data.plot()
```

## <a name='info'></a>配置info()
`pandas`中我们经常使用`info()`来查看`DataFrame`的数据情况。但info()这个方法对要分析的最大列数,并且如果数据集中有null，那么在大数据集计数统计时会非常慢。</br>

pandas提供了两种选择：
>display.max_info_columns: 设置要分析的最大列数，默认为100。</br>display.max_info_rows: 设置计数null时的阈值，默认为1690785。</br>

比如，在分析有 150 个特征的数据集时，我们可以设置`display.max_info_columns`为涵盖所有列的值，比如将其设置为 200：</br>

```python
pd.set_option('display.max_info_columns', 200)
```
在分析大型数据集时，`df.info()`由于要计算所有null，导致速度很慢。因此我们可以简单地设置`display.max_info_rows`为一个小的值来避免计数，例如只在行数不超过5时才计数null：</br>

```python
pd.set_option('display.max_info_rows', 5)
```
## <a name='-1'></a>打印出当前设置并重置上面的设置

```python
pd.describe_option()
pd.reset_option('all')
```
