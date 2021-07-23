## Kernel

3.10.0-1160.24.1.el7.x86_64
主版本.次版本.release版本-修改版本.处理器架构

主版本、次版本架构不变的情况下，新增的功能累积到一定程度后释放的版本 -- **release**.

Linux内核使用的是GPL的授权，因此大家都可以修改内核程序代码的修改。因此，如果针对某个版本的内核修改过部分的程序代码，那么这个被修改过的内核版本就是**修改版本**
dev version

主要用来测试与开发新功能，一般是内核工程师使用。

stable version

内核功能开发成熟后发行的版本，一般是家庭或企业使用。

内核是一组程序，如果这组程序每次加入新功能都得重新编译与改版的话就太麻烦了。可以通过**模块化**，不变动原来的内核程序，直接将新加入的功能设置为**驱动程序**。

## distributions

Linux+software+Tools = distributions

开发Linux distributions的团队和公司实在太多了，为了让所有的Linux distributions开发不至于差异太大，制定了标准：

1. Linux Standard Base(LSB)
2. File system Hierarchy Standard(FHS)文件系统层次标准



