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
      - [使用Docker部署](#使用docker部署)
      - [使用Docker取消部署](#使用docker取消部署)
      - [更新Docker镜像](#更新docker镜像)
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
Henandog提供了Docker镜像。您可以使用以下命令运行它：
```bash
docker build -t henandog .
docker run -d henandog
```

#### 使用Docker部署
要使用Docker部署Henandog，您可以使用提供的 `deploy.sh` 脚本：

只需执行 `deploy.sh` 脚本来构建和运行Henandog容器。

#### 使用Docker取消部署
要取消部署Henandog并删除正在运行的容器，您可以使用提供的 `undeploy.sh` 脚本：

执行 `undeploy.sh` 脚本以停止并删除正在运行的Henandog容器。

#### 更新Docker镜像
如果需要更新Henandog的Docker镜像，可以使用提供的 `update.sh` 脚本：

运行 `update.sh` 脚本以停止并删除现有容器，构建更新的镜像，并运行一个基于更新镜像的新容器。

注意：在运行这些脚本之前，请确保赋予它们执行权限，可以使用以下命令：`chmod +x deploy.sh undeploy.sh update.sh`。

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
| $search | 在谷歌上搜索。 |

---
## 许可证
Henandog 使用 [MIT 许可证](./LICENSE) 授权。