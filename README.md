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
      - [Docker (Recommended)](#docker-recommended)
      - [Deploying with Docker](#deploying-with-docker)
      - [Undeploying with Docker](#undeploying-with-docker)
      - [Updating the Docker Image](#updating-the-docker-image)
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
git clone https://github.com/FabricSoul/Henandog.git
```
### Dependencies
Henandog requires the following dependencies:
  * [discord.py](https://pypi.org/project/discord.py/)

### Configuration
Henandog requires a configuration file to run. You can create one by copying the `config.py.example` file and renaming it to `config.py`. You can then edit the file to add your bot's token and the prefix you want to use.

Certainly! Here's the updated portion of the README.md documentation with the bash scripts enclosed in a code snippet:

### Running

#### Docker (Recommended)
Henandog is available for Docker. You can run it using the following command:
```bash
docker build -t henandog .
docker run -d henandog
```

#### Deploying with Docker
To deploy Henandog with Docker, you can use the provided `deploy.sh` script:


Simply execute the `deploy.sh` script to build and run the Henandog container.

#### Undeploying with Docker
To undeploy Henandog and remove the running container, you can use the provided `undeploy.sh` script:


Execute the `undeploy.sh` script to stop and remove the running Henandog container.

#### Updating the Docker Image
If you need to update the Docker image for Henandog, you can use the provided `update.sh` script:


Run the `update.sh` script to stop and remove the existing container, build the updated image, and run a new container with the updated image.

Note: Make sure to give execute permissions to the scripts before running them using the following command: `chmod +x deploy.sh undeploy.sh update.sh`.


#### Python
You can also run it using Python. You can do so by running the following command:
```bash
python3 bot.py
```

---
## Commands
| Command  | Description                    |
| -------- | ------------------------------ |
| $timeout | Sets the timeout for the vote. |
| $kick    | Kicks a user from the server.  |
| $search  | Search on Google.              |

---
## License
Henandog is licensed under the [MIT License](./LICENSE).