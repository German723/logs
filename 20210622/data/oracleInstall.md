
## 添加用户组和用户
```shell
groupadd dba
groupadd oinstall
useradd -g oinstall -G dba -m -d /opt/oracle oracle
passwd oracle
```

## 配置Oracle安装环境
```shell
vim /etc/sysctl.conf
fs.aio-max-nr = 1048576
fs.file-max = 6815744
kernel.shmall = 2097152
# 默认设置为物理内存的一半,单位为byte
kernel.shmmax = 536870912
kernel.shmmni = 4096
kernel.sem = 250 32000 100 128
net.ipv4.ip_local_port_range = 9000 65500
net.core.rmem_default = 4194304
net.core.rmem_max = 4194304
net.core.wmem_default = 262144
net.core.wmem_max = 1048586
```

```shell
vim /etc/security/limits.conf
oracle soft nproc 2047
oracle hard nproc 16384
oracle soft nofile 1024
oracle hard nofile 65536
```

```shell
vim /etc/pam.d/login
session required /lib/security/pam_limits.so
session required pam_limits.so
```

## 配置oracle用户环境变量
```shell
vim /etc/profile
if [ $USER = "oracle" ]; then
if [ $SHELL = "/bin/ksh" ]; then
ulimit -p 16384
ulimit -n 65536vi 
else
ulimit -u 16384 -n 65536
fi 
fi 
```

```shell
su - oracle
# cd /opt/oracle
vim .profile
ORACLE_BASE=/opt/oracle
ORACLE_HOME=$ORACLE_BASE/product/11.1.0
ORACLE_SID=orcl
PATH=$ORACLE_HOME/bin:$PATH
export ORACLE_BASE ORACLE_HOME ORACLE_SID PATH
```

## 上传文件并更改文件所有者

```shell
unzip 
unzip
mv database/ /opt/oracle
chown -R oracle:oinstall /opt/oracle/database
```

## 安装Oracle数据库