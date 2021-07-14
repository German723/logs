# anaconda

1. 自带180多个包，包括conda、numpy、scipy和pandas等
2. 虚拟环境管理。可以创建**任意版本**的python虚拟环境

# 安装配置

1. [Download](https://www.anaconda.com/distribution/#download-section)
2. 环境变量
3. 镜像源

(1) 命令行输入以下命令：
```
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/ 
conda config --set show_channel_urls yes
```

(2) 编辑`~/.condarc`
```
channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
  - defaults
show_channel_urls: true
```

# 虚拟环境

## base环境(默认环境)

```
# Windows激活base环境
activate base
# macOS Linux激活base
conda activate base
```

## 查看已存在的虚拟环境

```
conda info --envs
```

## 创建虚拟环境

```
conda create --name venv_name python=version;
conda create --name demo python=2.7
demo activate
conda activate demo
```

## 删除虚拟环境

```
conda remove --name venv_name --all
```

