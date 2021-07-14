# NEW OLD

只有使用了关键字`FOR EACH ROW`时，`new old`这两个关键字才存在。  
`new` --> 引用最新的列值
`old` --> 引用以前的列值

insert into 时，只能`:new`，  
update 时，`new`和`old`都可以，  
delete时，只能`old`。