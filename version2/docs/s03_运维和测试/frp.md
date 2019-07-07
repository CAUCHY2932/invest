## frp

frpc

客户端



frps

服务端



frp下载之后，解压



首先，我们把frpc.exe和frpc.ini拷贝至c盘，目录结构如下图所示，当然你拷贝至其他盘也是一样的，看个人喜好了。



修改frpc.ini文件，

> [common]
>
> server_addr = 公网ip
>
> server_port = 5443
>
> token = frps填写的token
>
> 
>
> [rdp]
>
> type = tcp
>
> local_ip = 127.0.0.1
>
> local_port = 3389
>
> remote_port = 5200

3389嘛，是默认的远程端口了，5200就是当我mstsc请求公网时，后面加这个5200，就能转发到我这台装有frpc的电脑上。

然后启动服务

```
`c:\frpc\frpc.exe -c c:\frpc\frpc.ini`
```

可以看到类似如下的提示

```
`2019``/04/02` `22:53:54 [I] [service.go:221] login to server success, get run ``id` `[885ee37cd0e0191e], server udp port [0]``2019``/04/02` `22:53:54 [I] [proxy_manager.go:137] [885ee37cd0e0191e] proxy added: [rdp]``2019``/04/02` `22:53:54 [W] [control.go:142] [rdp] start error: port already used`
```

说明客户端也启动成功了！

这里有2点需要注意的

1、你的本地端口3389、5200防火墙得打开

2、你本机必须开启允许远程，我的是win10，需要勾选“允许远程连接此计算机”







最后，mstsc，公网ip+5200端口就可以远程该电脑了。





