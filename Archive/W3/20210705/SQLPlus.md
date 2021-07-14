# SQL/Plus的基本功能

<p style="text-indent:2em">这篇文章介绍了如何启动SQL/Plus，如何使用CONNECT命令连接数据库以及SQL/Plus的运行环境参数。</p>

## 1. 启动SQL/Plus

<p style="text-indent:2em">对于Linux和Unix平台，启动SQL/Plus之前，需要设置环境变量<mark>ORACLE_SID、ORACLE_HOME和LD_LIBBARY_PATH</mark>。而Windows平台一般无需设置。</p>

```shell
# 启动sqlplus
# 方式一
[oracle@localhost ~]$ sqlplus 
请输入用户名：
请输入密码：
# 方式二
[oracle@localhost ~]$ sqlplus /nolog
SQL>
# 方式三
[oracle@localhost ~]$ sqlplus username/password
[oracle@localhost ~]$ sqlplus username
[oracle@localhost ~]$ sqlplus username@connect_identifider
[oracle@localhost ~]$ sqlplus username/password@connect_identifieder
```
`connect_identifider`
>Note:connect_identifider --> $ORACLE_HOME/NETWORK/ADMIN/tnsnames.ora

## 重新连接数据库

<mark>当命令提示行窗口出现了<strong>SQL></strong>提示符后，表示已经连接到一个Oracle数据库实例。</mark>

不用退出即可完成切换用户身份和切换数据库

```sql
--演示切换用户身份
SQL>conn scott/tigers
connected
SQL>show user
USER is "SCOTT'
SQL>conn sys/password as sysdba
conected
SQL>show user
USER is "sys"
--切换数据库
SQL>conn scott/password@helowin
connected
```