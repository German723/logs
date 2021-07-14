# 1. User space and Kernel space

操作系统中，内存通常被分为`User space`和`Kernel space`。进程/线程运行在`User space`时就处于用户态(user mode)，运行在`Kernel space`时就处于内核态(kernel mode)。

+ 运行在`Kernel mode`的程序可以访问任何计算机资源 --> 既可以访问`User space`也可以访问`Kernel space`。不受限制，为所欲为。
+ 运行在`User mode`的程序只能访问`User space`

为什么要区分`User space`和`Kernel space`?

假如应用程序可以访问任何内存空间的话，如果应用程序崩溃的话，可能会影响操作系统的正常运转。

# 2. 操作系统线程

(1) 用户空间实现线程 --> 早期系统

早期系统中，所有线程都在用户空间实现，操作系统只能看到进程无法看到线程。这样一来，开发者需要手动定义线程(数据结构、创建、销毁、调度和维护等)

优点

缺点


(2) 内核空间实现线程 --> 现代系统(Linux、Windows、MACOS、Solaris)

运行在内核空间，只能由内核完成线程的调度。  

每个内核线程可以视为内核的一个分身，这样操作系统就有能力同时处理多件事情 `Multi-Threads Kernel`

操作系统内置线程(内核完成线程的创建、销毁、调度和维护)，开发者只需要`系统调用`