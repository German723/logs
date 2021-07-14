# Oracle中的ROWID

<mark>根据每一行数据的物理地址信息编码而成的ROWID</mark>
ROWID用于定位数据库一条记录的的一个相对唯一地址值。

实际存储的物理地址信息通过`base64`编码转换为ROWID。一条记录插入到数据库表时，它的ROWID值就被唯一确定。
base64:0代表A 25代表Z 26代表a 51代表z 52代表0 61代表9 62代表+ 63代表/，刚好64个字符

## ROWID与B-Tree索引

B-Tree索引的每个条目具有两个字段。第一个字段是索引的键值，对于单列索引来说是一个值，对于多列索引来说则是多个值组合在一起。第二个字段是ROWID。
<mark>索引值-->ROWID-->ROWID转换成物理地址-->得到一行数据</mark>

## ROWID的格式

```
OOOOOOFFFBBBBBBRRR
OOOOOO-->Data object number
FFF-->Relative file number
BBBBBB-->Block number
RRR-->Row number
```

(1) Data object number --> data_object_id
object_id是Oracle为它的对象唯一分配的id
data_object_id是存放数据的“数据段对象id”
```sql
SELECT owner,object_id,data_object_id,status FROM dba_objects WHERE object_name='ACTOR';
OWNER       OBJECT_ID       DATA_OBJECT_ID      STATUS
---------------------------------------------------------------
ORCL        98413           98413               VALID
ALTER TABLE ACTOR MOVE TABLESPACE users; 
SELECT owner,object_id,data_object_id,status FROM dba_objects WHERE object_name='ACTOR';
OWNER       OBJECT_ID       DATA_OBJECT_ID      STATUS
---------------------------------------------------------------
ORCL        98413           98581               VALID
```
上面代码显示

(2) 相对文件编码 relative_fno
绝对文件编码file_id,相对于整个数据库唯一
相对文件编码relative_fno，相对于表空间唯一

```sql
SELECT file_name,file_id,relative_fno FROM dba_data_files;
FILE_NAME                                       FILE_ID             RELATIVE_FNO
-----------------------------------------------------------------------------------
C:\APP\ORACLE\ORADATA\ORCL\PDBORCL\SYSTEM01.DBF    7                    1
C:\APP\ORACLE\ORADATA\ORCL\PDBORCL\SYSAUX01.DBF    8                    4
...
```

## 通过ROWID访问数据的执行计划

```
SELECT t.*,''||t.ROWID FROM "ORCL"."ACTOR" t;
ACTOR_ID FIRST_NAME LAST_NAME LAST_UPDATE ''||ROWID
------------------------------------------------------
XX  XX  XX  XX AAAYEVAAJAAAACrAA
EXPLAIN PLAN FOR 
SELECT * FROM ACTOR WHERE ROWID='AAAYEVAAJAAAACrAA';
SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY)
--------------------------------------------------------
PALN_TABLE_OUTPUT
-------------------------
Plan hash value:2255410730
-----------------------------------------------------------------
|Id|Operation                 |Name       | Rows  |Bytes |Cost(%Cpu) |Time    |
|0 |SELECT STATEMENT          |           | 1     | 24   |1(0)       |00:00:01|
|1 |TABLE ACCESS BY USER ROWID| ACTOR     | 1     | 24   |1(0)       |00:00:01|

```

## 通过ROWID计算obj#,rfile#,block#,row#
(1) 查询dba_objects

SELECT t.*,''||t.ROWID FROM "ORCL"."ACTOR" t;
ACTOR_ID FIRST_NAME LAST_NAME LAST_UPDATE ''||ROWID
------------------------------------------------------
XX  XX  XX  XX AAAYEVAAJAAAACrAA
select owner,object_id,data_object_id,status from dba_objects where object_name='ACTOR';
OWNER       OBJECT_ID       DATA_OBJECT_ID          STATUS
------------------------------------------------------------------
ORCL        98413           98581                   VALID
```
(2) 手动转换
AAAYEVAAJAAAACrAA
A -- 0
Y -- 24
E -- 4
V -- 21
(1) data_object_id:AAAYEV(64进制)
AAAYEV=24*64*64+4*64+21=98581和查询字典表的值一致
(2) relative_fno:AAJ(64进制)
AAJ=9
(3) Block number
AAAACr=2*64+43=171
(4) Row number
AAA=0,即第一行
(3) 通过存储过程查询

```sql
SELECT

dbms_rowid.rowid_object (ROWID) data_object_id,

dbms_rowid.rowid_relative_fno (ROWID) relative_fno,

dbms_rowid.rowid_block_number (ROWID) block_no,

dbms_rowid.rowid_row_number (ROWID) row_no

FROM

ACTOR;
```

