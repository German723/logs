# Oracle11g参数的简单查看

1. 查看processes和sessions

```sql
SQL>show parameter processes
SQL>show parameter sessions
SQL>alter system set processes=300 scope=spfile;
SQL>ALTER SYSTEM SET sessions=335 scope=spfile;
--重启服务生效
--sessions=(1.1*processes+5)
```

