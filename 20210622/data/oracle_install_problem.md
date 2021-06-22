# problem 

## swap size is not enough

```shell
dd if=/dev/zero of=swapfile bs=1024 count=2000000
mkswap swapfile
# 临时挂载
swapon swapfile
swapoff swapfiles
# 永久挂载
vim /etc/fstab

```

## oracle 启动报错
LRM-00109: could not open parameter file '/opt/oracle/product/11.1.0/dbs/initorcl.ora'