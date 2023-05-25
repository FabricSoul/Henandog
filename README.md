# Henandog

---
[中文](./README_zh.md) | [English](./README.md)

## Table of Contents

- [Henandog](#henandog)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Installation](#installation)
    - [Dependencies](#dependencies)
    - [Configuration](#configuration)
    - [Running](#running)
      - [Docker(Recommended)](#dockerrecommended)
      - [Deploying with Docker](#deploying-with-docker)
      - [Python](#python)
  - [Commands](#commands)
  - [License](#license)

---
## Introduction
Henandog is a Discord bot that allows you to initiate votes in your server. It is written in Python and uses the [discord.py](https://pypi.org/project/discord.py/) library.

---
## Installation
Henandog is available on this repository. You can clone it using the following command:
```bash
git clone Henandog_URL
```
### Dependencies
Henandog requires the following dependencies:
  * [discord.py](https://pypi.org/project/discord.py/)

### Configuration
Henandog requires a configuration file to run. You can create one by copying the `config.py.example` file and renaming it to `config.py`. You can then edit the file to add your bot's token and the prefix you want to use.

### Running

#### Docker(Recommended)
Henandog is available for Docker. You can run it using the following command:
```bash
docker build -t Henandog .
docker run -d Henandog
```

#### Deploying with Docker
```bash
docker build -t Henandog .
docker run -d --restart=always Henandog
```

#### Python
You can also run it using Python. You can do so by running the following command:
```bash
python3 bot.py
```

---
## Commands
| Command | Description |
| --- | --- |
| $timeout | Sets the timeout for the vote. |
| $kick | Kicks a user from the server. |

---
## License
Henandog is licensed under the [MIT License](./LICENSE).