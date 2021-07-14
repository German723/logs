# 认识pip

`pip`(package installer for python)可以对python得第三方库进行<mark>安装、更新和卸载</mark>等操作。python的所有工具库都存放在名为`PyPi`(Python Package Index)的仓库中。简而言之，`PyPi`是一个仓库，`pip`是仓库管理员。

# 安装pip

从python3.4开始，pip已经内置在python中。如果你的python版本中没有pip，那么可以通过以下两种方法安装：</br>
(1) `easy_install pip`</br>
(2) [pip download](https://pypi.org/project/pip/#files) --> python scripts directory --> `python setup.py install`</br>

# 查看pip版本

`pip --version`

# 升级pip

`pip install --upgrade pip`

# 获取帮助

`pip help`

# 安装第三方库

## 1. 基本安装方式

`pip install package_name`

`pip install package_name==1.1.2`

## 2. 批量安装库

(1) 将需要安装的库名称及版本写入文件`requirements.txt`
```
vim requirements.txt
pickleshare==0.7.5
Pillow==8.2.0
prometheus-client==0.10.0
promopt-tookit==3.0.18
```
(2) 使用下面命令批量安装库</br>
`pip install -r ./requirements.txt`

## 3. 使用wheel文件安装

这种方法适合离线安装，wheel文件是库的源文件，可以下载后放到本地安装。

步骤如下：</br>

(1) [Download link](https://www.lfd.uci.edu/~gohlke/pythonlibs/)</br>
(2) 切换到`*.whl`所在文件夹内，运行命令: `pip install *.whl`。

# 卸载库

`pip uninstall package_name`

# 升级库

`pip install --upgrade package_name`

# 查看库信息

`pip show -f package_name`

# 查看已安装的库

`pip list`

# 将已安装的库信息保存到特定文件内

`pip freeze > requirements.txt`

# 查看已安装的库中哪些可以升级

`pip list -o`

# 查看兼容性问题

`pip check package_name`

# 将库文件下载到本地

`pip download package_name -d directory_path`

# 更换pip下载源

(1) 临时更换</br>
`pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package matplotlib`</br>
(2) 设为默认</br>
`pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple`

# 国内主流镜像源

[清华](https://pypi.tuna.tsinghua.edu.cn/simple)</br>
[阿里云](http://mirrors.aliyun.com/pypi/simple/)</br>
[中国科技大学](https://pypi.mirrors.ustc.edu.cn/simple/)</br>
[华中理工大学](http://pypi.hustunique.com/)</br>
[山东理工大学](http://pypi.sdutlinux.org/)</br>
[豆瓣](http://pypi.douban.com/simple/)</br>

