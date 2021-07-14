# <center>spfile</center>

## 1. spfile简介

<p style="text-indent:2em">
<mark>spfile</mark>(server parameter file--服务器参数文件--)，可以通过<mark>create spfile</mark>语句或者<mark>DBCA</mark>工具创建。spfile也是<mark>二进制文件</mark>。虽然可以用文本编辑器打开，但打开后查看到的基本是乱码，也无法编辑。如果强行使用文本编辑器编辑二进制文件，则二进制文件将损坏。<strong>二进制文件需要通过接口查看和修改。</strong></p>

## 2. spfile的作用

<p style="text-indent:2em">数据库启动时，需要读取参数文件来分配内存区域并定位控制文件的位置。启动数据库时(`startup open`)，如果不指定<mark>spfile</mark>，Oracle实例会在操作系统中特定缺省位置搜索,即`spfile`有一个默认存放位置。有以下两种搜索结果：</p>

1. 在默认位置找到了`spfile`，Oracle实例读取文件内容，并根据文件内容分配内存并进行其他配置；

2. 在默认位置没找到`spfile`，启动失败。

<p style="text-indent:2em">也可以通过下列代码指定<mark>spfile</mark>的位置:</p>

```startup pfile='/home/oracle/app/oracle/product/11.2.0/dbhome_2/dbs/spfilehelowin.ora'```

## 3. spfile存放位置

<p style="text-indent:2em">通过以下命令查询<mark style="color=green">spfile</mark>存放位置:</p>

`show parameter spfile` or `show parameter pfile`

## 4. spfile全称

<p style="text-indent:2em">
如果实例名称是<strong>orcl</strong>，则<strong>spfileorcl.ora</strong>；如果实例名称是<strong>helowin</strong>，则<strong>spfilehelowin.ora</strong>。
</p>
