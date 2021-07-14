<h1 style="text-align:center">Oracle Database Reference</h1>

<h2 id="Chapter1"> Chapter1 Initialzation Parameters</h2>

This part describes the database initialization parameters that can be specified in a parameter file to start or configure an instance.This part contains the following chapter:
+ <a href="#Chapter1">Chapter1,"Initialization Parameter"</a>

This chapter contains detailed descriptions(in alphabetical order ) of the database initialization parameters.

This chapter contain the following topics:

+ <a href="#1.1">Uses of initialization parameters</a>
+ <a href="#1.2">Basic initialization parameters</a>
+ <a href="#1.3">Parameter Files</a>
+ <a href="#1.4">Changing Parameter Values in a Parameter File</a>
+ <a href="#1.5">Reading the Parameter Descriptions</a>
+ <a href="#1.6">Initialization Parameter Descriptions</a>

<h3 id="1.1">1.1 Uses of Initialization Parameters</h3>

Initialization parameters fall into various functional groups.For example,parameters perform the following functions:

+ Set limits for the entire database
+ Set user or process limits
+ Set limits on database resources 
+ Affect performance(these are called variable **parameters**)

Variable parameters are of particular interest to database adminstrators,because these parameters are used primarily to improve database performance.

Database adminstrators can use initialization parameters to:

+ Optimize performance by adjusting memory structures,such as the number of database buffers in memory.
+ Set database-wide defaults,such as the amount of space initially allocated for a context area when it is created.
+ Set database limits,such as the maximum number of database users
+ Specify names of files or directories required by the database

Many initialization can be fined-tune to improve database performance.Other parameters should never be altered or should be altered only under the supervision of Oracle Services.

All initialization parameters are optional.Oracle has a default value for each parameter.This value may be operating system-dependent,depending on the parameter.

#### 1.1.1 Types of Initialization Parameters

The Oracle database server has the following types of initialization parameters:

+ <a href="#1.1.2">Derived Parameters</a>
+ <a href="#1.1.3">Operating System-Dependent Parameters</a>
+ <a href="#1.1.4">Variable Parameters</a>

<h4 id="1.1.2"> 1.1.2 Derived Parameters</h4>

Some initialization parameters are **derived**,meaning that their values are calculated from the values of other parameters.Normally,you should not alter values for derived parameters,but if you do,then the value you specify will override the calculated value.

For example,the default value of the **SESSIONS** parameter is derived from the value of the **PROCESS** parameter.If the value of **PROCESS** changes,then the default value of **SESSION** changes as well,unless you override it with a specified value. 

<h4 id="1.1.3">1.1.3 Operating System-Dependent Parameters</h4>

The valid values or value ranges of some initialization parameters depend upon the host operating system.For example,the parameter **DB_BLOCK_BUFFERS** indicates the number of data buffers in main memory,and its maximum value depends on the operating system.The size of those buffers,set by **DB_BLOCK_SIZE**,has an operating system-dependent default value.

<h4 id="1.1.4"> 1.1.4 Variable Parameters</h4>

<h3 id="1.2"> 1.2 Basic Iniaialization Parameters</h3>

The following is a list of the database basic initialization parameters.Most databases should only need to have basic parameters set to run properly and efficently.Oracle adivses you to become familiar with the basic parameters and only use other parameters when directed to by feature documention or in special circumstances:

*CLUSTER_DATABASE*
*COMPATIBLE*
*CONTROL_FILES*
...

<h3 id="1.3">1.3 Parameter Files

A parameter file is a file that contains a list of initialization parameters and a value for each parameter.
You specify initialization parameters in a parameter file that reflect your particular installation.Oracle supports the following two types of parameter files:

+ Server Parameter Files
+ Initialization Parameter Files

<h4>Server Parameter Files</h4>

A server parameter file is <mark>a binary file</mark> that acts as a respository for installization parameters.The server parameter file can reside on the machine where the Oracle database server executes.Initialization parameters stored in a server parameter file are persistent,in that any changes made to the parameters while an instance is running can persistent across instance shutdown and startup.

<h4>Initialization Parameter Files</h4>

An initialization parameter file is <mark>a text file</mark> that contains a list of initialization parameters.The file should be written in the client's default character set.

The following are sample entries in an initialization parameter file:

```
PROCESSES=100
OPEN_LINKS=12
GLOBAL_NAMES=true
```

The name of the initialization parameter file varies depending on the operating system.For example,it can be in mixed case or lowercase,or it can have a logical name or a variation of the name init.ora.Also supplied is an initdw.ora file,which contains suggested parameter settings for data warehouse and data marts.The database administrators can choose a different filename for the initialization parameter file.

Refer to your operating system-specific Oracle documentation for the default locations and filenames for initialization parameter files on your operating system.The initialization parameter file is read by the client-side tool used to start the server(such as SQL*Plus).

Sample initialization parameter files are provided on the Oracle distribution medium for each operating system.A sample file is sufficent for initial use,but you will probably want to modify the file to tune the database for best performance.Any changes will take effect after you completely shutdown and restart the instance.

<h3 id="1.4">1.4 Changing Parameter Values in a Parameter File</h3>

You change the value of a parameter in a parameter file in one of the following ways:

+ By editing an initialization parameter file

In most cases,the new value takes effect the next time you start an instance of database.

+ By issusing an *ALTER SYSTEM SET  ... SCOPE=SPFILE* statement to update a server parameter file.
+ By issusing an *ALTER SYSTEM RESET ... SCOPE=SPFILE* statement to remove a parameter from a server parameter file,causing the default value to take effect the next you start an instance of the database.

<h3 id="1.5"> 1.5 Reading the Parameter Descriptions</h3>

<h3 id="1.6"> 1.6 Initialization Parameter Descriptions</h3>

### 1.7 Parameters by Functional Category

The following list shows the initialization parameters by their functional category:

+ ANSI Compliance
BLANK_TRIMMING
+ Backup and Restore
+ BFILES
+ Buffer Cache and I/O
+ Cursors and Library Cache
+ Database/Instance Identification
+ Diagnostics and Statistics
+ Distributed, Replication
+ File Locations,Names,and Sizes
+ Globalization
+ JAVA
+ Job Queues
+ License Limits
+ Memory
+ Miscellaneous
+ Networking
+ Objects and LOBs
+ OLAP
+ Optimizer
+ Parallel Execution
+ PL/SQL
+ PL/SQL Complier
+ SGA Memory
+ Oracle RAC
+ Redo Logs,Archiving,and Recovery
+ Resource Manager 
+ Security and Auditing 
+ Sessions and Processes
+ Shared Server Architecture
+ Standby Database
+ Temporary Sort Space
+ Transactions
+ Undo Management

### 1.8 Modifiable Parameters

Some initialization parameters can be modified using the *ALTER SESSION* or *ALTER SYSTEM* statements while an instance is running.Use the following initialization parameters:

```
ALTER SESSION SET parameter_name = value
ALTER SYSTEM SET parameter_name = value[DERERRED]
```

Whenever a parameter is modified using the *ALTER SYSTEM* statement,the Oracle Database records the statement that modifies the parameter in the alert log.

The *ALTER SESSION* statement changes the value of the specified parameter for the duration of the session that invokes the statement.The value of the parameter does not change for other sessions in the instance.The value of the following initialization parameters can be changed with *ALTER SESSION*:

```
ASM_POWER_LIMIT
COMMIT_LOGGING
COMMIT_WAIT
COMMIT_WRITE
CREATE_STORED_OUTLINES
CURSOR_BIND_CAPTURE_DESTINATION
CURSOR_SHARING
DB_BLOCK_CHECKING
DB_CREATE_FILE_DEST
DB_CREATE_ONLINE_LOG_DEST_n
DB_FILE_MULTIBLOCK_READ_COUNT
...
```

The *ALTER SYSTEM* statement without *DEFERRED* keyword modifies the global value of the parameters for all sessions in the instance,for the duration of the instance(until the database is shutdown).The value of the following initialization parameters can be changed with *ALTER SYSTEM*:

```
AQ_TM_PROCESSES
ARCHIVE_LAG_TARGET
ASM_DISKGROUPS
ASM_DISKSTRING
ASM_POWER_LIMIT
ASM_PREFERRED_READ_FAILURE_GROUPS
AWR_SNAPSHOT_TIME_OFFSET
BACKGROUND_DUMP_DEST
CIRCUITS
COMMIT_LOGGING
COMMIT_WAIT
...
```

The *ALTER SYSTEM DEFERRED* statement does not modify the global value of the parameter for existing sessions,but the value will be modified for future sessions that connect to the database.The value of the following initialization parameters can be changed with *ALTER SYSTEM ... DEFERRED*

### 1.8 Displaying Current Parameter Values 

To see the current settings for initialization parameters,use the following `SQL*Plus` command:

```
SQL> SHOW PARAMETERS
```

This command displays all parameters in alphabetical order,along with their current values.

Enter the following text string to display all parameters having *BLOCK* in their names:

```
SQL> SHOW PARAMETER BLOCK
```

You can use the *SPOOL* command to write the output to a file.

### 1.9 Parameters You Should Not Specify in the Parameter File

You should not specify the following two types of parameters in your parameter files:

+ Parameters that you never alter except when instructed to do so by Oracle to resolve a problem
+ Derived parameters,which normally do not need altering because their values are calculated automatically by the Oracle database server.

### 1.10 When Parameters Are Set Incorrectly 

Some parameters have a minimum setting below which an Oracle instance will not start.For other parameters,setting the value too low or too high may cause Oracle to perform badly,but it will still run.Also Oracle may convert some values outside the acceptable range to usable levels.

If a parameter value is too low or too high,or you have reached maximum for some resource,then Oracle returned an error.Frequently,you can wait a short while and retry the operation when the system is not as busy.If a message occurs repeatedly,then you should shutdown the instance,adjust the revevant parameter,and restart the instance.

### 1.11 Reading the Parameter Descriptions

The parameter descriptions in this chapter adhere to the following format:
PARAMETER_NAME
Property                  Description
Parameter type      Specifies the type of the parameter:
                    ■ A Boolean parameter accepts either true or false as its value.
                    ■ A string parameter accepts any sequence of characters as its value, 
                    subject to the syntax for the parameter.
                    ■ An integer parameter accepts a 4-byte value that can range from 0 
                    to 232 - 1.
                    ■ A parameter file parameter accepts an initialization parameter file 
                    specification as its value.
                    ■ A big integer parameter accepts an 8-byte value that can range 
                    from 0 to 264 - 1. You specify a value for a big integer as an integer 
                    together with an optional modifier such as K, M, or G, which 
                    respectively denotes kilobytes, megabytes, or gigabytes.
                    For example, 1000, 100 KB, 50 MB and 2 GB are valid specifications for big integers.

Syntax              For string and big integer parameters, specifies the valid syntax for specifying the parameter.

Default value       Specifies the value this parameter assumes if not explicitly specified

Modifiable          Specifies whether the parameter can be changed for the current session (by an ALTER SESSION statement) 
                    or for all sessions in the current instance (by an ALTER SYSTEM statement):
                    

## 2 static data dictionary views

### 2.1 ALL_

### 2.2 DBA_

### 2.3 USER_

### 2.4 Others

## 3 dynamic performance views



## 4 Appendixes

### A Data