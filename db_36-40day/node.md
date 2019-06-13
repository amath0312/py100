# 关系数据库入门（RDB）

## MySQL

- 修改管理员秘密

    ``` sql
    -- 取消弱口令校验
    set global validate_password_policy=0;
    set global validate_password_length=6;
    -- 修改密码
    alter user 'root'@'localhost' identified by '123456';
    ```

- 查看服务器版本：select version();
- 事务：start transaction - commit - rollback
- 用户管理

    ``` sql
    -- 创建名为hellokitty的用户
    create user 'hellokitty'@'%' identified by '123123';

    -- 将对school数据库所有对象的所有操作权限授予hellokitty
    grant all privileges on school.* to 'hellokitty'@'%';

    -- 召回hellokitty对school数据库所有对象的insert/delete/update权限
    revoke insert, delete, update on school.* from 'hellokitty'@'%';
    ```

- 创建数据库：

    ``` sql
    -- 创建名为school的数据库并设置默认的字符集和排序方式
    create database school default charset utf8 collate utf8_bin;
    ```

- 创建数据表：

    ``` sql
    create table tb_record
        (
        recid int auto_increment comment '选课记录编号',
        sid int not null comment '选课学生',
        cid int not null comment '所选课程',
        seldate datetime default now() comment '选课时间日期',
        score decimal(4,1) comment '考试成绩',
        primary key (recid),
        foreign key (sid) references tb_student (stuid),
        foreign key (cid) references tb_course (couid),
        unique (sid, cid)
        );
    ```

- 

## 相关知识

### 范式理论

1. 第一范式：数据表的每个列的值域都是由原子值组成的，不能够再分割。
2. 第二范式：数据表里的所有数据都要和该数据表的键（主键与候选键）有完全依赖关系。
3. 第三范式：所有非键属性都只和候选键有相关性，也就是说非键属性之间应该是独立无关的。

### 数据完整性

1. 实体完整性 - 每个实体都是独一无二的
   - 主键（primary key） / 唯一约束 / 唯一索引（unique）
2. 引用完整性（参照完整性）- 关系中不允许引用不存在的实体
   - 外键（foreign key）
3. 域完整性 - 数据是有效的
   - 数据类型及长度
   - 非空约束（not null）
   - 默认值约束（default）
   - 检查约束（check）

### 数据一致性

1. 事务：一系列对数据库进行读/写的操作
2. 事务的ACID特性：
   - 原子性(atomicity)：事务作为一个整体被执行，包含在其中的对数据库的操作要么全部被执行，要么都不执行
   - 一致性(consistency)：事务应确保数据库的状态从一个一致状态转变为另一个一致状态
   - 隔离性(isolation)：多个事务并发执行时，一个事务的执行不应影响其他事务的执行
   - 持久性(durability)：已被提交的事务对数据库的修改应该永久保存在数据库中
