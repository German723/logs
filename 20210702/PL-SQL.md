# PL/SQL基础知识

SQL语法 + PL/SQL语法  
`procedure` `function` `trigger` `package`  

# 编写规范

## 注释
-- 单行注释  
/*
注释内容
*/ 多行注释  

## 标识符命令规范

1. 变量 --> v_作为前缀 --> v_sal
2. 常量 --> c_作为前缀 --> c_rate
3. 游标 --> _cursor作为后缀 --> emp_cursor
4. exception --> e_作为前缀 --> 

## PL/SQ块结构

```sql
DECLARE
/*
    声明部分 --> optional
1. 声明变量、常量
2. 声明游标
3. 声明exception
4. 复杂数据类型
*/
BEGIN
/*
    执行部分 --> necessary
1. PL/SQL代码
2. SQL代码
*/
EXCEPTION --> optional
/*
    exception处理
处理运行的各种错误
*/
END;
```