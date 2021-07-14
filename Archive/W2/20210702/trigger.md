# trigger

trigger --命名块-- 具有`名称、声明、执行和异常处理区`，存储在数据字典中。  

## 15.1 触发器的作用

自动调用机制  
业务逻辑  

```sql
CREATE OR REPLACE TRIGGER trigger_name
-- 自动调用机制
{after|before} {INSERT|UPDATE|DELETE}
ON table_name
FOR EACH ROW
-- trigger body
-- 业务逻辑
BEGIN

END;
```
<center>代码15.1 触发器定义示例</center>
业务需求:  

更新员工薪资时，1. 调整的薪资大于当前薪资才更新  2. 用户原始调薪信息写入emp_history;

```sql
CREATE OR REPLACE TRIGGER v_verifySalary
BEFORE UPDATE 
ON emp
FOR EACH ROW
WHERE(NEW.sal>old.sal)
--PL/SQL Code Block
Declare 
v_sal NUMBER;
BEGIN
    IF UPDATING('sal') THEN
        v_sal := :NEW.sal -:OLD.sal;
        DELETE FROM emp_history
            WHERE empno = :OLD.empno;
        INSERT INTO emp_history VALUES(
            :OLD.empno, :OLD.ename, :OLD.job, :OLD.mgr, :OLD.hiredate, :OLD.sql, :OLD.comm, :OLD.deptno
        )
        UPDATE emp_history SET sal = v_sal
            WHERE empno = :NEW.empno;
    END IF;
END;
```

