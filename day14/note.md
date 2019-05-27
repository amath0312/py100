# PythonDay14: 网络编程入门

## 计算机网络基础
参考资料：  

> Andrew S.Tanenbaum老师的经典之作《计算机网络》  
> Kurose和Ross老师合著的《计算机网络:自顶向下方法》   



### 计算机网络发展史
- 1960s - 美国国防部ARPANET项目问世，奠定了分组交换网络的基础。
- 1980s - 国际标准化组织（ISO）发布OSI/RM，奠定了网络技术标准化的基础。
  - OSI七层模型：
    - 物理层：建立、维护、断开物理连接。
    - 数据链路层：建立逻辑连接、进行硬件地址寻址、差错校验等功能，由底层网络定义协议。将比特组合成字节进而组合成帧，用MAC地址访问介质，错误发现但不能纠正。
    - 网络层：进行逻辑地址寻址，实现不同网络之间的路径选择。协议有ICMP、IGMP、IP（IPV4、IPV6）、ARP、RARP。
    - 传输层：定义传输数据的协议端口号，以及流控和差错校验，协议有TCP、UDP，数据包一旦离开网卡即进入网络传输层。
    - 会话层：建立、管理、终止会话，对应主机进程，指本地主机与远程主机正在进行的会话。
    - 表示层：数据的表示、安全、压缩，如JPEG、ASCll、DECOIC、加密格式等。
    - 应用层：HTTP FTP TFTP SMTP SNMP DNS TELNET HTTPS POP3 DHCP。  
  - TCP/IP四层概念模型中，将物理层、数据链路层合并为网络接口层，将会话层、表示层和应用层合并为应用层。
- 1990s - 英国人[蒂姆·伯纳斯-李](https://zh.wikipedia.org/wiki/%E6%8F%90%E5%A7%86%C2%B7%E6%9F%8F%E5%85%A7%E8%8C%B2-%E6%9D%8E)发明了图形化的浏览器，浏览器的简单易用性使得计算机网络迅速被普及。

### TCP/IP模型
- 可靠的传输协议：
  
> 构成我们今天使用的Internet的基础的是TCP/IP协议族，所谓协议族就是一系列的协议及其构成的通信模型，我们通常也把这套东西称为TCP/IP模型。  

- 可靠的传输协议：
  - 数据不传丢不传错（利用握手、校验和重传机制可以实现）。
  - 流量控制（通过滑动窗口匹配数据发送者和接收者之间的传输速度）。
  - 拥塞控制（通过RTT时间以及对滑动窗口的控制缓解网络拥堵）。

### 网络应用模式
- C/S模式和B/S模式。
  - 这里的C指的是Client（客户端），通常是一个需要安装到某个宿主操作系统上的应用程序； 
  - 而B指的是Browser（浏览器），它几乎是所有图形化操作系统都默认安装了的一个应用软件； 
  - 通过C或B都可以实现对S（服务器）的访问。
- 去中心化的网络应用模式。
  - 不管是B/S还是C/S都需要服务器的存在
  - 服务器就是整个应用模式的中心
  - 而去中心化的网络应用通常没有固定的服务器或者固定的客户端，所有应用的使用者既可以作为资源的提供者也可以作为资源的访问者。

## 基于HTTP的网络资源访问
###HTTP
- [统一资源标识符](https://zh.wikipedia.org/wiki/統一資源標識符)
- [《HTTP 协议入门》](http://www.ruanyifeng.com/blog/2016/08/http.html)

### JSON
- 简捷、轻量、可读性

### requests库
> Requests是唯一的一个**非转基因**的Python HTTP库，人类可以安全享用。

### httpclient库



## 基于传输层协议的套接字编程
> 套接字：进程间通信和网络编程
> 实际开发中使用的套接字可以分为三类：  
>
> - 流套接字（TCP套接字）  
> - 数据报套接字
> - 原始套接字

### TCP套接字

**服务端**

```python
from socket import socket, SOCK_STREAM, AF_INET
server = socket(family=AF_INET, type=SOCK_STREAM)
server.bind(('192.168.1.2', 6789))
server.listen(512)
client, addr = server.accept()
client.send(str(datetime.now()).encode('utf-8'))
client.close()
```

**客户端**

```python
from socket import socket
client = socket()
client.connect(('192.168.1.2', 6789))
print(client.recv(1024).decode('utf-8'))
client.close()
```



### UDP套接字
> 不对传输的可靠性和可达性做出任何承诺从而避免了TCP中握手和重传的开销。
> 所以在强调性能和而不是数据完整性的场景中（例如传输网络音视频数据），UDP可能是更好的选择。
> 可能大家会注意到一个现象，就是在观看网络视频时，有时会出现卡顿，有时会出现花屏，这无非就是部分数据传丢或传错造成的

### 发送电子邮件

发送邮件要使用SMTP（简单邮件传输协议）  <br/>Python中的smtplib模块将这些操作简化成了几个简单的函数

> [参考代码](https://github.com/jackfrued/Python-100-Days/blob/master/Day01-15/Day14-B/网络应用开发.md#发送电子邮件)


### 发送短信

> [互亿无线](http://www.ihuyi.com/)短信平台（该平台为注册用户提供了50条免费短信以及常用开发语言发送短信的demo
>
> [参考代码](https://github.com/jackfrued/Python-100-Days/blob/master/Day01-15/Day14-B/网络应用开发.md#发送短信)
>
> [](https://github.com/jackfrued/Python-100-Days/blob/master/Day01-15/Day14-B/网络应用开发.md#发送短信)
>
> 

### 