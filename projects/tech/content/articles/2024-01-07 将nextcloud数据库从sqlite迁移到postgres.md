---
title: 从 SQLite 到 PostgreSQL：Nextcloud 数据库迁移指南
slug: 
category: 
keywords: Nextcloud, SQLite, PostgreSQL, 数据库迁移, 容器部署
tags: nextcloud,sqlite,postgres,数据库 ,迁移 
date: 2024-01-07
created: 2024-01-07 18:10:37
modified: 2024-01-07 19:34:28
status: 
summary: 本指南详细说明了如何将容器部署的 Nextcloud 从 SQLite 数据库迁移到 PostgreSQL，以应对文件和用户数量增加的挑战。包含全面的步骤描述和必要的代码示例。
allDay: false
startTime: 18:00
endTime: 18:30
completed: null
---

## 1. 概述

Nextcloud 提供了灵活的部署选项，其中包括使用 SQLite 或 PostgreSQL 作为其后端数据库。随着用户数量和数据量的增长，可能会需要从轻量级的 SQLite 迁移到更强大的 PostgreSQL 数据库。本文档将指导您完成从 SQLite 到 PostgreSQL 的迁移过程，特别适用于容器化环境中的 Nextcloud 实例。

当前使用的 Docker Compose 配置如下，其中展示了基于 SQLite 的 Nextcloud 部署：

```yaml
version: '3'


services:
  nextcloud_app:
    image: nextcloud
    container_name: nextcloud_container
    restart: always
    volumes:
      - apps:/var/www/html/custom_apps
      - config:/var/www/html/config
      - data:/var/www/html/data
      - qbittorrent_qbittorrent_shared_downloads:/mnt/qbittorrent_shared_downloads
    environment:
      - TZ=Asia/Shanghai
    networks:
      - nginx-network

networks:
  nginx-network:
    name: nginx-network
    external: true

volumes:
  apps:
  config:
  data:
  qbittorrent_qbittorrent_shared_downloads:
    external: true
```

## 2. 迁移策略

迁移 Nextcloud 数据库涉及以下主要步骤：更新 Docker Compose 配置以包含 PostgreSQL 服务，执行数据库迁移命令，修改 Nextcloud 配置以连接新的数据库，最后重启服务以应用更改。

## 3. 实施步骤

### 3.1 更新 Docker Compose 文件

首先，将 PostgreSQL 容器配置添加到现有的 Docker Compose 文件中：

```yaml
version: '3'

services:
  nextcloud_app:
    image: nextcloud
    container_name: nextcloud_container
    restart: always
    volumes:
      - apps:/var/www/html/custom_apps
      - config:/var/www/html/config
      - data:/var/www/html/data
      - qbittorrent_qbittorrent_shared_downloads:/mnt/qbittorrent_shared_downloads
    environment:
      - TZ=Asia/Shanghai
      - POSTGRES_HOST=postgres
      - POSTGRES_DB=[数据库名]
      - POSTGRES_USER=[用户名]
      - POSTGRES_PASSWORD=[密码]
    networks:
      - nginx-network

  postgres:
    image: postgres
    restart: always
    volumes:
      - postgres_data:/var/lib/postgresql/data
    environment:
      - POSTGRES_DB=[数据库名]
      - POSTGRES_USER=[用户名]
      - POSTGRES_PASSWORD=[密码]
    networks:
      - nginx-network

networks:
  nginx-network:
    name: nginx-network
    external: true

volumes:
  apps:
  config:
  data:
  postgres_data:
  qbittorrent_qbittorrent_shared_downloads:
    external: true
```

确保正确设置 `POSTGRES_DB`, `POSTGRES_USER`, 和 `POSTGRES_PASSWORD` 环境变量。

### 3.2 执行数据库迁移

使用 Nextcloud 的 `occ` 命令工具进行数据库迁移。在 Docker **容器外部**执行以下命令：

```bash
docker exec -it -u www-data nextcloud_container php occ db:convert-type --all-apps pgsql [用户名] [密码] [数据库名]
```

这将迁移数据并保留原有结构。

### 3.3 修改 Nextcloud 配置

迁移完成后，更新 `config.php` 文件以反映新的数据库连接信息。示例如下：

```php
 'dbtype' => 'pgsql',
 'dbname' => 'nextcloud',  // PostgreSQL 数据库名
 'dbuser' => 'nextclouduser',  // PostgreSQL 用户名
 'dbpassword' => 'password',  // PostgreSQL 密码
 'dbhost' => 'postgres',  // PostgreSQL 主机名，如果在同一 Docker 网络可以使用服务名
 'dbport' => '',  // PostgreSQL 端口，如果使用默认端口可以留空
```

### 3.4 重启服务

重新启动 Nextcloud 服务以应用更改：

```bash
docker-compose restart nextcloud_container
```

### 3.5 验证和优化

确认数据库迁移成功并检查 Nextcloud 的性能。可选地，使用 `occ db:add-missing-indices` 命令添加任何缺失的数据库索引以优化性能。
