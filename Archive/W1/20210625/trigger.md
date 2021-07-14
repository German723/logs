# Oracle trigger 

## Instroduction

`trigger`是一种事件发生时隐式自动执行的`PL/SQL`。不能接受参数，不能被显示调用

## trigger type

### DML trigger
对数据表进行DML语句操作(insert、update、delete)时触发的触发器
    + 行级触发器 --> 对表中受影响的每一行触发一次`trigger`
    + 语句级触发器 --> 只触发一次
    + before trigger --> 事件发生之前执行代码
    + after trigger --> 事件发生之后执行代码

`语法`
```sql
create [or replace] trigger trigger_name
{before | after} trigger_event
on table_name
[for each row]
[when trigger_condition]
trigger_body
```

`语法解释`
>trigger_name:触发器名称</br>
before | after:</br>
trigger_event:</br>
table_name:发生触发器作用的对象</br>
for each row:指定创建行级触发器(没有该子句则为语句级触发器)</br>
when trigger_condition:添加触发条件</br>
trigger_body:触发体 --> 标准的PL/SQL语句</br>

### instead of trigger

`只能作用与视图触发器`

`语法`
```sql
create [or replace] trigger trigger_name
instead of trigger_event --事件名称
on view_name --视图名称
for each row  --替代触发器必须指定为行级触发器
[when trigger_condition] --触发条件
trigger_body --触发体，PL/SQL块
```

### 系统事件触发器

对数据库实例或者某个用户模式进行操作时定义的触发器:
1. 数据库系统触发器
2. 用户触发器


### Example of case

`DML`
```sql
create table STUDENT   ---创建student表
(
  id        NUMBER(19), --id
  stu_no    VARCHAR2(20), --学号
  stu_name  VARCHAR2(32), --姓名
  stu_age   NUMBER,  --年龄
  stu_major VARCHAR2(32) --专业
)
```

```sql
create table STU_LOG   ---创建stu_log表，用于记录对student表的操作日志
(
  log_id     NUMBER,  --日志id
  log_action VARCHAR2(100),  --操作名称
  log_date   DATE,  --操作时间
  log_message   VARCHAR2(32) --
)
```

a. 行级触发器（before触发器）

```sql
创建触发器：实现id的隐式自增
create or replace trigger modify_stu 
before insert on student
for each row
declare
next_id number;
begin
  select seq_test.nextval into next_id from dual;
  :new.id :=next_id;
end;
```

`insert into student(stu_no,stu_name,stu_age,stu_major) values('NO1','张三',20,'中文系'); `

b. 行级触发器（after触发器）

```sql
创建触发器：将对student表的操作都记录到stu_log表中（update of 用于指定一个或多个字段，指定字段被更新时才会触发触发器）
create or replace trigger modify_stu
after insert or delete or update of stu_name
on student
for each row
  begin 
    if inserting then
      insert into stu_log values(1,'insert',sysdate,:new.stu_name);
    elsif deleting then
       insert into stu_log values(2,'delete',sysdate,:old.stu_name);
    elsif updating then
      insert into stu_log values(3,'update_old',sysdate,:old.stu_name);
      insert into stu_log values(4,'update_new',sysdate,:new.stu_name);
     end if;
end;
```

```sql
insert into student values(1,'NO2','李四',21,'数学系');  --插入一条数据
delete student where stu_name='张三';   --删除一条数据
update student set stu_age=19 where stu_name='李四';  --修改李四的年龄
update student set stu_name='王二' where stu_name='李四';  --修改李四的名称
```

c、语句级触发器（before触发器）：用来控制对表的修改

```sql
create or replace trigger modify_stu
before insert or update or delete on student
begin
   if deleting then
     raise_application_error(-20001,'该表不允许删除数据');
   elsif updating then
     raise_application_error(-20002,'该表不允许修改数据');
    elsif inserting then
     raise_application_error(-20003,'该表不允许插入数据');
    end if;
end;
```

c、语句级触发器（after触发器）：用来控制对表的修改

