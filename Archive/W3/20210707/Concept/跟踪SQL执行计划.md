`SET AUTOTRACE TRACEONLY EXPLAIN STATISTICS`
使用上述命令<mark style="background-color:orange">跟踪SQL执行计划</mark>

# Example

(1) 代码示例  

```sql
--创建位图索引
SQL> CREATE BITMAP INDEX idx_bit_objtype 
ON tbl_idx_objects(object_type);
Index created.
--位图索引信息查询
scott@ORCL> SELECT index_name,index_type,num_rows FROM user_indexes WHERE index_name='IDX_BIT_OBJTYPE';
INDEX_NAME              INDEX_TYPE              NUM_ROWS
--------------------------------------------------------------------------
IDX_BIT_OBJTYPE         BITMAP                  42
--跟踪SQL执行计划
scott@ORCL> SET AUTOTRACE TRACEONLY EXPLIAN;
scott@ORCL> SELECT object_name FROM tbl_idx_objects WHERE object_type='TABLE' AND ROWNUM<=10;
Execution plan
-----------------------------------------------------------------------------------------
Plan hash value:676352033
-----------------------------------------------------------------------------------------------
| ID | Operation                    |Name             | Rows | Bytes | Cost(%CPU) | Time     |
| 0  | SELECT STATEMENT             |                 | 10   | 28    | 1(0)       | 00:00:01 |
| *1 | COUNT STOPKEY                |                 |      |       |            |          |
| 2  | TABLE ACCESS BY INDEX ROWID  | TBL_IDX_OBJECTS | 3526 | 98728 | 1(0)       | 00:00:01 |
| 3  | BITMAP CONVERSION TO ROWIDS  |                 |      |       |            |          |
| *4 | BITMAP INDEX SINGLE VALUE    | IDX_BIT_OBJTYPE |      |       |            |          |
--------------------------------------------------------------------------------------------------
Predicate information
----------------------------------------------------------------------------------------------
1 - fliter(ROWNUM<=10)
4 - access ("OBJECT_TYPE"="TABLE")
Note
-----------------------------------------------------------------------------------
  - dynamic sampling used for this statement(level=2)
```

(2) 示例代码的一些关键词注释
`Operation`
`Predicate information`查询谓词
`Note`注释注意
`dynamic sampling used for this statement`这次SQL计划使用了<mark style="backgrond-color:orange">动态抽样(dynamic sampling)</mark>