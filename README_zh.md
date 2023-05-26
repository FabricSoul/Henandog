# Henandog

---
[中文](./README_zh.md) | [English](./README.md)


## 目录

- [Henandog](#henandog)
  - [目录](#目录)
  - [介绍](#介绍)
  - [安装](#安装)
    - [依赖项](#依赖项)
    - [配置](#配置)
    - [运行](#运行)
      - [Docker（推荐）](#docker推荐)
      - [使用 Docker 部署](#使用-docker-部署)
      - [Python](#python)
  - [命令](#命令)
  - [许可证](#许可证)

---
## 介绍
Henandog 是一个 Discord 机器人，允许您在服务器中发起投票。它使用 Python 编写，并使用 [discord.py](https://pypi.org/project/discord.py/) 库。

---
## 安装
Henandog 可在此存储库中获得。您可以使用以下命令克隆它：
```bash
git clone https://github.com/FabricSoul/Henandog.git
```
### 依赖项
Henandog 需要以下依赖项：
  * [discord.py](https://pypi.org/project/discord.py/)

### 配置
Henandog 需要一个配置文件才能运行。您可以通过复制 `config.py.example` 文件并将其重命名为 `config.py` 来创建一个配置文件。然后，您可以编辑该文件，添加您的机器人令牌和要使用的前缀。

### 运行

#### Docker（推荐）
Henandog 可以在 Docker 中运行。您可以使用以下命令运行它：
```bash
docker build -t henandog .
docker run -d henandog
```

#### 使用 Docker 部署
```bash
docker build -t henandog .
docker run -d --restart=always henandog
```

#### Python
您也可以使用 Python 运行它。您可以运行以下命令：
```bash
python3 bot.py
```

---
## 命令
| 命令 | 描述 |
| --- | --- |
| $timeout | 设置投票的超时禁言。 |
| $kick | 将用户踢出服务器。 |

---
## 许可证
Henandog 使用 [MIT 许可证](./LICENSE) 授权。