<h1 style="text-align:center">Osquery</h1>

Linux提供了很多帮助用户收集**主机操作系统信息**的命令：列出文件或者目录的属性信息；查询安装的软件包、正在执行的命令、开机时启动的服务；或者了解系统硬件。

每个命令使用自己的输出格式列出系统信息。你需要使用**grep**、**sed**、**awk**这样的工具过滤命令输出，以便找到特定的信息。此外，很多这样的信息会频繁变动，导致系统状态的改变。

如果将所有的信息格式化为一个数据库的SQL查询的输出进行查看将十分有益。想象一下，你能够查询具有类似名称的SQL数据库表一样进行查看**ps**和**rpm**命令的输出。幸运的是，**Osquery**刚好实现了这个功能。它是一个开源的**由SQL驱动的操作系统仪表、监控和分析框架**。


## 安装Osquery

Osquery适用于Linux、macOS、Windows、FreeBSD。可以参照[官方指南](https://osquery.io/)进行安装。安装完成之后，确保Osquery可以工作:

```
$ rpm -qa | grep osquery
osquery-4.7.0-1.linux.x86_64
$ osqueryi --version
osqueryi version 4.7.0
```

## Osquery组件

Osquery有两个主要组件：

+ `osqueryi`是一个交互式的SQL查询控制台，可以独立运行，一般不需要root权限。

+ `osqueryd`像一个安装在主机的监控守护进程，可以定期调度查询操作执行，从底层架构收集信息。通过`osqueryctl`控制`osqueryd`的启动、停止和检查其状态。

```
$ rpm -ql osquery-4.8.0-1.linux.x86_64 | grep bin
/usr/bin/osqueryctl
/usr/bin/osqueryd
/usr/bin/osqueryi
$
```

## 使用osqueryi交互式命令提示符

用户和Osquery的交互与使用SQL数据库十分相似。事实上，`osqueryi`是SQLite shell的一个修改版。执行`osqueryi`命令进入交互式命令提示符，就可以执行Osquery命令，通常以`.`开始：

```
$ osqueryi
Using a virtual database.Need help,type '.help'
osquery>
```

要退出交互式命令提示符，执行`.quit`命令回到操作系统的命令提示符：

```
osquery>
osquery>.quit
$
```

## 找出可用的表

如前所述，Osquery像SQL查询一样输出数据，数据库中的信息通常保存在表中。但是如何在不知道表名的情况下查询这些表呢？你可以运行`.tables`命令列出所有可以查询的表。如果你是一个Linux长期用户或者一个系统管理员，就会对表名十分熟悉，因为你一直在使用操作系统命令获取同样的信息：

```
osquery>.tables
  => acpi_tables
  => apparmor_events
  => apparmor_profiles
  => apt_sources
<<裁剪>>
  => arp_cache
  => user_ssh_keys
  => users
  => yara
  => yara_events
  => ycloud_instance_metadata
  => yum_sources
osquery>
```

## 检查各个表的模式

知道表名后，可以查看每个表提供的信息。`.schema tablename`查看表中保存的信息。以**ps**命令为例，可以通过**ps -ef**或**ps aux**验证osquery的执行结果。

```


