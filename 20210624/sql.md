# title

## 添加字段注释

```sql
create table test.demo(
    id,int,primary key,auto_increment,comment '物理主键',
    name,varchar(24),not null,comment '姓名',
    age,int,comment '年龄',
    gender,enum('男','女','保密'),default '保密'
)comment='这是添加字段注释的demo'
```

##