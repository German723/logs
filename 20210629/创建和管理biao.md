# 5 创建和管理表

## 5.1 表和表列

### 5.1.1 表和实体

E-R图

### 5.1.2 表的分类

### 5.1.3 表和列的命名规则

### 5.1.4 列数据类型

## 5.2 创建表

### 5.2.1 设计器建表

### 5.2.2 创建标准表

```sql
CREATE TABLE scoot.books (
    ID INTEGER PRIMARY KEY COMMENT "图书编号",
    Name VARCHAR2(50) COMMENT "图书名称",
    Author VARCHAR(50) COMMENT "图书作者",
    ISBN VARCHAR(20) UNIQUE COMMENT "图书ISBN编号",
    Publisher VARCHAR(50) COMMENT "图书出版社",
    PublishDate DATE COMMENT "出版日期",
    Qty INTEGER COMMENT "库存数量",
)SEGMENT CREATION DEFERRED
PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 NOCOMPRESS NOLOGING
TABLESPACE "EXAMPLE"
```

```sql
CREATE TABLE scoot.invoice (
    invoice_id NUMBER NOT NULL UNIQUE COMMENT "发票编号",
    vendor_id NUMBER NOT NULL COMMENT "发票编号",
    invoice_number VARCHAR2(50) NOT NULL COMMENT "发票编号",
    invoice_date DATE DEFAULT SYSDATE COMMENT "发票编号",
    inovice_total NUMBER(9,2) NOT NULL COMMENT "发票编号",
    payment_total NUMBER(9,2) DEFAULT 0 COMMENT "发票编号",
)
```

### 创建临时表

```sql
--创建临时表
CREATE GLOBAL TEMPORARY TABEL scoot.books (
    col_name data_type constraint,
    ...
){ON COMMIT DELETE ROWS |           --事务级临时表
  ON COMMIT PRESERVE ROWS};          --会话级临时表
```
事务级临时表 --> 事务结束(提交或回滚事务)时，Oracle自动清除临时表中数据
会话级临时表 --> 会话结束时，Oracle自动清除临时表中的数据
1. 事务级临时表代码示例
```sql
CREATE GLOBAL TEMPORARY TABLE scoot.book_temp_transaction (
    ID NUMBER(9) PRIMARY KEY COMMENT "图书ID",
    bookname VARCHAR2(50) COMMENT "图书名称",
    publisher VARCHAR2(50) COMMENT "图书出版社",
)
ON COMMIT DELETE ROWS; --事务级临时表

--
INSERT INTO book_temp_transaction VALUES (1,'Oracle学习指南','计算机出版社');
--格式化输出
COL bookname format a20;
COL publisher format a20;
--查看插入数据
SELECT * FROM book_temp_transaction;
--提交
COMMIT;
--提交后再次查看
SELECT * FROM book_temp_transaction; --事务级临时表中的数据被清除了
```

2. 会话级临时表示例

```sql
--创建会话级临时表
CREATE GLOBAL TEMPORARY TABLE book_temp_session(
    ID NUMBER(9) PRIMARY KEY COMMENT "图书ID",
    bookname VARCHAR2(50) COMMENT "图书名称",
    publisher VARCHAR2(50) COMMENT "图书出版社",
)
ON COMMIT PRESERVE ROWS;
--插入数据
INSERT INTO book_temp_session VALUES(1,'Oracle学习指南','计算机出版社')
--COMMIT;
COMMIT;
--格式化输出
COL bookname format a20;
COL publisher format a20;
--会话级临时表提交后数据仍在
SELECT * FROM book_temp_session;
--DISCONNECT
DISCONNECT;
--reconnect
CONN scoot/scotttiger
--断开重新连接后会话级临时表中数据被清空了
SELECT * FROM book_temp_session;
```

### 5.2.7 数据字典中的表信息

表作为一种方案对象，一经创建，其建表信息就保存到数据字典中。
`建表信息`：
表的创建者，创建时间，表空间等
`数据字典`：
存储数据库的元数据
`数据字典视图`

查询某个表的信息
```sql
SELECT tablespace_name 表空间名,
       table_name       表名,
       num_rows         行数,
FROM DBA_TABLES
WHERE OWNER='SCOOT';    --对象名称必须大写
```

DBA_TAB_COLUMNS --> 查询表里面特定列信息
```sql
SELECT column_name 列名,
        data_type 数据类型,
        nullable 是否为空,
FROM DBA_TAB_COLUMNS
WHERE OWNER='SCOOT' AND table_name='EMP';

`数据字典分类`:
DBA_XXX
USER_XXX
ALL_XXX