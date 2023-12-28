---
title: 使用 Docker 自托管方式在 Pelican 中集成 Twikoo 评论系统
slug: 
category: Pelican
keywords: 
tags: pelican twikoo
date: 2023-12-27
created: 2023-12-28 14:52:18
modified: 2023-12-28 16:17:43
status: 
summary: 
allDay: false
startTime: 14:30
endTime: 15:00
completed: null
---

由于 twikoo 提供了 [官方的容器和YAML文件](https://twikoo.js.org/backend.html#%E7%A7%81%E6%9C%89%E9%83%A8%E7%BD%B2-docker)，所以如果有自己的服务器，采用容器部署自托管方式就非常简便了，5 分钟即可完成部署。

## 服务器端

### YAML

由于我的服务器上已经运行了一个 nginx 容器服务，所以只在官方的 YAML 文件中加上网络的配置，将其加入到已有的 nginx 网络，并监听 twikoo 容器 8080 端口即可。

```YAML
version: "3"
services:
  twikoo:
    image: imaegoo/twikoo
    container_name: twikoo
    restart: unless-stopped
    environment:
      TWIKOO_THROTTLE: 1000
    volumes:
      - ./data:/app/data
    networks:
      - nginx-network

networks:
  nginx-network:
    name: nginx-network
    external: true
```

#### Twikoo + Nginx 容器

如果本来没有 Nginx 的话，可以使用以下 YAML 文件让 Twikoo 和 Nginx 一起启动，在同一个 YAML 里启动的容器会默认在同一个容器网络里：

```YAML
version: "3"
services:
  twikoo:
    image: imaegoo/twikoo
    container_name: twikoo
    restart: unless-stopped
    environment:
      TWIKOO_THROTTLE: 1000
    volumes:
      - ./data:/app/data
      - 
  nginx:
    container_name: nginx
    ports:
      - "8092:8092" # 设置想用的端口，以8092为例，前面是宿主机端口，后面是容器端口。
    restart: always
    volumes:
      - ./conf.d:/etc/nginx/conf.d
      - ./certs:var/certs/
```

### Nginx 代理

使用 Nginx 反向代理 twikoo 并进行 https 加密。 在很多情况下使用 https 加密是必要的，如果你的静态网站是使用 https 加密的，但是网页内的部分内容使用 http 通信，这在大部分现代浏览器上是不被允许的，请求会被拒绝。

在 nginx 配置文件里加上 server 块，设置你希望的监听端口，此处设置为 8092（自定义）：

```nginx
server {
    listen  8092  ssl; # 配置想要监听的端口
    server_name  _;

    ssl_certificate      /certs/zerossl/certificate.crt;  # 配置自己的证书
    ssl_certificate_key  /certs/zerossl/private.key; # 配置自己的密钥


    location / {
        proxy_pass http://twikoo:8080;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
```

## 客户端

官方文档没有提供 pelican 客户端的配置示例，我在通用示例上做了一下修改以适应 pelican 模板。

在需要添加评论的网页（比如 article 模板文件下）的末尾添加以下脚本：

```html
  <div id="twikoo">
  </div>
  <script src="https://cdn.staticfile.org/twikoo/1.6.27/twikoo.all.min.js"></script>
  <script>
  twikoo.init({
    envId: 'https://xx.xxx.xxx.xx:8092/', <!-- 放上你的服务器的域名或IP地址以及Nginx监听的端口号 -->
    path: '{{ article.url }}'
  });
  </script>
```
