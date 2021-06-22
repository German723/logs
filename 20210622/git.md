# basic concept

## file state

1. modified
git可以感知工作目录中哪些文件被修改了，然后把已修改的文件加入到modified区域
2. staged
通过add命令将工作目录中修改的文件提交到暂存区,等待commit
3. commited
将暂存区文件commit至git目录永久保存

## commit node

git每次提交都会生成一个节点,而每个节点都会有一个哈希值作为唯一标识,多次提交会形成一个线性节点链(不考虑merge)

## head

head是指针(引用),指向当前工作目录

## remote repository

# branch

```git
# 创建分支
git branch branch_name
# 切换分支
git checkout branch_name
git checkout -b branch_name
# 删除分支
git branch -d branch_name
# 合并分支
git merge branch_name/hash
git rebase branch_name/hash
```

# common commands

## commit

```git
# 添加当前文件夹下面的所有文件到暂存区
git add .
# 添加某个文件到暂存区
gti add file_path
# 撤销工作区改动
git checkout --file_name
# 清空暂存区
git reset HEAD file_name
# 提交到本地库(生成节点)
git commit -m "describe this commit"
```

##

## remote 

```git
git clone repository_address
# 如果远程仓库更新了,而本地仓库没有同步,这时候需要使用git fetch
git fetch 远程仓库地址/分支名
# pull = fetch + merge(default)
git pull 远程分支名
git pull --rebase 远程分支名
# git push因为可能存在冲突,所以在push之前往往会先pull一下



```