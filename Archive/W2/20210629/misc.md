DUAL --> SYS
数据字典 --> SYSTEM
DUAL表所有用户都可以访问  
`表结构只有一列`
```sql
SQL>SELECT * FROM DUAL;
DUMAY
----------
X
```
`DUAL表是用来给用户查询信息的` --> 
1. 计算表达式的值
```sql
SQL>SELECT ((3*4)+5)/3 AS result FROM DUAL;
result
----------------
5.66666667
```

2. 系统内置函数
```sql
SQL>ALTER SESSION SET NLS_DATE_FORMAT='YYYY-MM-DD'
会话已更改。
SQL>SELECT SYSDATE FROM DUAL;
SYSDATE
-------------------
2021-06-29
```

`通过DUAL表可以实现很多计算和函数调用`  


# Oracle用户
1. system
2. sys

# 标准表的存储方式是堆存储

表上的索引是单独存储的一类数据库对象，它将特定字段的字段内容提取到一个单独存储位置。

# 建表类型

1. 标准表
2. 全局临时表
3. 索引组织表
4. 外部表
+ concept
Oracle只能处理Oracle服务器上的外部文件。通过Oracle的目录对象和ORACLE_LOADER加载外部文件。`以只读的方式`加载外部文件。  
实际上创建外部表只是在数据字典添加了外部表的元数据信息，并没有在数据库中创建数据文件。  
Oracle通过`访问驱动程序` --> `ORACLE_LOADER`或者`ORACLE_DATAPUMP`来读取外部表中的数据。
5. DUAL表
6. 数据字典中的表信息
