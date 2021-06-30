
## 复制旧表到新表

### 新表不存在
1. 将旧表中的数据复制到新表 --> 但字段属性(`primary key/auto_increment/extra等`)没有被复制
```sql
create table new_table as select * from old_table;
```
2. 复制表结构到新表 --> 不复制数据
```sql
# 给一个`false条件`
create table new_table
as select * from old_table where 1=2;
# 使用like
create table new_table like old_table;
```

### 新表已存在

复制旧表数据到新表
+ 表结构相同
```sql
insert into new_table
select * from old_table;
```
+ 表结构不同
```sql
insert into new_table(filed1,filed2...)
select field1,field2... from old_table;
```
2. 复制全部数据
```sql
select * into new_table from old_table;
```
3. 只复制表结构到新表
```sql
# 给一个false条件
select * into new_table from old_table where 1=2;
```

`Note`:
>1：只会复制表数据和表结构，不会有任何约束。
2：当 where 条件不成立时，只复制表结构，没有任务数据。