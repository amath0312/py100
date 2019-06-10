# Linux操作系统

## 常用命令

- 获取登录信息：w / last / who / lastb
- 查看命令的说明和位置：whatis / whereis / which
- 关机：shutdown，取消关机： shutdown -c 
- 查看文件内容： cat / tac / head / tail / more / less / rev / od
- 文件分隔：split -l 100 file_prefix -#100行分隔一个
- 输出重定向和错误重定向 - > / >> / 2>
- 多重定向：tee，ls | tee -a ls.txt
- 字符流编辑器：sed，操作、过滤和转换文本内容
- 模式匹配和处理语言：awk
- 判断文件类型: file
- 去掉相邻重复内容: uniq
- 对内容排序: sort
- 编码转换: iconv, iconv -f gb2312 -t utf-8 qq.html
- 替换指定内容为新内容: tr, cat hello.txt | tr '\t' ','

## 用户管理

- useradd / userdel: useradd emmm -g emmm_grp
- groupadd / groupdel
- 修改密码：passwd
  - -l / -u - 锁定/解锁用户。
  - -d - 清除用户密码。
  - -e - 设置密码立即过期，用户登录时会强制要求修改密码。
  - -i - 设置密码过期多少天以后禁用该用户。
- 编辑sudoers文件: visudo

## 文件系统

- 格式化磁盘：mkfs -t ext4 -v /dev/sdb
- 转换或拷贝文件: dd, dd if=/dev/sda of=/home/username/sdadisk.img, if= 定义源驱动器，of= 定义你要将数据保存到的文件或位置
- 交换分区管理：mkswap / swapon / swapoff

## VIM

- 在命令模式下可以通过Ctrl+y和Ctrl+e来实现向上、向下滚动一行文本的操作，可以通过Ctrl+f和Ctrl+b来实现向前和向后翻页的操作
- 查找和替换：:{作用范围}s/{目标}/{替换}/{替换标志}
  - :5,12s/foo/bar/g #5-12行
  - :.,+2s/foo/bar/g #当前行与接下来两行
  - 空替换标志表示只替换从光标位置开始，目标的第一次出现
  - g - global：全局匹配，即替换目标的所有出现。
  - i - ignore case：忽略大小写匹配。
  - c - confirm：替换时需要确认。
  - e - error：忽略错误。
- 参数设定：在输入:进入末行模式后可以对 vim 进行设定。
  - 设置 Tab 键的空格数：set ts=4
  - 设置显示 / 不显示行号：set nu / set nonu
  - 设置启用 / 关闭高亮语法：syntax on / syntax off
  - 设置显示标尺（光标所在的行和列）： set ruler
  - 设置启用 / 关闭搜索结果高亮：set hls / set nohls
  - 说明：如果希望上面的这些设定在每次启动 vim 时都能自动生效，需要将这些设定写到用户主目录下的. vimrc 文件中。
- 比较多个文件：vim -d foo.txt bar.txt

## RPM

> rpm - Redhat Package Manager。

- 安装软件包：rpm -ivh <packagename>.rpm。
- 移除软件包：rpm -e <packagename>。
- 查询软件包：rpm -qa，例如可以用rpm -qa | grep mysql来检查是否安装了MySQL相关的软件包。

## 定时任务

- at / atq / atrm: 创建定时任务/查看定时任务队列/删除定时任务
- crontab：crontab -e 编辑定时任务（cron表达式）

## 网络访问和管理

- 文件同步工具： rsync
- 网络配置工具（新）：ip，ip address
- 网络监听抓包：tcpdump
- 查找与指定条件匹配的进程: pgrep, pgrep mysqld
- 终止进程：ps -ef | grep redis | grep -v grep | awk '{print $2}' | xargs kill
- 通过进程名或用户名终止进程： killall / pkill，pkill mysqld，pkill -u user_name
- 用户登出后进程继续工作：nohup，nohup ping www.baidu.com > result.txt &
- 跟踪进程系统调用情况：strace，strace -c -p 8803
- 后台进程
  - 查询后台进程：jobs
  - 让进程继续在后台运行(suspendes --> running)：bg %4
  - 将后台进程置于前台：fg %4

## 系统诊断

- 系统启动异常诊断：dmesg。
- 查看系统活动信息：sar，sar -u -r 5 10
  - -A - 显示所有设备（CPU、内存、磁盘）的运行状况。
  - -u - 显示所有CPU的负载情况。
  - -d - 显示所有磁盘的使用情况。
  - -r - 显示内存的使用情况。
  - -n - 显示网络运行状态。
- 查看内存使用情况： free
- 虚拟内存统计：vmstat
- CPU信息统计：mpstat
- 查看进程使用内存状况: pmap [pid]
- 报告设备CPU和I/O统计信息: iostat
- 显示所有PCI设备: lspci
- 显示进程间通信设施的状态：ipcs

