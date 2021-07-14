# Linux command alternatives

## find-->fd

find的局限性-->搜索结果的默认条目不合理
`fd` features:
1. 目录的并行遍历-->一次搜索多个目录
2. 正则表达式(regex)
3. 通配符

### how to install fd

```shell
# redhat series(redhat\centos\Fedora)
sudo dnf install fd-find
# macos-->MacPorts、HomeBrew
